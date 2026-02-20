# 🏠 House Price Prediction

This project predicts house prices using a machine learning pipeline developed in `housepriceprediction.ipynb` and served through a Streamlit app.

---

## 🎯 What I Built

I built an end-to-end regression workflow:

1. Load and inspect the raw housing dataset
2. Clean missing values and drop low-value columns
3. Engineer useful numerical features from text-based fields
4. Remove outliers and keep a realistic value range
5. Train multiple regression models
6. Compare metrics and pick the best model
7. Save model + metadata artifacts for app inference

---

## 🧪 Notebook Workflow (Based on `housepriceprediction.ipynb`)

### 1) Data loading and initial inspection
- Imported `numpy`, `pandas`, `seaborn`, `matplotlib`
- Loaded dataset from CSV and checked `head()`, `info()`, `describe()`, shape, duplicates, missing values

### 2) Data cleaning and column pruning
- Dropped columns with low utility / high missingness:
	- `Index`, `Description`, `Amount(in rupees)`, `Society`, `Dimensions`, `overlooking`, `Plot Area`, `facing`
- Removed rows where target was missing (`Price (in rupees)`)
- Removed rows with missing key categoricals (`Status`, `Furnishing`, `Transaction`, `location`, `Car Parking`, `Ownership`)
- Dropped `Super Area`

### 3) Feature engineering from text fields
- Converted `Carpet Area` text into structured numeric components:
	- extracted numeric value (`area_value`)
	- extracted unit (`sqft`, `sqm`, `sqyard`)
	- converted to standardized `Carpet Area(Sqft)` (including sqm conversion)
- Built quality filters:
	- kept `Carpet Area(Sqft)` between 200 and 4000
	- kept positive prices only
- Created `Price Per Sqft` for analysis, then removed it from final training data
- Cleaned floor information:
	- parsed `Total Floors` from `Floor`
	- created `Current Floor` with custom logic for basement / ground / numbered floors
- Extracted `BHK` from `Title`

### 4) Type fixing, imputation, and consistency
- Converted `Bathroom` and `Balcony` to numeric
- Filled missing values in numeric columns using median/mean where needed
- Cleaned extreme string values like `>10` into numeric values
- Dropped temporary/helper columns after transformation
- Removed duplicates in final processed data

### 5) Outlier handling
- Applied IQR-based filtering on `Price (in rupees)` to reduce extreme values

### 6) Modeling and evaluation
- Prepared features and target:
	- `X = df.drop('Price (in rupees)')`
	- `y = df['Price (in rupees)']`
- Applied one-hot encoding (`pd.get_dummies`)
- Split data into train/test (`test_size=0.2`, `random_state=42`)
- Trained and compared:
	- `RandomForestRegressor`
	- `GradientBoostingRegressor`
- Evaluated with:
	- `R²`
	- `MAE`
	- `RMSE`
- Selected best model by highest R²

### 7) Artifact saving for deployment
- Saved best model: `best_model.pkl`
- Saved encoded training columns: `columns.pkl`
- Saved categorical options map: `unique_categories.pkl`

---

## 📚 What I Learned (Meaningful Takeaways)

### 1) Real-world data is messy
I learned that most work happens before modeling. Columns had mixed formats, missing values, and noisy text patterns. Cleaning this properly made model training possible.

### 2) Feature engineering is critical
Converting `Carpet Area` strings to standardized square feet and extracting `BHK`, `Current Floor`, and `Total Floors` taught me how domain features can strongly improve model quality.

### 3) Outlier handling changes model behavior
Using IQR filtering on price showed me that extreme values can distort regression models. Controlled outlier removal improved stability.

### 4) Categorical encoding must be reproducible
I learned not to rely on ad-hoc encoding. Saving encoded column structure (`columns.pkl`) is essential so app-time input matches training-time schema.

### 5) Model comparison beats model guessing
Instead of picking one algorithm directly, I compared Random Forest vs Gradient Boosting with the same split and metrics. This gave an evidence-based model choice.

### 6) Metrics should be read together
R² alone is not enough. Combining R², MAE, and RMSE gave better understanding of prediction quality and error magnitude.

### 7) Deployment needs more than a `.pkl` model
I learned that model deployment also needs metadata artifacts (columns + categories). Without them, UI predictions can break or become inconsistent.

### 8) Notebook-to-app transition is a separate skill
Building the notebook taught modeling; integrating it into Streamlit taught product thinking: user inputs, validation, transformations, and safe prediction flow.

### 9) Data pipeline discipline matters
Temporary columns (`area_value`, `area_unit`, `Price Per Sqft`) are useful during engineering, but I learned to drop them cleanly before final training to avoid leakage/confusion.

### 10) End-to-end ML is about reliability
The biggest learning: a successful ML project is not just “trained model works once,” but a repeatable pipeline that can be understood, reused, and deployed.

---

## 🗂️ Project Files

- `housepriceprediction.ipynb` → Full training and experimentation workflow
- `app.py` → Streamlit inference app
- `best_model.pkl` → Selected trained model
- `columns.pkl` → Encoded training feature columns
- `unique_categories.pkl` → Dropdown category values
- `requirements.txt` → Dependency list

---

## ▶️ Run the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Note

This is a learning and portfolio project. Predictions are for educational/demo purposes.
