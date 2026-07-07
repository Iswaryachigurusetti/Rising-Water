# Rising Waters — ML-Powered Flood Prediction System

End-to-end flood prediction system built on historical rainfall data, using
Decision Tree, Random Forest, KNN, and XGBoost classifiers, served through a
Flask web application.

## 1. Project Structure

```
flood_prediction/
├── data/
│   ├── flood_dataset.xlsx              <- labeled training data (used by the models)
│   └── rainfall_india_1901_2015.xlsx   <- raw historical archive (reference / Epic 1)
├── src/
│   ├── config.py                   <- column names / paths (edit if your CSV differs)
│   ├── data_preprocessing.py       <- cleaning, feature engineering, encoding
│   ├── eda.py                      <- Epic 2: visualizations
│   └── train_models.py             <- Epic 4: trains all 4 models, saves the best
├── models/                         <- trained model + scaler + encoder land here
├── app/
│   ├── app.py                      <- Flask app (Epic 5)
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   └── static/
│       └── style.css
├── notebooks/
│   └── flood_prediction_walkthrough.py   <- full pipeline as one runnable script
├── requirements.txt
└── README.md
```

This maps directly onto your Epics:

- **Epic 1 – Data Collection**: `data/rainfall_dataset.csv` (you download from Kaggle)
- **Epic 2 – Visualizing and Analysing the Data**: `src/eda.py`
- **Epic 3 – Data Pre-processing**: `src/data_preprocessing.py`
- **Epic 4 – Model Building**: `src/train_models.py`
- **Epic 5 – Application Building**: `app/app.py` + `app/templates/`

## 2. The dataset

Your Kaggle archive contains two files, already placed in `data/`:

- **`flood_dataset.xlsx`** (115 rows) — the labeled training set actually
  used to build the models. Columns:
  `Temp, Humidity, Cloud Cover, ANNUAL, Jan-Feb, Mar-May, Jun-Sep, Oct-Dec,
  avgjune, sub, flood` — where `flood` (0/1) is the prediction target.
- **`rainfall_india_1901_2015.xlsx`** (4,116 rows) — the raw historical
  rainfall archive (Epic 1 source data, India 1901–2015 by state/subdivision).
  It's kept for reference/Epic-1 documentation but isn't used directly in
  training since it has no flood label.

`src/config.py` is already configured for `flood_dataset.xlsx`'s exact
schema (`DATA_PATH`, `TARGET_COLUMN = "flood"`, `FEATURE_COLUMNS`). If you
swap in a different or updated dataset later, that's the one file you need
to edit — everything downstream reads from it. The preprocessing script also
auto-detects common alternate target-column spellings and will print a
warning telling you exactly which columns it found vs. expected.

## 3. Setup

```bash
cd flood_prediction
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 4. Run the pipeline

### Step 1 — EDA (optional, generates plots into `notebooks/plots/`)
```bash
python src/eda.py
```

### Step 2 — Preprocess + Train + Evaluate all 4 models
```bash
python src/train_models.py
```
This will:
- Clean and encode the data
- Split into train/test
- Train Decision Tree, Random Forest, KNN, and XGBoost
- Print accuracy / precision / recall / F1 / confusion matrix for each
- Save the **best-performing model** (by test accuracy) to `models/best_model.pkl`,
  along with `models/scaler.pkl` and `models/feature_columns.pkl`

### Step 3 — Run the web app
```bash
cd app
python app.py
```
Then open **http://127.0.0.1:5000** in your browser.

## 5. Deploying to IBM Cloud

`app/app.py` reads the port from the `PORT` environment variable
(`os.environ.get("PORT", 5000)`), which is the convention IBM Cloud
(and most PaaS providers, e.g. Cloud Foundry / Code Engine) use. To deploy:

1. Push this repo to GitHub.
2. Create an IBM Cloud **Code Engine** application (or Cloud Foundry app)
   pointing at the repo, build type "Dockerfile" or "buildpack: Python".
3. A minimal `Dockerfile` is included below (Section 6) if you want
   container-based deployment.
4. Make sure `models/best_model.pkl`, `scaler.pkl`, and `feature_columns.pkl`
   are committed (or regenerated at build time via `train_models.py`).

## 6. Dockerfile (optional, for IBM Cloud Code Engine)

Already included as `Dockerfile` in the project root.

## 7. Notes

- All four models are trained and compared automatically; whichever scores
  highest on the held-out test set is the one saved and served by the app.
  On this 115-row dataset, Decision Tree and Random Forest both hit ~95-96%
  test accuracy; results shift a little run to run given how small the
  dataset is, so don't be surprised if a different model wins on your machine.
- The dataset is small (115 rows) and imbalanced (~14% flood-positive), so
  treat accuracy alone with caution — the script also prints precision,
  recall, F1, and a confusion matrix for each model so you can judge how
  well it actually catches flood events, not just overall correctness.
- Input form fields on the web app are generated dynamically from
  `models/feature_columns.pkl`, so if you change `FEATURE_COLUMNS` in
  `config.py`, the UI updates automatically — no template editing needed.
