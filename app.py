import pandas as pd
import joblib
import random
import streamlit as st

# Load the trained credibility model
model = joblib.load("credibility_model.pkl")

st.title("EcoSwap Seller Credibility & Waste Demo")

# --- Seller Score Prediction ---
st.header("Predict Seller Credibility Score")

# Example input fields (adjust to match your dataset features)
quantity = st.number_input("Quantity (kg)", min_value=0.0, step=0.1)
price = st.number_input("Price per kg (₦)", min_value=0.0, step=0.01)
distance = st.number_input("Delivery Distance (km)", min_value=0.0, step=0.1)
saving = st.number_input("Estimated Cost Saving (₦)", min_value=0.0, step=1.0)

if st.button("Predict Seller Score"):
    # Build input DataFrame
    input_data = pd.DataFrame({
        "quantity_kg": [quantity],
        "price_per_kg(₦)": [price],
        "delivery_distance_km": [distance],
        "estimated_cost_saving(₦)": [saving]
    })
    prediction = model.predict(input_data)
    st.success(f"Predicted Seller Score: {prediction[0]}")

# --- Waste Image Generator ---
st.header("Generate Waste Image")

waste_types = ["Plastics", "Paper", "Textiles", "Organics", "Mixed_Industrial"]
selected_waste = st.selectbox("Choose Waste Type", waste_types)

# AI-generated image URLs

    sample_images = {
    "Plastics": "https://copilot.microsoft.com/th/id/BCO.c37bb345-9c08-4f57-a85e-fcecd80b203e.png",
    "Paper": "https://copilot.microsoft.com/th/id/BCO.2cc0fa88-a133-4e80-b3e0-25f9ff72e3ef.png",
    "Textiles": "https://copilot.microsoft.com/th/id/BCO.98f99866-f964-4caa-aa95-2613bf168311.png",
    "Organics": "https://copilot.microsoft.com/th/id/BCO.97d8d2d3-dd8e-435c-a2d6-5eec59203677.png",
    "Mixed_Industrial": "https://copilot.microsoft.com/th/id/BCO.5be61b44-40f0-424d-8928-b67fd83b1d17.png"
    }
if st.button("Generate Waste Image"):
    st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
    
