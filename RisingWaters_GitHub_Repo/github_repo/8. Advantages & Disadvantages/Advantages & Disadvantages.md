# 8. Advantages & Disadvantages

## 8.1 Advantages

- **Early warning lead time**: Provides a data-driven flood-risk estimate
  ahead of visible flooding, giving authorities more time to issue
  evacuation advisories.
- **Multi-model transparency**: Rather than committing to one algorithm
  blindly, the system trains and compares four different classifiers and
  documents why the winning one was chosen.
- **Low barrier to use**: A simple web form means field staff and
  coordinators don't need programming or data-science skills to get a
  prediction.
- **Configurable and maintainable**: All dataset-specific settings live in
  one `config.py` file, so the system can be adapted to new or updated
  rainfall datasets without touching the model training or app logic.
- **Cloud-deployable**: Comes with a working Dockerfile and environment-based
  port configuration, ready for IBM Cloud or any container-based host.
- **Fast inference**: Classical ML models (not deep learning) mean
  predictions return in milliseconds, suitable for real-time use during a
  monsoon monitoring session.

## 8.2 Disadvantages / Limitations

- **Small training dataset**: Only 115 labeled rows are available, which
  limits how well the model generalizes to conditions outside its training
  distribution (e.g., extreme or unprecedented weather events).
- **Class imbalance**: Flood-positive examples make up roughly 14% of the
  data, so the model may under-predict rare but severe flood events unless
  carefully monitored (precision/recall, not just accuracy, should be
  checked before operational reliance).
- **No real-time data feed**: The current system requires manual entry of
  readings rather than pulling live data from weather stations or
  satellites.
- **No geographic/spatial modeling**: Predictions are per-input-vector, not
  tied to GPS coordinates or region-specific historical patterns beyond
  what's implicitly captured in the training data.
- **No time-series memory**: Each prediction is independent; the model
  doesn't track rainfall trends building up over multiple days/weeks
  (e.g., soil saturation effects), which are known contributors to flooding.
- **Single-point-in-time input**: Doesn't account for upstream river
  levels, dam release schedules, or drainage infrastructure — all of which
  materially affect real-world flood risk.
