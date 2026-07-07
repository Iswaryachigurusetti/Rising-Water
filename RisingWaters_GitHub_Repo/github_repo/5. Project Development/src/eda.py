"""
Epic 2: Visualizing and Analysing the Data

Generates exploratory plots and saves them to notebooks/plots/.
Run standalone: python src/eda.py
"""

import sys
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # headless-safe backend
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config
from data_preprocessing import load_raw_data, clean_data, encode_target, _find_target_column


def run_eda():
    df = load_raw_data()
    target_col = _find_target_column(df)
    df = clean_data(df)
    df_encoded = encode_target(df, target_col)

    numeric_df = df.select_dtypes(include="number")

    # 1. Target class balance
    plt.figure(figsize=(6, 4))
    df_encoded[target_col].value_counts().sort_index().plot(kind="bar", color=["#4C72B0", "#C44E52"])
    plt.title("Flood vs No-Flood Class Distribution")
    plt.xlabel("Flood (1) / No Flood (0)")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(config.PLOTS_DIR, "01_class_distribution.png"))
    plt.close()

    # 2. Correlation heatmap
    plt.figure(figsize=(10, 8))
    corr = numeric_df.corr()
    sns.heatmap(corr, cmap="coolwarm", annot=False)
    plt.title("Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(os.path.join(config.PLOTS_DIR, "02_correlation_heatmap.png"))
    plt.close()

    # 3. Annual rainfall distribution (if present)
    if "ANNUAL" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.histplot(df["ANNUAL"].dropna(), kde=True, color="#55A868")
        plt.title("Distribution of Annual Rainfall")
        plt.xlabel("Annual Rainfall (mm)")
        plt.tight_layout()
        plt.savefig(os.path.join(config.PLOTS_DIR, "03_annual_rainfall_distribution.png"))
        plt.close()

    # 4. Seasonal rainfall averages (or monthly, whichever this dataset has)
    month_cols = [c for c in ["JAN", "FEB", "MAR", "APR", "MAY", "JUN",
                               "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"] if c in df.columns]
    season_cols = [c for c in ["Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec"] if c in df.columns]
    bar_cols = month_cols or season_cols
    if bar_cols:
        plt.figure(figsize=(10, 5))
        df[bar_cols].mean().plot(kind="bar", color="#4C72B0")
        plt.title("Average Rainfall by Period")
        plt.ylabel("Rainfall (mm)")
        plt.tight_layout()
        plt.savefig(os.path.join(config.PLOTS_DIR, "04_seasonal_rainfall_avg.png"))
        plt.close()

    # 4b. Temperature / Humidity / Cloud Cover distributions (this dataset's
    # extra meteorological features, beyond rainfall alone)
    extra_cols = [c for c in ["Temp", "Humidity", "Cloud Cover"] if c in df.columns]
    if extra_cols:
        fig, axes = plt.subplots(1, len(extra_cols), figsize=(5 * len(extra_cols), 4))
        if len(extra_cols) == 1:
            axes = [axes]
        for ax, col in zip(axes, extra_cols):
            sns.histplot(df[col].dropna(), kde=True, ax=ax, color="#DD8452")
            ax.set_title(col)
        plt.tight_layout()
        plt.savefig(os.path.join(config.PLOTS_DIR, "04b_temp_humidity_cloud.png"))
        plt.close()

    # 5. Annual rainfall vs flood occurrence (if both present)
    if "ANNUAL" in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(x=df_encoded[target_col], y=df["ANNUAL"])
        plt.title("Annual Rainfall vs Flood Occurrence")
        plt.xlabel("Flood (1) / No Flood (0)")
        plt.ylabel("Annual Rainfall (mm)")
        plt.tight_layout()
        plt.savefig(os.path.join(config.PLOTS_DIR, "05_annual_vs_flood.png"))
        plt.close()

    print(f"[eda] Saved plots to {config.PLOTS_DIR}")


if __name__ == "__main__":
    run_eda()
