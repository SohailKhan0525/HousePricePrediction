# 🏠 House Price Prediction

This project is an end-to-end machine learning workflow for predicting house prices, rebuilt from the updated notebook `housepricepred.ipynb` and deployed with Streamlit.

---

## 🎯 Project Summary

I worked on the complete ML cycle:

1. Load and inspect raw housing data
2. Clean missing/invalid values
3. Build features from text-heavy columns
4. Normalize units and value scales
5. Train and compare multiple regressors
6. Save deployable model artifacts

The prediction target in this notebook is **`Price(in lakhs)`**.

---

## 🧪 What I Did in `housepricepred.ipynb`

### 1) Data loading and exploration
- Imported `numpy`, `pandas`, `matplotlib`, `seaborn`
- Loaded `house_prices.csv`
- Checked data quality using `info()`, `describe()`, `isnull().sum()`, and `shape`

### 2) Missing value handling and column cleanup
- Removed high-missing / low-use columns:
	- `Plot Area`, `Dimensions`, `Super Area`, `Car Parking`, `Society`
- Filled key missing values with statistical imputations:
	- `Ownership` with mode
	- `Bathroom`, `Balcony` with median
	- `Current Floor` and `Total Floor` with median

### 3) Data type cleaning and standardization
- Converted noisy bathroom and balcony values (like `> 10`) into numeric values
- Converted these columns to integers
- Processed floor strings into structured numeric features:
	- `Total Floor`
	- `Current Floor`

### 4) Feature engineering
- Extracted numeric carpet area from text and standardized into `Carpet Area(SQFT)`
	- handled units such as sqft, sqm, and sqyard
- Derived price target from amount text:
	- parsed number into `amount_value`
	- converted crore/lakh strings into unified `Price(in lakhs)`
- Extracted `BHK` count from `Title`

### 5) Outlier filtering and dataset constraints
- Kept realistic carpet area range: `300` to `6000` sqft
- Kept realistic price range: `7` to `1200` lakhs
- Removed temporary/raw columns after conversion:
	- `Title`, `Amount(in rupees)`, `amount_value`, raw carpet intermediates

### 6) Model training and comparison
- Prepared `X` and `y` where target = `Price(in lakhs)`
- Applied one-hot encoding with `pd.get_dummies(drop_first=True)`
- Train/test split: `test_size=0.2`, `random_state=42`
- Trained and compared:
	- `RandomForestRegressor`
	- `GradientBoostingRegressor`
	- `DecisionTreeRegressor`
- Evaluated each using:
	- `R²`
	- `MAE`
	- `RMSE`
- Selected best model based on highest `R²`

### 7) Model artifact export
- Saved best model to `best_model.pkl`
- Saved encoded feature columns to `columns.pkl`

---

## 📚 What I Learned (Expanded)

### 1) Most ML time is spent before modeling
I learned that preprocessing is the core of real projects. The raw data had mixed formats, missing values, and text-heavy fields. Cleaning them correctly was more important than quickly fitting a model.

### 2) Text-to-numeric conversion is a key practical skill
Fields like `Carpet Area`, `Floor`, and `Amount(in rupees)` are not directly model-ready. I learned how to parse and transform these into consistent numeric variables.

### 3) Unit normalization matters a lot
Area values came in different units (`sqft`, `sqm`, `sqyard`). Converting all of them into one unit (`SQFT`) improved consistency and reduced hidden noise.

### 4) Target engineering affects model stability
Converting `Amount(in rupees)` into a clean numeric target (`Price(in lakhs)`) taught me how important a stable target representation is for regression performance.

### 5) Data constraints improve robustness
Filtering unrealistic area and price ranges helped remove extreme outliers and made the model more stable on practical values.

### 6) Multiple metrics give better judgment
I learned not to depend on only one metric. Reading `R²`, `MAE`, and `RMSE` together gave a fuller view of both fit quality and prediction error scale.

### 7) Comparing models is better than guessing
Trying Random Forest, Gradient Boosting, and Decision Tree in the same setup helped me choose the best model objectively instead of by assumption.

### 8) Categorical encoding must be deployment-ready
I learned that saving encoded column order (`columns.pkl`) is essential. Without the exact feature schema, app-time predictions can break or become inconsistent.

### 9) Dropping temporary columns prevents confusion
During feature engineering I created helper columns (like parsed area and amount values). Removing these after use keeps the final training dataset clean and reproducible.

### 10) End-to-end delivery is the real milestone
The biggest learning is that successful ML is not only training a model. It is building a full pipeline that can be understood, reused, and connected to a real app.

---

## 📂 Current Files

- `housepricepred.ipynb` → Updated training and preprocessing notebook
- `app.py` → Streamlit app
- `best_model.pkl` → Best trained model
- `columns.pkl` → Encoded training feature schema
- `requirements.txt` → Project dependencies

---

## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Note

This is a learning/portfolio project. Predictions are for educational and demonstration use.
