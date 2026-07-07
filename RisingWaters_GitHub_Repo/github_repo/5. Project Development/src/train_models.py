"""
Epic 4: Model Building

Trains Decision Tree, Random Forest, KNN, and XGBoost classifiers,
evaluates each on the held-out test set, and saves the best-performing
model (by test accuracy) to disk for the Flask app to load.
"""

import sys
import os
import json
import joblib
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
try:
    from xgboost import XGBClassifier
    XGBOOST_AVAILABLE = True
except ImportError:
    XGBOOST_AVAILABLE = False
    print("[train_models] WARNING: xgboost is not installed. Run "
          "`pip install xgboost` to include it. Continuing without it.")
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, confusion_matrix, classification_report,
)

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config
from data_preprocessing import preprocess


def build_models():
    models = {
        "Decision Tree": DecisionTreeClassifier(**config.DECISION_TREE_PARAMS),
        "Random Forest": RandomForestClassifier(**config.RANDOM_FOREST_PARAMS),
        "KNN": KNeighborsClassifier(n_neighbors=config.KNN_NEIGHBORS),
    }
    if XGBOOST_AVAILABLE:
        models["XGBoost"] = XGBClassifier(**config.XGBOOST_PARAMS)
    return models


def evaluate(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)
    cm = confusion_matrix(y_test, y_pred).tolist()

    print(f"\n{'=' * 50}")
    print(f"Model: {name}")
    print(f"{'=' * 50}")
    print(f"Accuracy : {acc * 100:.2f}%")
    print(f"Precision: {prec * 100:.2f}%")
    print(f"Recall   : {rec * 100:.2f}%")
    print(f"F1 Score : {f1 * 100:.2f}%")
    print("Confusion Matrix:")
    print(np.array(cm))
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, zero_division=0))

    return {
        "accuracy": acc,
        "precision": prec,
        "recall": rec,
        "f1": f1,
        "confusion_matrix": cm,
    }


def main():
    print("[train_models] Starting preprocessing...")
    X_train, X_test, y_train, y_test, feature_columns, scaler = preprocess()

    models = build_models()
    results = {}
    trained_models = {}

    for name, model in models.items():
        print(f"\n[train_models] Training {name}...")
        model.fit(X_train, y_train)
        trained_models[name] = model
        results[name] = evaluate(model, X_test, y_test, name)

    # Pick best by accuracy (ties broken by F1)
    best_name = max(results, key=lambda n: (results[n]["accuracy"], results[n]["f1"]))
    best_model = trained_models[best_name]

    print(f"\n{'#' * 50}")
    print(f"BEST MODEL: {best_name}  "
          f"(Accuracy: {results[best_name]['accuracy'] * 100:.2f}%)")
    print(f"{'#' * 50}")

    joblib.dump(best_model, config.BEST_MODEL_PATH)
    print(f"[train_models] Saved best model to {config.BEST_MODEL_PATH}")

    summary = {
        "best_model": best_name,
        "results": results,
        "feature_columns": feature_columns,
    }
    with open(config.METRICS_PATH, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"[train_models] Saved metrics summary to {config.METRICS_PATH}")

    return summary


if __name__ == "__main__":
    main()
