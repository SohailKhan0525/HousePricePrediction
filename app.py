import streamlit as st
import pandas as pd
import joblib

# ---------------- LOAD MODEL + ARTIFACTS ----------------
@st.cache_resource
def load_artifacts():
    model = joblib.load("best_model.pkl")
    columns = joblib.load("columns.pkl")
    unique_categories = joblib.load("unique_categories.pkl")
    return model, columns, unique_categories

model, columns, unique_categories = load_artifacts()

# ---------------- UI ----------------
st.title("🏠 House Price Prediction")
st.write("Enter property details to estimate price.")

# ---------------- INPUTS ----------------

carpet_area = st.number_input("Carpet Area (sqft)", min_value=100, step=10)
bathroom = st.number_input("Bathrooms", min_value=0, step=1)
balcony = st.number_input("Balcony", min_value=0, step=1)
current_floor = st.number_input("Current Floor", min_value=0, step=1)
total_floor = st.number_input("Total Floors", min_value=1, step=1)
bhk = st.number_input("BHK", min_value=1, step=1)

location = st.selectbox("Location", unique_categories["location"])
transaction = st.selectbox("Transaction", unique_categories["Transaction"])
furnishing = st.selectbox("Furnishing", unique_categories["Furnishing"])
car_parking = st.selectbox("Car Parking", unique_categories["Car Parking"])
ownership = st.selectbox("Ownership", unique_categories["Ownership"])

# ---------------- VALIDATION ----------------
if current_floor > total_floor:
    st.error("❌ Current Floor cannot be greater than Total Floors")
    st.stop()

# ---------------- PREDICTION ----------------
if st.button("Predict Price 💰"):

    # EXACT column names as training data
    input_data = {
        "Bathroom": bathroom,
        "Balcony": balcony,
        "Carpet Area(Sqft)": carpet_area,
        "Total Floors": total_floor,
        "Current Floor": current_floor,
        "BHK": bhk,
        "location": location,
        "Transaction": transaction,
        "Furnishing": furnishing,
        "Car Parking": car_parking,
        "Ownership": ownership
    }

    # Convert to DataFrame
    df_input = pd.DataFrame([input_data])

    # One-hot encode
    df_input_encoded = pd.get_dummies(df_input)

    # Align with training columns
    df_input_encoded = df_input_encoded.reindex(columns=columns, fill_value=0)

    # Predict
    prediction = model.predict(df_input_encoded)[0]

    st.success(f"💰 Estimated Price: ₹{prediction:,.0f}")