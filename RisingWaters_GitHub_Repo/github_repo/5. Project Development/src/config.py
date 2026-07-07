"""
Central configuration for the Flood Prediction project.

Edit this file if your actual downloaded CSV has different column names
than the standard Indian rainfall/flood dataset schema assumed below.
Every other script imports its settings from here, so this is the ONE
place you need to touch.
"""

import os

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "flood_dataset.xlsx")
# Supplementary raw rainfall archive (not used directly for training, but
# kept for Epic 1 / reference — 1901-2015 rainfall by Indian state).
RAINFALL_ARCHIVE_PATH = os.path.join(BASE_DIR, "data", "rainfall_india_1901_2015.xlsx")
MODELS_DIR = os.path.join(BASE_DIR, "models")
PLOTS_DIR = os.path.join(BASE_DIR, "notebooks", "plots")

os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(PLOTS_DIR, exist_ok=True)

BEST_MODEL_PATH = os.path.join(MODELS_DIR, "best_model.pkl")
SCALER_PATH = os.path.join(MODELS_DIR, "scaler.pkl")
FEATURE_COLUMNS_PATH = os.path.join(MODELS_DIR, "feature_columns.pkl")
LABEL_ENCODER_PATH = os.path.join(MODELS_DIR, "label_encoder.pkl")
METRICS_PATH = os.path.join(MODELS_DIR, "metrics.json")

# ---------------------------------------------------------------------------
# Column configuration
# ---------------------------------------------------------------------------
# Target column: the flood label. Common alternate names are auto-detected
# in data_preprocessing.py if this exact name isn't found.
TARGET_COLUMN = "flood"

# Values in TARGET_COLUMN that mean "yes, a flood occurred".
# Only used if the column is text; this dataset's target is already 0/1.
POSITIVE_LABELS = {"yes", "y", "1", "true"}

# Columns to drop before modeling (identifiers / non-predictive text columns).
DROP_COLUMNS = []

# Feature columns used for prediction — matches the actual flood_dataset.xlsx
# schema: temperature, humidity, cloud cover, and seasonal/annual rainfall
# totals. If left as None, the code will auto-use "every numeric column
# except the target and DROP_COLUMNS".
FEATURE_COLUMNS = [
    "Temp", "Humidity", "Cloud Cover", "ANNUAL",
    "Jan-Feb", "Mar-May", "Jun-Sep", "Oct-Dec",
    "avgjune", "sub",
]

# Friendly labels shown on the web form (falls back to the raw column name
# if not listed here).
FEATURE_LABELS = {
    "Temp": "Temperature (°C)",
    "Humidity": "Humidity (%)",
    "Cloud Cover": "Cloud Cover (%)",
    "ANNUAL": "Annual Rainfall (mm)",
    "Jan-Feb": "Jan-Feb Rainfall (mm)",
    "Mar-May": "Mar-May Rainfall (mm)",
    "Jun-Sep": "Jun-Sep Rainfall (mm)",
    "Oct-Dec": "Oct-Dec Rainfall (mm)",
    "avgjune": "Average June Rainfall (mm)",
    "sub": "Subdivision Rainfall Index (mm)",
}

# ---------------------------------------------------------------------------
# Train/test split & model settings
# ---------------------------------------------------------------------------
TEST_SIZE = 0.2
RANDOM_STATE = 42

KNN_NEIGHBORS = 5

RANDOM_FOREST_PARAMS = {
    "n_estimators": 200,
    "max_depth": None,
    "random_state": RANDOM_STATE,
}

XGBOOST_PARAMS = {
    "n_estimators": 200,
    "max_depth": 5,
    "learning_rate": 0.1,
    "use_label_encoder": False,
    "eval_metric": "logloss",
    "random_state": RANDOM_STATE,
}

DECISION_TREE_PARAMS = {
    "max_depth": 8,
    "random_state": RANDOM_STATE,
}
