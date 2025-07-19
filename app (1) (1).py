import streamlit as st
import joblib
import numpy as np

# Load the trained model and encoder
model = joblib.load("house_price_model.pkl")
le = joblib.load("location_encoder.pkl")

st.title("🏠 House Price Prediction App")

# Input fields
area = st.number_input("Area (in sqft)", min_value=500, max_value=10000, value=1200)
bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
location = st.selectbox("Location", le.classes_)

# Prediction button
if st.button("Predict Price"):
    location_encoded = le.transform([location])[0]
    input_data = np.array([[area, bedrooms, location_encoded]])
    prediction = model.predict(input_data)
    st.success(f"🏡 Estimated House Price: ₹{int(prediction[0]):,}")
