# 1. Brainstorming & Idea Prioritization

## Project: Rising Waters — ML-Powered Flood Prediction System

### Team
| Name | Role |
|---|---|
| Pachigolla Rupa Sri Malleswari | Team Lead |
| Chigurusetti Iswarya | Member |
| Penneru Sushmika | Member |
| Praneetha Oruganti | Member |
| Uma Lingam | Member |

---

## 1.1 Problem Statement

Floods are among the most devastating natural disasters, claiming thousands
of lives and displacing millions every year. Despite their recurring nature,
the lack of timely and accurate early-warning systems continues to amplify
their destructive impact. Conventional forecasting methods often fall short
in predicting floods at the right time, leaving authorities and communities
with insufficient opportunity to respond.

## 1.2 Brainstorming Session — Raw Ideas

During ideation, the team explored multiple approaches to tackling the
flood-forecasting problem:

- Build a rule-based threshold system (e.g., "if rainfall > X mm, flag flood
  risk") — rejected as too rigid and unable to capture interactions between
  temperature, humidity, cloud cover, and seasonal rainfall patterns.
- Use a single deep learning model (LSTM on time-series rainfall) — set
  aside for this phase due to limited historical time-series granularity in
  the available dataset; flagged as a strong candidate for Future Scope.
- **Selected approach:** Train and compare multiple classical ML
  classifiers (Decision Tree, Random Forest, KNN, XGBoost) on historical
  meteorological data, select the best performer, and expose it through a
  simple web interface so non-technical disaster management staff can use it
  without needing to run code.

## 1.3 Idea Prioritization

| Idea | Impact | Feasibility | Priority |
|---|---|---|---|
| Multi-model ML classification (chosen) | High | High | 1 |
| Web app for authorities/coordinators | High | High | 1 |
| Cloud deployment (IBM Cloud) | Medium | Medium | 2 |
| Real-time satellite data integration | High | Low (data access) | 3 (future scope) |
| SMS/alert-based evacuation notifications | High | Medium | 3 (future scope) |

## 1.4 Why This Solution

- **Accessible**: A Flask web form means field staff don't need to run
  notebooks or scripts — they just enter readings and get a risk prediction.
- **Transparent**: Multiple models are trained and compared side-by-side
  (accuracy, precision, recall, F1), so the team can justify which model is
  deployed and why, rather than trusting a black box.
- **Extensible**: The architecture (config-driven feature columns, swappable
  model) allows the dataset or feature set to be updated later — e.g. adding
  real-time satellite rainfall feeds — without rewriting the app.

## 1.5 Target Users & Scenarios

1. **Meteorologist** — enters current rainfall/cloud readings for a
   flood-prone district to issue evacuation advisories in advance.
2. **Disaster relief coordinator** — monitors multiple regions during
   monsoon season to prioritize resource deployment.
3. **Government analyst** — validates model accuracy against historical
   flood records for operational sign-off.
