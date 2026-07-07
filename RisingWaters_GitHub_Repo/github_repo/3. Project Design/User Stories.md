# 3. User Stories

| User Type | User Story No. | I want to... | So that... | Acceptance Criteria | Priority |
|---|---|---|---|---|---|
| Meteorologist | USN-1 | enter current rainfall, temperature, humidity, and cloud cover readings | I can check flood risk for my district | Form accepts numeric input for all required fields and returns a prediction | High |
| Meteorologist | USN-2 | see the probability of flooding, not just yes/no | I can judge how confident the model is | Result page displays a percentage probability alongside the classification | High |
| Disaster Relief Coordinator | USN-3 | run predictions for multiple regions in sequence | I can prioritize where to send resources first | Form can be resubmitted quickly with a "Run Another Prediction" link | High |
| Government Analyst | USN-4 | see accuracy, precision, recall, and F1 for each trained model | I can validate the system before operational sign-off | `train_models.py` prints and saves a full metrics report for all 4 models | High |
| Government Analyst | USN-5 | know which model was ultimately selected and why | I can trust the deployed model's decision-making | `metrics.json` records the best model name alongside all models' scores | Medium |
| Developer/Maintainer | USN-6 | change the dataset's column names without editing multiple files | I can adapt the system to a new dataset quickly | All column/target configuration lives in a single `config.py` file | Medium |
| Developer/Maintainer | USN-7 | deploy the app to IBM Cloud | disaster management teams can access it from anywhere | A working `Dockerfile` and port-from-env-variable setup is provided | Medium |
| End User | USN-8 | get a clear error message if something goes wrong | I'm not left staring at a blank/broken page | Flask app catches missing-model and bad-input errors and shows a readable message | Medium |
