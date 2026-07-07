"""
Epic 5: Application Building

Flask web app that loads the best trained model + scaler and serves
a prediction UI. Run with: python app.py  (from inside the app/ directory)
"""

import os
import sys
import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src"))
import config

app = Flask(__name__)

# ---------------------------------------------------------------------------
# Load model artifacts at startup
# ---------------------------------------------------------------------------
model = None
scaler = None
feature_columns = None
load_error = None

try:
    model = joblib.load(config.BEST_MODEL_PATH)
    scaler = joblib.load(config.SCALER_PATH)
    feature_columns = joblib.load(config.FEATURE_COLUMNS_PATH)
    print(f"[app] Loaded model, scaler, and {len(feature_columns)} feature columns.")
except FileNotFoundError as e:
    load_error = (
        "No trained model found. Run `python src/train_models.py` from the "
        "project root first, then restart the app."
    )
    print(f"[app] WARNING: {load_error}\nDetails: {e}")


def get_form_fields():
    """Build (column_name, friendly_label) pairs for the HTML form."""
    cols = feature_columns or []
    return [(c, config.FEATURE_LABELS.get(c, c.title())) for c in cols]


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", fields=get_form_fields(), load_error=load_error)


@app.route("/predict", methods=["POST"])
def predict():
    if load_error:
        return render_template("index.html", fields=get_form_fields(), load_error=load_error)

    try:
        values = []
        for col in feature_columns:
            raw = request.form.get(col, "0")
            values.append(float(raw))

        X = pd.DataFrame([values], columns=feature_columns)
        X_scaled = scaler.transform(X)

        pred = model.predict(X_scaled)[0]
        proba = None
        if hasattr(model, "predict_proba"):
            proba = float(model.predict_proba(X_scaled)[0][1]) * 100

        result = {
            "prediction": "Flood Likely" if int(pred) == 1 else "Flood Unlikely",
            "is_flood": int(pred) == 1,
            "probability": f"{proba:.1f}%" if proba is not None else "N/A",
            "inputs": dict(zip(feature_columns, values)),
        }
        return render_template("result.html", result=result)

    except Exception as e:
        return render_template(
            "index.html",
            fields=get_form_fields(),
            load_error=f"Prediction failed: {e}",
        )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
