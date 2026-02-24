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
        "Plastics": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Plastic_bottles.jpg",
        "Paper": "https://upload.wikimedia.org/wikipedia/commons/6/6d/Waste_paper.jpg",
        "Textiles": "https://upload.wikimedia.org/wikipedia/commons/2/2d/Textile_waste.jpg",
        "Organics": "https://upload.wikimedia.org/wikipedia/commons/4/4e/Food_waste.jpg",
        "Mixed_Industrial": "https://upload.wikimedia.org/wikipedia/commons/9/9b/Industrial_waste.jpg"
    }
    st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
