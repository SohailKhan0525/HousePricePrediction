# 🏠 House Price Prediction

A Streamlit-based machine learning project that predicts house prices from property details using a trained regression model and saved preprocessing artifacts.

---

## 🎯 Project Goal

The main objective of this project is to take user input from a clean UI, transform it into the exact feature structure used during training, and return a reliable predicted house price.

This project is designed as a practical, end-to-end ML learning build: from feature understanding to inference-time consistency.

---

## ✅ Project Files

- **app.py**
	- Streamlit app for collecting user inputs and running predictions
	- Includes validation, feature creation, encoding, alignment, and prediction
- **best_model.pkl**
	- Final trained regression model used for inference
- **columns.pkl**
	- Saved list of training feature columns used to align prediction-time input
- **unique_categories.pkl**
	- Saved category values used to populate Streamlit dropdowns
- **housepriceprediction.ipynb**
	- Notebook for experimentation and model-building workflow
- **requirements.txt**
	- Python dependencies for running the app

---

## ✨ Features Implemented

- Clean Streamlit interface for property data entry
- Categorical value selection with controlled dropdowns
- Input validation (`Current Floor <= Total Floor`)
- Derived features for better signal capture:
	- `Floor Ratio`
	- `Is top floor`
- One-hot encoding with `pd.get_dummies`
- Strict feature alignment with saved training columns via `reindex`
- Fast artifact loading using `@st.cache_resource`
- Predicted price output with formatted currency display

---

## 🧠 Input Features Used by Model

### Numerical Features
- Carpet Area
- Bathroom
- Balcony
- Current Floor
- Total Floor

### Categorical Features
- location
- Transaction
- Furnishing
- facing
- overlooking
- Car Parking
- Ownership

### Engineered Features
- Floor Ratio (`Current Floor / Total Floor`)
- Is top floor (`1` if current floor equals total floor, otherwise `0`)

---

## ▶️ How to Run

1. Open terminal in this folder.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the Streamlit app:

```bash
streamlit run app.py
```

4. Fill in the property details and click **Predict Price 💰**.

---

## 📚 What I Learned (Detailed)

This project gave me practical experience in building an ML system that works beyond a notebook. Here are the key lessons I learned and expanded:

### 1) End-to-End ML Thinking (Not Just Model Training)

I learned that a good ML project is not only about accuracy during training. It must also run reliably when a real user gives new input. This project taught me to think in complete stages:

- collecting usable inputs,
- validating them,
- transforming them exactly like training data,
- and then predicting consistently.

### 2) Importance of Inference Consistency

One of the most important lessons was schema consistency between training and prediction.

If feature columns during prediction do not match the model’s expected columns, predictions become invalid or fail. I learned to solve this by:

- saving the original training columns (`columns.pkl`),
- encoding incoming input with `pd.get_dummies`,
- and reindexing to the training schema with missing columns filled by `0`.

This made the app robust and production-minded.

### 3) Feature Engineering Improves Practical Performance

I learned to move beyond raw inputs and create features that represent domain behavior:

- `Floor Ratio` captures relative vertical position,
- `Is top floor` captures an important binary characteristic.

This improved my understanding of how domain-inspired features can add meaningful predictive signal.

### 4) Data Validation is a Core ML Skill

I learned that model quality is directly connected to input quality. Even a trained model can produce poor results with invalid input.

By enforcing checks like `Current Floor cannot be greater than Total Floor`, I learned how validation protects both user trust and model behavior.

### 5) Working with Categorical Data in Real Apps

I learned practical handling of categorical variables in two parts:

- preserving allowed categories in `unique_categories.pkl`,
- using those categories to drive dropdown choices in Streamlit.

This avoids inconsistent or unexpected user inputs and creates a cleaner UI/ML interface.

### 6) Artifact Management and Reproducibility

I learned to treat artifacts as first-class parts of the project:

- model file,
- column schema,
- and category mappings.

Saving and versioning these artifacts means the project can be rerun and shared without retraining every time.

### 7) Building User-Facing ML with Streamlit

I learned how to convert backend ML logic into an interactive app:

- collecting structured inputs,
- running prediction on button click,
- and returning clear output.

I also learned to improve app performance by caching expensive loads with `@st.cache_resource`.

### 8) Debugging DataFrame Pipeline Mistakes

A key debugging lesson was making sure the exact encoded DataFrame is passed to the model.

Small mistakes in variable usage (for example, aligning one DataFrame but predicting with another) can silently break results. This project improved my attention to detail in ML data pipelines.

### 9) Better Project Structuring for Portfolio Readiness

I learned to organize files so others can understand and run the project quickly:

- app code in `app.py`,
- dependencies in `requirements.txt`,
- model artifacts in `.pkl` files,
- and documentation in `README.md`.

This made the project cleaner and more professional for sharing on GitHub.

### 10) Communication and Documentation

I learned that writing a clear README is part of engineering work. Documentation helps explain:

- what the project does,
- what inputs it expects,
- how to run it,
- and what technical decisions were taken.

This improves collaboration and makes the project easier to maintain in the future.

---

## 🚀 Future Improvements

- Add model training script with reproducible pipeline steps
- Add evaluation report section with MAE / RMSE / R² from final model
- Add automated tests for input validation and schema alignment
- Add Docker support for one-command deployment

---

## 📌 Note

This is a learning and portfolio project. Predicted values are for demonstration and may not represent live market pricing.

---

## 📄 License

Personal learning project. You may reuse with credit.
