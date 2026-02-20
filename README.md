# 🏠 House Price Prediction

Machine learning project to estimate house prices using a trained regression model and engineered features.

---

## ✅ What's Included

- **app.py** – Prediction pipeline with input validation, one-hot encoding, and artifact loading.
- **best_model.pkl** – Trained regression model serialized with joblib.
- **columns.pkl** – Training column order for one-hot encoded features, used to align inference inputs.
- **unique_categories.pkl** – Allowed category values for each categorical feature.
- **requirements.txt** – Python dependencies.

---

## ✨ Features

- Input validation (e.g., floor constraints)
- One-hot encoding aligned to training columns to prevent feature mismatch
- Derived features: Floor Ratio, Is Top Floor
- Serialized model and column artifacts for reproducible inference

---

## ▶️ Run Locally

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the prediction script:

```bash
python app.py
```

---

## 🧠 Model Inputs

The model uses these inputs:

- **Numerical:** Carpet Area, Bathrooms, Balcony, Current Floor, Total Floor
- **Categorical:** Location, Transaction, Furnishing, Facing, Overlooking, Car Parking, Ownership
- **Derived:** Floor Ratio, Is Top Floor

---

## 📌 Notes

- Data shown is illustrative; this is a portfolio/learning project.
- Retrain the model and regenerate `unique_categories.pkl` and `columns.pkl` if the dataset changes.

---

## 📚 What I Learned

- **Data preprocessing:** Handling missing values, type casting, and cleaning raw housing data before modeling.
- **Exploratory data analysis (EDA):** Identifying distributions, correlations, and outliers that informed feature decisions.
- **Feature engineering:** Creating derived features (Floor Ratio, Is Top Floor) to capture domain-relevant signal.
- **Categorical encoding alignment:** Using `pd.get_dummies` and `reindex` with saved column order to ensure inference inputs match training schema.
- **Artifact serialization:** Saving and loading model, column list, and category mappings with joblib for reproducible predictions.
- **Model evaluation:** Comparing regression metrics (MAE, RMSE, R²) across models to select the best performer.
- **Reproducibility:** Persisting all preprocessing artifacts alongside the model so predictions can be reproduced without retraining.

---

## 📄 License

Personal project for learning and portfolio use. Provide credit if reused.
