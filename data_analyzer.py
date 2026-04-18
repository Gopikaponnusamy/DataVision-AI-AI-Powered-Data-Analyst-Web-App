import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

def analyze_data(path):
    df = pd.read_csv(path)

    charts = []
    os.makedirs("static/charts", exist_ok=True)

    # clear old charts
    for f in os.listdir("static/charts"):
        os.remove("static/charts/"+f)

    num_cols = df.select_dtypes(include='number').columns

    for col in num_cols[:2]:
        # Histogram
        plt.figure()
        df[col].plot(kind='hist')
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")

        p = f"static/charts/{col}_hist.png"
        plt.savefig(p)
        plt.close()
        charts.append(p)

        # Line
        plt.figure()
        df[col].plot(kind='line')
        plt.title(f"{col} Trend")
        plt.xlabel("Index")
        plt.ylabel(col)

        p = f"static/charts/{col}_line.png"
        plt.savefig(p)
        plt.close()
        charts.append(p)

    return df, charts, df.head().to_string(), list(df.columns)