from flask import Flask, render_template, request, redirect, session, jsonify
import os
import pandas as pd
import matplotlib
matplotlib.use('Agg')   # 🔥 IMPORTANT FIX
from data_analyzer import analyze_data
from ollama_helper import ask_llm

app = Flask(__name__)
app.secret_key = "secret123"

# folders
os.makedirs("uploads", exist_ok=True)
os.makedirs("static/charts", exist_ok=True)


# 🏠 HOME
@app.route('/')
def home():
    return render_template("home.html")


# 🔐 LOGIN
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form.get('username')
        return redirect('/upload')
    return render_template("login.html")


# 📂 UPLOAD PAGE
@app.route('/upload', methods=['GET','POST'])
def upload():

    if request.method == 'POST':
        try:
            file = request.files['file']

            if not file or file.filename == "":
                return "❌ Please upload a file"

            path = os.path.join("uploads", file.filename)
            file.save(path)

            df, charts, preview, columns = analyze_data(path)

            # 🔥 AI INSIGHTS PROMPT
            prompt = f"""
You are an AI Data Analyst.

Dataset Preview:
{preview}

Give exactly 5 insights:
- Only data insights
- No column descriptions
- 1 line each
- Start with '-'
"""

            insights = ask_llm(prompt)

            # ensure exactly 5
            lines = [i.strip() for i in insights.split("\n") if i.strip()]
            while len(lines) < 5:
                lines.append("- Additional insight not available")

            insights = "\n".join(lines[:5])

            # save session
            session['file'] = path
            session['preview'] = preview
            session['columns'] = columns

            return render_template(
                "upload.html",
                charts=charts,
                insights=insights,
                columns=columns
            )

        except Exception as e:
            return f"❌ Error: {str(e)}"

    return render_template("upload.html")


# 🎯 CUSTOM CHART (FINAL FIXED)
@app.route('/custom_chart', methods=['POST'])
def custom_chart():
    import matplotlib.pyplot as plt

    try:
        if 'file' not in session:
            return jsonify({"error": "Upload dataset first"})

        df = pd.read_csv(session['file'])

        col1 = request.form.get('col1')
        col2 = request.form.get('col2')
        chart = request.form.get('chart')

        numeric_cols = df.select_dtypes(include='number').columns

        # 🔥 UNIQUE FILE NAME (IMPORTANT FIX)
        filename = f"custom_{col1}_{col2}_{chart}.png"
        path = f"static/charts/{filename}"

        plt.figure()

        # BAR / LINE / PIE
        if chart in ["bar", "line", "pie"]:
            if col2 not in numeric_cols:
                return jsonify({"error": "Select numeric column for Y-axis"})

            data = df.groupby(col1)[col2].sum()

            if chart == "bar":
                data.plot(kind='bar')
            elif chart == "line":
                data.plot(kind='line')
            elif chart == "pie":
                data.plot(kind='pie')

            plt.xlabel(col1)
            plt.ylabel(col2)

        # SCATTER
        elif chart == "scatter":
            if col1 not in numeric_cols or col2 not in numeric_cols:
                return jsonify({"error": "Scatter needs numeric columns"})

            plt.scatter(df[col1], df[col2])
            plt.xlabel(col1)
            plt.ylabel(col2)

        # HISTOGRAM
        elif chart == "hist":
            if col1 not in numeric_cols:
                return jsonify({"error": "Histogram needs numeric column"})

            df[col1].plot(kind='hist')
            plt.xlabel(col1)
            plt.ylabel("Frequency")

        else:
            return jsonify({"error": "Invalid chart type"})

        # 🔥 TITLE FIX
        if chart == "scatter":
            plt.title(f"{col1} vs {col2}")
        elif chart in ["bar", "line", "pie"]:
            plt.title(f"{col2} by {col1}")
        elif chart == "hist":
            plt.title(f"Distribution of {col1}")

        plt.tight_layout()

        # 🔥 CLEAR OLD + SAVE NEW
        plt.savefig(path)
        plt.close()

        # return correct path
        return jsonify({"path": path})

    except Exception as e:
        return jsonify({"error": str(e)})


# 🤖 CHATBOT
@app.route('/chat', methods=['POST'])
def chat():
    try:
        question = request.form.get('question')
        preview = session.get('preview', '')

        prompt = f"""
You are Data Bot.

Dataset:
{preview}

Answer in 1-2 short lines:
{question}
"""
        response = ask_llm(prompt)
        return response.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# 🚀 RUN
if __name__ == "__main__":
    app.run(debug=True)