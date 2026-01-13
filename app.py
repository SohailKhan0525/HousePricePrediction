import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model + scaler + columns
model = joblib.load("best_model.pkl")
# scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")
unique_categories = joblib.load("unique_categories.pkl")

st.markdown("❌This is not an actual dataset.")
st.markdown("Check out my all apps-> [My Apps](https://share.streamlit.io/user/sohailkhan0525)")
st.title("House Price Prediction")
st.write("Enter the details below to predict the house price.")

# -------------- INPUTS --------------

carpet_area = st.number_input("Carpet Area (sqft)", min_value=100, step=10)
bathroom = st.number_input("Bathrooms", min_value=0, step=1)
balcony = st.number_input("Balcony", min_value=0, step=1)
current_floor = st.number_input("Current Floor", min_value=0, step=1)
total_floor = st.number_input("Total Floor", min_value=1, step=1)

location = st.selectbox("Location", unique_categories["location"])
transaction = st.selectbox("Transaction", unique_categories["Transaction"])
furnishing = st.selectbox("Furnishing", unique_categories["Furnishing"])
facing = st.selectbox("Facing", unique_categories["facing"])
overlooking = st.selectbox("Overlooking", unique_categories["overlooking"])
car_parking = st.selectbox("Car Parking", unique_categories["Car Parking"])
ownership = st.selectbox("Ownership", unique_categories["Ownership"])

# ------------ VALIDATION -------------
errors = []

if current_floor > total_floor:
    errors.append("Current Floor cannot be greater than Total Floors.")

# -------------- PREDICTION --------------
if st.button("Predict Price"):

    floor_ratio = current_floor / total_floor
    is_top_floor = int(current_floor == total_floor)

    if errors:
        st.error("Please fix the following issues:")
        for e in errors:
            st.warning(e)
        st.stop()

    # Prepare input dictionary — FIXED names
    input_data = {
        "location": location,
        "Carpet Area": carpet_area,
        "Transaction": transaction,
        "Furnishing": furnishing,
        "facing": facing,
        "overlooking": overlooking,
        "Bathroom": bathroom,
        "Balcony": balcony,
        "Car Parking": car_parking,
        "Ownership": ownership,
        "Current Floor": current_floor,
        "Total Floor": total_floor,
        "Floor Ratio": floor_ratio,
        "Is top floor": is_top_floor
    }

    df_input = pd.DataFrame([input_data])

    # One-hot encode
    df_input_encoded = pd.get_dummies(df_input)

    # Align with training columns
    df_input = df_input.reindex(columns=columns, fill_value=0)

    # Predict
    prediction = model.predict(df_input_encoded)[0]

    st.success(f"Esimated Predicted Price: ₹{prediction:,.0f}")
