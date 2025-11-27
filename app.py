import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model + scaler + columns
model = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")
unique_categories = joblib.load("unique_categories.pkl")

st.markdown("❌This is not an actual dataset.")
st.markdown("Check out my all apps-> [My Apps](https://share.streamlit.io/user/sohailkhan0525)")
st.title("House Price Prediction")
st.write("Enter the details below to predict the house price.")

# ----------- INPUT FIELDS -----------

carpet_area = st.number_input("Carpet Area (sqft)", min_value=0)
super_area = st.number_input("Super Area (sqft)", min_value=0)
bathrooms = st.number_input("Bathrooms", min_value=0)
balcony = st.number_input("Balcony", min_value=0)
car_parking = st.number_input("Car Parking", min_value=0)
current_floor = st.number_input("Current Floor", min_value=0)
total_floor = st.number_input("Total Floor", min_value=1)

location = st.selectbox("Location", sorted(unique_categories["location"]))
status = st.selectbox("Status", sorted(unique_categories["Status"]))
transaction = st.selectbox("Transaction", sorted(unique_categories["Transaction"]))
furnishing = st.selectbox("Furnishing", sorted(unique_categories["Furnishing"]))
facing = st.selectbox("Facing", sorted(unique_categories["facing"]))
overlooking = st.selectbox("Overlooking", sorted(unique_categories["overlooking"]))
ownership = st.selectbox("Ownership", sorted(unique_categories["Ownership"]))

# ------------ VALIDATION -------------
errors = []

if carpet_area > super_area:
    errors.append("Super Area must be greater than or equal to Carpet Area.")

if current_floor > total_floor:
    errors.append("Current Floor cannot be greater than Total Floors.")

# -------------- PREDICTION --------------
if st.button("Predict Price"):

    if errors:
        st.error("Please fix the following issues:")
        for e in errors:
            st.warning(e)
        st.stop()

    # Prepare input dictionary — FIXED names
    data = {
        "Carpet_Area": [carpet_area],
        "SuperArea": [super_area],
        "Bathroom": [bathrooms],
        "Balcony": [balcony],
        "CarParking": [car_parking],
        "Floor_num": [current_floor],
        "Total_Floor": [total_floor],
        "location": [location],
        "Status": [status],
        "Transaction": [transaction],
        "Furnishing": [furnishing],
        "facing": [facing],
        "overlooking": [overlooking],
        "Ownership": [ownership]
    }

    df_input = pd.DataFrame(data)

    # One-hot encode
    df_input_encoded = pd.get_dummies(df_input)

    # Align with training columns
    df_input_encoded = df_input_encoded.reindex(columns=columns, fill_value=0)

    # Correct numeric column list
    numeric_cols = [
    "Bathroom",
    "Balcony",
    "Carpet_Area",
    "Floor_num",
    "Total_Floor",
    "CarParking",
    "SuperArea"
]

    df_input_encoded[numeric_cols] = scaler.transform(df_input_encoded[numeric_cols])

    # Predict
    prediction = model.predict(df_input_encoded)[0]

    st.success(f"Predicted Price: ₹{prediction:,.0f}")
