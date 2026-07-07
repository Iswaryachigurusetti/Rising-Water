"""
Full pipeline walkthrough, runnable end-to-end as a single script
(useful for pasting into a Jupyter Notebook cell-by-cell, or running
in Google Colab). Mirrors: EDA -> Preprocessing -> Model Building.

Run from the project root:
    python notebooks/flood_prediction_walkthrough.py
"""

import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))

# Epic 1: Data Collection — place your Kaggle CSV at data/rainfall_dataset.csv
# (see README.md section 2 for details)

# Epic 2: Visualizing and Analysing the Data
from eda import run_eda

# Epic 3 + 4: Preprocessing and Model Building
from train_models import main as train_all_models

if __name__ == "__main__":
    print("### STEP 1: Exploratory Data Analysis ###")
    run_eda()

    print("\n### STEP 2 & 3: Preprocessing + Training all models ###")
    summary = train_all_models()

    print("\n### DONE ###")
    print(f"Best model: {summary['best_model']}")
    print("Now run the Flask app:  cd app && python app.py")
