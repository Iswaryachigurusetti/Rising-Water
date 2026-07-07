# Rising Waters — ML-Powered Flood Prediction System

Floods are among the most devastating natural disasters, claiming thousands
of lives and displacing millions every year. This project builds a
machine-learning flood prediction system trained on historical rainfall and
meteorological data, comparing Decision Tree, Random Forest, KNN, and
XGBoost classifiers, and serving the best-performing model through a Flask
web application for use by meteorologists and disaster management teams.

## Repository Structure

| Folder | Contents |
|---|---|
| `1. Brainstorming & Ideation` | Problem statement, brainstorming, idea prioritization |
| `2. Requirement Analysis` | Customer journey map, functional & non-functional requirements |
| `3. Project Design` | Data flow diagram, solution architecture, user stories |
| `4. Project Planning` | Milestones, activity list, sprint delivery plan |
| `5. Project Development` | **Full working source code** — data, models, Flask app, README |
| `6. Testing` | Test cases across pre-processing, model training, and the web app |
| `7. Results` | Model performance comparison, EDA outputs, scenario validation |
| `8. Advantages & Disadvantages` | Honest assessment of strengths and current limitations |
| `9. Conclusion` | Project summary |
| `10. Future Scope` | Planned improvements and extensions |
| `11. Appendix` | Source code pointer, GitHub/demo links, dataset source, team |

## Quick Start

```bash
cd "5. Project Development"
pip install -r requirements.txt
python src/train_models.py      # trains & evaluates all 4 models, saves the best
cd app && python app.py         # open http://127.0.0.1:5000
```

Full setup, dataset details, and IBM Cloud deployment instructions are in
`5. Project Development/README.md`.

## Team

| Name | Role |
|---|---|
| Pachigolla Rupa Sri Malleswari | Team Lead |
| Chigurusetti Iswarya | Member |
| Penneru Sushmika | Member |
| Praneetha Oruganti | Member |
| Uma Lingam | Member |
