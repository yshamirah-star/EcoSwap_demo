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

if st.button("Generate Waste Image"):
    # Placeholder: random image URLs (replace with your own or integrate later)
    sample_images = {
       "Plastics": "https://images.unsplash.com/photo-1579547621617-be0876d7294b?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Pexels plastic waste
        "Paper": "https://images.unsplash.com/photo-1629815077478-f7564cc49195?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",   # Pexels paper waste
        "Textiles": "https://images.unsplash.com/photo-1549429462-df21f42d2a45?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Pexels textile waste
        "Organics": "https://images.unsplash.com/photo-1582234057861-c852e008b89e?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Pexels organic waste
        "Mixed_Industrial": "https://images.unsplash.com/photo-1620892976077-d652f1e626e2?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D" # Pexels industrial waste
    }
    st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
    
