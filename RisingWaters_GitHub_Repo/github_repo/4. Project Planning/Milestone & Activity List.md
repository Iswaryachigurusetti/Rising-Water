# 4. Milestone & Activity List

## Sprint Plan

| Sprint | Epic | Activities | Duration | Status |
|---|---|---|---|---|
| Sprint 1 | Epic 1: Data Collection | Source dataset (Kaggle rainfall/flood data), verify schema, place files in `data/` | 1 day | Done |
| Sprint 1 | Epic 2: Visualizing and Analysing the Data | Class balance plot, correlation heatmap, feature distributions, rainfall-vs-flood boxplot (`src/eda.py`) | 2 days | Done |
| Sprint 2 | Epic 3: Data Pre-processing | Handle missing values, encode target, feature/target split, scaling, persist scaler (`src/data_preprocessing.py`) | 2 days | Done |
| Sprint 2 | Epic 4: Model Building | Train Decision Tree, Random Forest, KNN, XGBoost; evaluate; auto-select and persist best model (`src/train_models.py`) | 3 days | Done |
| Sprint 3 | Epic 5: Application Building | Build Flask app, input form, prediction route, result page, styling | 3 days | Done |
| Sprint 3 | Deployment | Dockerfile, IBM Cloud deployment notes, environment-based port config | 1 day | Done |
| Sprint 4 | Documentation & Testing | Test cases, README, GitHub repo structure, project report | 2 days | Done |

## Activity List by Epic

### Epic 1 — Data Collection
- Identify and download rainfall/flood dataset
- Validate column completeness and data types
- Document dataset schema in README

### Epic 2 — Visualizing and Analysing the Data
- Plot target class distribution (flood vs no-flood)
- Plot correlation heatmap across all numeric features
- Plot annual rainfall distribution
- Plot seasonal rainfall averages
- Plot temperature/humidity/cloud-cover distributions
- Plot annual rainfall vs. flood occurrence (boxplot)

### Epic 3 — Data Pre-processing
- Drop empty rows/columns
- Fill missing numeric values with median
- Remove duplicate rows
- Encode the flood target to 0/1
- Select and validate feature columns
- Train/test split (80/20, stratified)
- Fit and persist `StandardScaler`

### Epic 4 — Model Building
- Implement Decision Tree classifier
- Implement Random Forest classifier
- Implement KNN classifier
- Implement XGBoost classifier
- Evaluate all models: accuracy, precision, recall, F1, confusion matrix
- Select best model by test accuracy (tie-break: F1)
- Persist best model + metrics summary

### Epic 5 — Application Building
- Build Flask routes (`/`, `/predict`)
- Build dynamic input form (auto-generated from feature columns)
- Build result page with prediction + probability
- Style the UI (CSS)
- Add error handling for missing model / bad input
- Write Dockerfile for IBM Cloud deployment
