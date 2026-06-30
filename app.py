import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ---------------- Load Model ----------------
model = joblib.load("models/house_price_model.pkl")

# ---------------- Title ----------------
st.title("🏠 House Price Prediction")
st.caption("Predict house prices using Machine Learning.")

st.divider()

# ---------------- Input Section ----------------
st.subheader("Property Details")

area = st.number_input(
    "Area (sq.ft)",
    min_value=500,
    max_value=5000,
    value=1200,
    step=100
)

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=5,
        value=2
    )

    age = st.number_input(
        "Age (Years)",
        min_value=0,
        max_value=50,
        value=5
    )

with col2:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=5,
        value=2
    )

    parking = st.number_input(
        "Parking",
        min_value=0,
        max_value=2,
        value=1
    )

location = st.selectbox(
    "Location",
    ["Kalyan", "Mumbai", "Navi Mumbai", "Pune", "Thane"]
)

# ---------------- One-Hot Encoding ----------------
location_mumbai = 1 if location == "Mumbai" else 0
location_navi_mumbai = 1 if location == "Navi Mumbai" else 0
location_pune = 1 if location == "Pune" else 0
location_thane = 1 if location == "Thane" else 0

# ---------------- Prediction ----------------
if st.button("Predict Price", use_container_width=True):

    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Age": [age],
        "Parking": [parking],
        "Location_Mumbai": [location_mumbai],
        "Location_Navi Mumbai": [location_navi_mumbai],
        "Location_Pune": [location_pune],
        "Location_Thane": [location_thane]
    })

    prediction = model.predict(input_data)[0]

    st.divider()

    st.metric(
        label="Estimated House Price",
        value=f"₹ {prediction:,.0f}"
    )

st.divider()
