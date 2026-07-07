# 9. Conclusion

Rising Waters demonstrates that a lightweight, classical machine-learning
pipeline can meaningfully support flood early-warning efforts without
requiring large-scale infrastructure or deep learning. By training and
comparing Decision Tree, Random Forest, KNN, and XGBoost classifiers on
historical rainfall, temperature, humidity, and cloud-cover data, the system
automatically identifies and deploys the best-performing model — achieving
95.65% test accuracy with the selected model on the available dataset.

The accompanying Flask web application closes the gap between a trained
model and a usable tool: meteorologists, disaster relief coordinators, and
government analysts can get an instant, interpretable flood-risk prediction
through a simple form, without needing to interact with code or notebooks
directly. The architecture is deliberately config-driven, so the same
codebase can be pointed at an updated or expanded dataset in the future with
minimal changes.

While the current system is constrained by a small, imbalanced training set
and the absence of real-time or spatial data, it establishes a solid,
well-tested foundation — validated end-to-end from data pre-processing
through model training to live web prediction — that can be extended as
richer data sources become available (see Future Scope).
