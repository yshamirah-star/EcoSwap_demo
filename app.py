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
        "Plastics": "https://images.unsplash.com/photo-1574768399587-f2730103759b?q=80&w=1471&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Plastic waste in a dump
        "Paper": "https://images.unsplash.com/photo-1627885731215-64906f36809c?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",   # Paper/cardboard waste mixed with other trash
        "Textiles": "https://images.unsplash.com/photo-1614792618956-f6d3f26046e7?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Textile waste in a large pile
        "Organics": "https://images.unsplash.com/photo-1594191630713-7f722384c311?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", # Organic waste rotting in a pile
        "Mixed_Industrial": "https://images.unsplash.com/photo-1610475491176-79cf55171701?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&"
    }
    st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
    
