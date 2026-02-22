import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="House Price Prediction", layout="centered")
# ---------------- LOAD MODEL ----------------
@st.cache_resource
def load_model():
    model = joblib.load("best_model.pkl")
    columns = joblib.load("columns.pkl")
    return model, columns

model, model_columns = load_model()

st.title("🏠 House Price Prediction")
st.write("Enter property details to estimate price.")

# ---------------- INPUTS ----------------

bhk = st.number_input("BHK", min_value=1, step=1)
carpet_area = st.number_input("Carpet Area (SQFT)", min_value=bhk * 250, step=50)
bathroom = st.number_input("Bathrooms", min_value=1, step=1)
balcony = st.number_input("Balcony", min_value=0, step=1)
current_floor = st.number_input("Current Floor", min_value=-2, step=1)
total_floor = st.number_input("Total Floors", min_value=1, step=1)

location = st.selectbox("Location", sorted([col.replace("location_", "") 
                    for col in model_columns if col.startswith("location_")]))

transaction = st.selectbox("Transaction", ["Resale", "Other", "Rent/Lease"])

furnishing = st.selectbox("Furnishing", ["Semi-Furnished", "Unfurnished"])

ownership = st.selectbox("Ownership", ["Freehold", "Leasehold", "Power Of Attorney"])

# ---------------- VALIDATION ----------------
# if current_floor > total_floor:
#     st.error("❌ Current Floor cannot be greater than Total Floors")
#     st.stop()
errors = []
if carpet_area < bhk * 250:
    errors.append(f"Minimum area for {bhk} BHK should be at least {bhk * 250} SQFT.")
if bathroom > bhk + 1:
    errors.append(f"Too many bathrooms for {bhk} BHK. Typically, it should be at most {bhk + 1}.")
if balcony > bhk:
    errors.append(f"Too many balconies for {bhk} BHK. Typically, it should be at most {bhk}.")
if current_floor > total_floor:
    errors.append("Current Floor cannot be greater than Total Floors.")

# ---------------- PREDICTION ----------------
if st.button("Predict Price 💰"):
    if errors:
        for e in errors:
            st.error(f"❌ {e}")
        st.stop()

    # input_data = {
    #     "Bathroom": bathroom,
    #     "Balcony": balcony,
    #     "Total Floor": total_floor,
    #     "Current Floor": current_floor,
    #     "Carpet Area(SQFT)": carpet_area,
    #     "BHK": bhk,
    #     "location_" + location: 1,
    #     "Transaction_" + transaction: 1,
    #     "Furnishing_" + furnishing: 1,
    #     "Ownership_" + ownership: 1
    # }

    # Create empty dataframe with all columns
    input_df = pd.DataFrame(0, index=[0], columns=model_columns)

    input_df.at[0, "Bathroom"] = bathroom
    input_df.at[0, "Balcony"] = balcony
    input_df.at[0, "Total Floor"] = total_floor
    input_df.at[0, "Current Floor"] = current_floor
    input_df.at[0, "Carpet Area(SQFT)"] = carpet_area
    input_df.at[0, "BHK"] = bhk

    location_col = "location_" + location
    transaction_col = "Transaction_" + transaction
    furnishing_col = "Furnishing_" + furnishing
    ownership_col = "Ownership_" + ownership

    # Fill selected values
    # for key, value in input_data.items():
    #     if key in input_df.columns:
    #         input_df.at[0, key] = value
    for col in [location_col, transaction_col, furnishing_col, ownership_col]:
        if col in input_df.columns:
            input_df.at[0, col] = 1

    # Predict
    prediction_lakh = model.predict(input_df)[0]

    st.success(f"💰 Estimated Price: ₹{prediction_lakh:.2f} Lakhs")
    st.info(f"≈ ₹{prediction_lakh * 100000:,.0f} Rupees")
    st.info(f"≈ ₹{prediction_lakh / 100:.2f} Crore")
