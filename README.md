🚀 DataVision AI – AI-Powered Data Analyst Web App

Transform raw data into meaningful insights instantly using AI.
Upload datasets, generate dashboards, and interact with your data through a smart chatbot — all in one place.

📌 Overview

DataVision AI is a Flask-based web application that simplifies data analysis for users without requiring technical expertise.
It automatically processes datasets, generates visualizations, and provides AI-powered insights using a local LLM.

✨ Features
* Simple Login System
* Upload CSV / Excel datasets
* Automatic chart generation (Bar, Line, Pie, Scatter, Histogram)
* AI-generated key insights (5 bullet points)
* Custom chart creation (choose columns + chart type)
*  Built-in chatbot to query dataset
*  Displays dataset fields dynamically
*  Modern responsive UI
Tech Stack
Frontend
HTML
CSS
JavaScript
Backend
Flask (Python)
Data Processing
Pandas
Visualization
Matplotlib
AI Integration
Project Structure
project/
│── app.py
│── data_analyzer.py
│── ollama_helper.py
│
├── templates/
│   ├── home.html
│   ├── login.html
│   └── upload.html
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── charts/
│
├── uploads/
│
└── requirements.txt

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/datavision-ai.git
cd datavision-ai
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Install & Run Ollama

Make sure Ollama is installed and running:

ollama run llama3

*Workflow
User logs in
Uploads dataset (CSV/Excel)
System processes data using Pandas
Charts are generated using Matplotlib
AI generates insights using Ollama
Dashboard displays results
User interacts using chatbot or custom charts
Ollama (Local LLM)

AI Capabilities
Prompt-based insight generation
Context-aware responses
Conversational chatbot
Structured output formatting
📊 Supported Charts
Bar Chart
Line Chart
Pie Chart
Scatter Plot
Histogram
📌 Use Cases
Data analysis for beginners
Academic projects
Quick business insights
Exploratory Data Analysis (EDA)

 Author

Gopika
AI & Data Analytics Enthusiast
