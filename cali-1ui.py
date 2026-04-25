import streamlit as st
import pickle
import numpy as np

# Load model (keep file in same folder)
model = pickle.load(open("Linear_Regression_california.pkl", "rb"))

st.title("🏠 California House Price Prediction")

# Input fields
MedInc = st.number_input("Median Income")
HouseAge = st.number_input("House Age")
Population = st.number_input("Population")
AveOccup = st.number_input("Average Occupancy")
AveBedrms = st.number_input("Average Bedrooms")
Latitude = st.number_input("Latitude")

if st.button("Predict"):
    if not all([MedInc, HouseAge, Population, AveOccup, AveBedrms, Latitude]):
        st.error("Please fill all fields!")
    else:
        input_data = np.array([[MedInc, HouseAge, Population, AveOccup, AveBedrms, Latitude]])
        prediction = model.predict(input_data)

        # Convert to price
        actual_price = prediction[0] * 100000
        formatted_price = f"₹ {actual_price:,.0f}"

        st.success(f"Estimated House Price: {formatted_price}")