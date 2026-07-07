# 3. Data Flow Diagram & Solution Architecture

## 3.1 High-Level Architecture

```
                    ┌────────────────────────┐
                    │   Historical Dataset    │
                    │  (flood_dataset.xlsx)   │
                    └───────────┬────────────┘
                                │
                                ▼
                    ┌────────────────────────┐
                    │  Data Pre-processing    │
                    │  (clean, encode, scale) │
                    │  src/data_preprocessing │
                    └───────────┬────────────┘
                                │
                 ┌──────────────┼──────────────┐
                 ▼              ▼              ▼
          ┌───────────┐ ┌───────────┐  ┌──────────────┐
          │  EDA /     │ │  Train /  │  │   Scaler +   │
          │  src/eda.py│ │ Test Split│  │ Feature List │
          └───────────┘ └─────┬─────┘  │  (persisted) │
                               │        └──────────────┘
                               ▼
                ┌──────────────────────────────┐
                │        Model Training          │
                │  Decision Tree | Random Forest │
                │  KNN | XGBoost                 │
                │  src/train_models.py           │
                └───────────────┬────────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │   Best Model Selection         │
                │   (highest test accuracy)      │
                │   models/best_model.pkl        │
                └───────────────┬────────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │        Flask Web App           │
                │        app/app.py              │
                │  - GET /   → input form         │
                │  - POST /predict → prediction  │
                └───────────────┬────────────────┘
                                │
                                ▼
                ┌──────────────────────────────┐
                │   End User (Browser)           │
                │  Meteorologist / Coordinator / │
                │  Government Analyst            │
                └──────────────────────────────┘
```

## 3.2 Data Flow Diagram (Level 0)

```
[User] --(rainfall/temp/humidity readings)--> [Flask App]
[Flask App] --(scaled feature vector)--> [Trained Model]
[Trained Model] --(prediction + probability)--> [Flask App]
[Flask App] --(rendered result page)--> [User]
```

## 3.3 Data Flow Diagram (Level 1 — Training Pipeline)

```
[Raw Dataset (xlsx)]
        │
        ▼
[Load & Clean] --(drop dupes, fill NA with median)--> [Cleaned DataFrame]
        │
        ▼
[Encode Target] --(flood: 0/1)--> [Labeled DataFrame]
        │
        ▼
[Train/Test Split] --(80/20 stratified)--> [Train Set] + [Test Set]
        │
        ▼
[StandardScaler.fit_transform] --(train)--> [Scaled Train Features]
[StandardScaler.transform]     --(test)-->  [Scaled Test Features]
        │
        ▼
[Train 4 Classifiers] --> [Evaluate on Test Set] --> [Pick Best by Accuracy/F1]
        │
        ▼
[Persist: best_model.pkl, scaler.pkl, feature_columns.pkl, metrics.json]
```

## 3.4 Technology Stack

| Layer | Technology |
|---|---|
| Data handling | pandas, NumPy, openpyxl |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn (Decision Tree, Random Forest, KNN, StandardScaler), XGBoost |
| Web Framework | Flask |
| Frontend | HTML, CSS (Jinja2 templates) |
| Model Persistence | joblib |
| Containerization | Docker |
| Target Cloud | IBM Cloud (Code Engine / Cloud Foundry) |
