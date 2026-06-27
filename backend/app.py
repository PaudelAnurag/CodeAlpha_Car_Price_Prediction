import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load data
try:
    model = joblib.load("../model/best_model.pkl")
    
except:
    pass

try:
    model = joblib.load("model/best_model.pkl")
    
except:
    pass

st.title("Car Price Prediction")

Year = st.number_input(
    "Enter the model year",
    min_value=2000,
    max_value= 2026
    )

Present_Price = st.number_input(
    "Enter Present Price",
    min_value=0.5,
    max_value= 100.0
    )

Driven_kms = st.number_input(
    "Enter Driven kms",
    min_value=500
    )

Fuel_Type = st.selectbox(
    "Select Your Fuel Type?",
    ("Petrol", "Diesel", "CNG"),
)

Selling_type = st.selectbox(
    "Select Your Selling type?",
    ("Dealer", "Individual"),
)

Transmission = st.selectbox(
    "Select Your Transmission type?",
    ("Manual", "Automatic"),
)

Owner = st.selectbox(
        "Select Your Ownership type?",
    ("First Hand", "Second Hand", "More than second hand"),
)


Owner_mapped = {
    "First Hand" : 0,
    "Second Hand" : 1,
    "More than second hand" : 3,
}
owner = Owner_mapped[Owner]

if st.button("Predict"):
    
    new_data = pd.DataFrame({
        "Year": [Year],
        "Present_Price": [Present_Price],
        "Driven_kms": [Driven_kms],
        "Fuel_Type": [Fuel_Type],
        "Selling_type": [Selling_type],
        "Transmission": [Transmission],
        "Owner": [owner]
    })

    new_data["Driven_kms"] = np.log1p(new_data["Driven_kms"])
    new_data["Present_Price"] = np.log1p(new_data["Present_Price"])
    prediction = model.predict(new_data)
    prediction = np.expm1(prediction)

    st.success(f"Predicted Selling Price: Rs {abs(prediction[0]*100000):.2f}")

