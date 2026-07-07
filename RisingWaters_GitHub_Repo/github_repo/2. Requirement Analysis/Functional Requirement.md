# 2. Functional Requirement

| FR No. | Functional Requirement | Sub Requirement |
|---|---|---|
| FR-1 | Data Collection | System shall allow ingestion of historical rainfall and meteorological data (temperature, humidity, cloud cover, seasonal rainfall) from CSV/Excel sources |
| FR-2 | Data Pre-processing | System shall clean missing values, remove duplicates, encode the flood label, and scale numeric features before training |
| FR-3 | Data Visualization | System shall generate exploratory plots (class distribution, correlation heatmap, feature distributions, rainfall-vs-flood boxplots) |
| FR-4 | Model Training | System shall train Decision Tree, Random Forest, KNN, and XGBoost classifiers on the pre-processed dataset |
| FR-5 | Model Evaluation | System shall compute accuracy, precision, recall, F1-score, and confusion matrix for every trained model |
| FR-6 | Model Selection | System shall automatically select and persist the best-performing model based on test-set accuracy (tie-broken by F1) |
| FR-7 | Prediction Input | System shall provide a web form where a user can enter meteorological readings |
| FR-8 | Prediction Output | System shall return a flood-risk classification ("Flood Likely" / "Flood Unlikely") with an estimated probability |
| FR-9 | Error Handling | System shall handle invalid/missing form input and missing model artifacts gracefully with a clear on-screen message |
| FR-10 | Deployment | System shall be deployable as a containerized (Docker) application suitable for IBM Cloud hosting |

# Non-Functional Requirements

| NFR No. | Non-Functional Requirement | Description |
|---|---|---|
| NFR-1 | Usability | The web interface must be usable by non-technical disaster-management staff with no ML background |
| NFR-2 | Performance | A single prediction request should return a result in under 1 second on standard hardware |
| NFR-3 | Reliability | The system should not crash on malformed input; it should validate and respond with a clear error instead |
| NFR-4 | Maintainability | Feature columns, target column, and model hyperparameters must be configurable in a single file (`config.py`) without touching other modules |
| NFR-5 | Scalability | The Flask app must run behind a standard WSGI/production server and be containerizable for horizontal scaling on IBM Cloud |
| NFR-6 | Portability | The system must run on Windows, Linux, and macOS with Python 3.8+ |
| NFR-7 | Security | The app must not expose the raw dataset or model internals through any public endpoint beyond the prediction form |
