# 10. Future Scope

- **Larger, richer datasets**: Incorporate multi-decade, multi-region
  datasets (e.g., the included `rainfall_india_1901_2015.xlsx` archive) with
  proper flood labels to improve generalization and reduce reliance on a
  115-row training set.
- **Real-time data integration**: Connect to live weather APIs or IMD
  (India Meteorological Department) feeds so readings are pulled
  automatically instead of manually entered.
- **Time-series / sequence modeling**: Introduce LSTM or other
  sequence-aware models to capture multi-day rainfall accumulation and
  soil-saturation effects, which are known flood drivers that a single
  snapshot of readings can't capture.
- **Geospatial modeling**: Tie predictions to GPS coordinates or watershed
  boundaries, and layer results onto a map for visual risk assessment
  across a region rather than one input at a time.
- **River and dam data integration**: Incorporate upstream river gauge
  levels and dam release schedules, which materially affect downstream
  flood risk beyond rainfall alone.
- **Alerting and notifications**: Add SMS/email/push alerting so that when a
  prediction crosses a risk threshold, relevant authorities are notified
  automatically rather than needing to check the app manually.
- **Bulk/batch predictions**: Support CSV upload for scoring multiple
  regions or time periods in a single request, useful for the Disaster
  Response scenario.
- **Model monitoring & retraining pipeline**: Automate periodic retraining
  as new labeled flood events become available, with drift detection to
  flag when the deployed model's performance degrades.
- **API endpoint**: Expose a REST API (in addition to the web form) so the
  prediction service can be integrated into other disaster-management
  software or dashboards.
- **IBM Cloud production hardening**: Move beyond the Docker starting point
  to a full CI/CD pipeline on IBM Cloud Code Engine with autoscaling,
  logging, and monitoring.
