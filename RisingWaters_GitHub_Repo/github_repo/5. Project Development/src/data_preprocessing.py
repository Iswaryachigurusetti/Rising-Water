"""
Epic 3: Data Pre-processing

Loads the raw rainfall CSV, cleans it, engineers a numeric target,
handles missing values, and returns train/test splits ready for modeling.
"""

import sys
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import config

# Common alternate spellings we'll auto-detect if config.TARGET_COLUMN
# isn't found verbatim in the CSV.
TARGET_ALIASES = ["FLOODS", "Flood", "flood", "FLOOD", "flood_occurred", "Flooded", "target"]


def _find_target_column(df: pd.DataFrame) -> str:
    if config.TARGET_COLUMN in df.columns:
        return config.TARGET_COLUMN
    for alias in TARGET_ALIASES:
        if alias in df.columns:
            print(f"[data_preprocessing] Note: using '{alias}' as target column "
                  f"(config.TARGET_COLUMN='{config.TARGET_COLUMN}' not found).")
            return alias
    raise ValueError(
        f"Could not find a target/flood column in the dataset.\n"
        f"Columns found: {list(df.columns)}\n"
        f"Please set TARGET_COLUMN in src/config.py to the correct column name."
    )


def load_raw_data() -> pd.DataFrame:
    if not os.path.exists(config.DATA_PATH):
        raise FileNotFoundError(
            f"Dataset not found at {config.DATA_PATH}\n"
            f"Download it from https://www.kaggle.com/datasets/arbethi/rainfall-dataset "
            f"and place the file at that path."
        )
    ext = os.path.splitext(config.DATA_PATH)[1].lower()
    if ext in (".xlsx", ".xls"):
        df = pd.read_excel(config.DATA_PATH)
    else:
        df = pd.read_csv(config.DATA_PATH)
    df.columns = [c.strip() for c in df.columns]  # trim stray whitespace in headers
    print(f"[data_preprocessing] Loaded {df.shape[0]} rows, {df.shape[1]} columns.")
    print(f"[data_preprocessing] Columns: {list(df.columns)}")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Drop fully empty rows/columns
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    # Fill missing numeric values with column median (robust to outliers)
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if df[col].isna().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"[data_preprocessing] Filled {df[col].isna().sum()} missing "
                  f"values in '{col}' with median={median_val:.2f}")

    # Drop duplicate rows
    before = len(df)
    df.drop_duplicates(inplace=True)
    if len(df) < before:
        print(f"[data_preprocessing] Dropped {before - len(df)} duplicate rows.")

    return df


def encode_target(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    df = df.copy()
    if df[target_col].dtype == object:
        df[target_col] = (
            df[target_col]
            .astype(str)
            .str.strip()
            .str.lower()
            .apply(lambda v: 1 if v in config.POSITIVE_LABELS else 0)
        )
    else:
        # Already numeric (0/1) — coerce just in case of floats like 1.0
        df[target_col] = df[target_col].apply(lambda v: 1 if v in (1, 1.0, True) else 0)
    return df


def get_feature_columns(df: pd.DataFrame, target_col: str) -> list:
    if config.FEATURE_COLUMNS:
        missing = [c for c in config.FEATURE_COLUMNS if c not in df.columns]
        if missing:
            print(f"[data_preprocessing] Warning: configured FEATURE_COLUMNS not "
                  f"found in data: {missing}. Falling back to auto-detected numeric columns.")
        else:
            return config.FEATURE_COLUMNS

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    exclude = set(config.DROP_COLUMNS + [target_col])
    return [c for c in numeric_cols if c not in exclude]


def preprocess(save_scaler: bool = True):
    """
    Full preprocessing pipeline. Returns:
        X_train, X_test, y_train, y_test, feature_columns, scaler
    """
    df = load_raw_data()
    target_col = _find_target_column(df)
    df = clean_data(df)
    df = encode_target(df, target_col)

    feature_columns = get_feature_columns(df, target_col)
    if not feature_columns:
        raise ValueError("No usable numeric feature columns found. Check config.FEATURE_COLUMNS.")

    print(f"[data_preprocessing] Using {len(feature_columns)} feature columns: {feature_columns}")

    X = df[feature_columns].astype(float)
    y = df[target_col].astype(int)

    print(f"[data_preprocessing] Target distribution:\n{y.value_counts()}")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=config.TEST_SIZE,
        random_state=config.RANDOM_STATE,
        stratify=y if y.nunique() > 1 else None,
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    if save_scaler:
        import joblib
        joblib.dump(scaler, config.SCALER_PATH)
        joblib.dump(feature_columns, config.FEATURE_COLUMNS_PATH)
        print(f"[data_preprocessing] Saved scaler to {config.SCALER_PATH}")
        print(f"[data_preprocessing] Saved feature column list to {config.FEATURE_COLUMNS_PATH}")

    return X_train_scaled, X_test_scaled, y_train, y_test, feature_columns, scaler


if __name__ == "__main__":
    preprocess()
    print("[data_preprocessing] Done.")
