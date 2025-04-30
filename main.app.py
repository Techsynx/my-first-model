import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('model.pkl')

# Streamlit app title
st.title("Water Potability Predictor")

# Input fields
ph = st.number_input("pH")
hardness = st.number_input("Hardness")
solids = st.number_input("Solids")
chloramines = st.number_input("Chloramines")
sulfate = st.number_input("Sulfate")
conductivity = st.number_input("Conductivity")
organic_carbon = st.number_input("Organic Carbon")
trihalomethanes = st.number_input("Trihalomethanes")
turbidity = st.number_input("Turbidity")

# Predict button
if st.button("Predict Potability"):
    input_data = np.array([[ph, hardness, solids, chloramines, sulfate,
                            conductivity, organic_carbon, trihalomethanes, turbidity]])
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.success("✅ Water is Potable (Safe to drink)")
    else:
        st.error("❌ Water is Not Potable")
