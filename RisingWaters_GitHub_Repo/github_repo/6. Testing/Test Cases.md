# 6. Test Cases

## 6.1 Data Pre-processing Tests

| Test Case ID | Description | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-01 | Load dataset from Excel | `flood_dataset.xlsx` | 115 rows, 11 columns loaded successfully | 115 rows, 11 columns loaded | Pass |
| TC-02 | Missing target column | CSV/Excel with no `flood`-like column | Raises clear `ValueError` naming the missing column | Raises `ValueError` with column list | Pass |
| TC-03 | Missing numeric values | Dataset with NaNs in a feature column | NaNs filled with column median, logged to console | Verified via console log message | Pass |
| TC-04 | Duplicate rows | Dataset with duplicate rows | Duplicates dropped, count logged | Verified via console log message | Pass |
| TC-05 | Target encoding (numeric) | `flood` column already 0/1 | Left as 0/1 ints | Preserved correctly | Pass |
| TC-06 | Target encoding (text) | `flood` column as YES/NO | Mapped to 1/0 respectively | Verified via unit check | Pass |
| TC-07 | Train/test split | 115 rows | 92 train / 23 test (80/20 stratified) | 92 train / 23 test | Pass |

## 6.2 Model Training Tests

| Test Case ID | Description | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-08 | Train Decision Tree | Scaled train set | Model trains without error, evaluates on test set | Accuracy 95.65% | Pass |
| TC-09 | Train Random Forest | Scaled train set | Model trains without error, evaluates on test set | Accuracy 95.65% | Pass |
| TC-10 | Train KNN | Scaled train set | Model trains without error, evaluates on test set | Accuracy 86.96% | Pass |
| TC-11 | Train XGBoost | Scaled train set | Model trains without error, evaluates on test set | Accuracy varies by run; typically 90%+ | Pass |
| TC-12 | Best model selection | Results dict from all 4 models | Best model (by accuracy, tie-break F1) is saved | Decision Tree saved as `best_model.pkl` | Pass |
| TC-13 | Metrics persistence | Trained models | `metrics.json` contains all 4 models' scores + best model name | File created with correct structure | Pass |

## 6.3 Flask Application Tests

| Test Case ID | Description | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC-14 | Load home page | `GET /` | HTTP 200, form renders with all feature fields | HTTP 200, form rendered | Pass |
| TC-15 | Valid prediction request | `POST /predict` with all 10 valid numeric fields | HTTP 200, prediction + probability shown | HTTP 200, "Flood Unlikely"/"Flood Likely" shown correctly | Pass |
| TC-16 | Missing model artifacts | App started before `train_models.py` run | Home page shows clear warning instead of crashing | Warning message displayed | Pass |
| TC-17 | Invalid form input (non-numeric) | `POST /predict` with a text value in a numeric field | App catches exception, re-renders form with error message | Error message shown, no server crash | Pass |
| TC-18 | Prediction consistency | Same input submitted twice | Identical prediction returned both times | Confirmed identical | Pass |

## 6.4 Cross-Browser / UI Checks

| Test Case ID | Description | Expected Result | Status |
|---|---|---|---|
| TC-19 | Responsive layout on mobile width | Form fields stack to single column below 480px | Pass |
| TC-20 | Result page navigation | "Run Another Prediction" link returns to home form | Pass |
