# 2. Customer Journey Map

## Persona: Disaster Relief Coordinator (Monsoon Season)

| Stage | Awareness | Consideration | Decision / Use | Action | Retention |
|---|---|---|---|---|---|
| **Doing** | Hears seasonal flood warnings on news; knows monsoon risk is rising | Looks for a fast way to assess regional flood risk without waiting on manual reports | Opens the Rising Waters web app, enters current rainfall/humidity/temperature readings | Receives an instant flood-risk prediction with probability | Uses the tool daily during monsoon season to track multiple regions |
| **Thinking** | "I need better lead time than what we currently get" | "Can I trust a model I don't fully understand?" | "This is faster than waiting for a manual report" | "This helps me decide where to send resources first" | "I'd like more regions and historical trend tracking" |
| **Feeling** | Anxious, time-pressured | Cautiously optimistic | Relieved to have a data point quickly | Confident, in control | Trusting, wants more features |
| **Pain Points** | No unified early-warning tool | Uncertainty about model reliability | Manual data entry per region is repetitive | No batch/multi-region view yet | No historical dashboard yet |
| **Opportunities** | Market the tool through disaster management agencies | Show model accuracy/metrics transparently in the UI | Add CSV bulk upload for multiple regions | Add a "risk level" color indicator | Add historical logging and trend charts (Future Scope) |

## Persona: Meteorologist (Early Warning)

| Stage | Awareness | Consideration | Decision / Use | Action | Retention |
|---|---|---|---|---|---|
| **Doing** | Monitors daily weather station readings | Compares readings against known flood thresholds | Enters readings into Rising Waters | Gets prediction, cross-checks with own judgement | Uses it as a standard part of daily monitoring routine |
| **Feeling** | Vigilant | Analytical | Focused | Validated or alerted | Habitual trust, wants integration with existing tools |
| **Pain Points** | Scattered data sources | No single tool combines rainfall + cloud + temp signals | Manual entry is slower than an automated feed | No historical comparison against past flood years | No API for integration into existing SCADA/weather systems |
| **Opportunities** | Position as a complementary decision-support tool, not a replacement for expert judgement | Bundle feature explanations (which inputs drove the prediction) | Auto-fill from a weather API (Future Scope) | Add a downloadable prediction log | Build an API endpoint (Future Scope) |
