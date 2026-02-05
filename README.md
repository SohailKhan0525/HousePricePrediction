# 🏠 House Price Prediction (Streamlit App)

Interactive machine learning app to estimate house prices using a trained model and engineered features.

🔗 **Live App:**  
[House Price Prediction App](https://housepriceprediction-rqo8ykwgldxbpemwl6kvok.streamlit.app/)

---

## ✅ What’s Included (File Analysis)

- **app.py** – Streamlit UI and prediction pipeline with input validation, one-hot encoding, and cached artifact loading.
- **best_model.pkl** – Trained regression model.
- **columns.pkl** – Training column order for one-hot encoded features.
- **unique_categories.pkl** – Allowed categories for dropdown inputs.
- **requirements.txt** – Python dependencies.

---

## ✨ Features

- Clean Streamlit UI with form inputs
- Validation for floor constraints
- One-hot encoding aligned to training columns
- Cached model loading for faster startup
- Live deployment on Streamlit Cloud

---

## ▶️ Run Locally

1. Install dependencies:

	```bash
	pip install -r requirements.txt
	```

2. Start the app:

	```bash
	streamlit run app.py
	```

---

## 🧠 Model Inputs

The app uses these inputs:

- **Numerical:** Carpet Area, Bathrooms, Balcony, Current Floor, Total Floor
- **Categorical:** Location, Transaction, Furnishing, Facing, Overlooking, Car Parking, Ownership
- **Derived:** Floor Ratio, Is top floor

---

## 📌 Notes

- This is a demo app; data shown is illustrative.
- Update `unique_categories.pkl` and `columns.pkl` if you retrain the model.

---

## 📚 What I Learned

- Data cleaning and preprocessing
- Exploratory data analysis (EDA)
- Feature engineering and outlier handling
- Model tuning and evaluation

---

## 📄 License

Personal project for learning and portfolio use. Provide credit if reused.
