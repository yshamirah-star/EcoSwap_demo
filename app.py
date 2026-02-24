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
        "Plastics": "https://i.imgur.com/vHqC3qf.jpg", # Example direct link from Imgur
        "Paper": "https://i.imgur.com/2s351Dk.jpg",    # Example direct link from Imgur
        "Textiles": "https://i.imgur.com/gK2g05M.jpg",  # Example direct link from Imgur
        "Organics": "https://i.imgur.com/qL3gT1S.jpg",  # Example direct link from Imgur
        "Mixed_Industrial": "https://i.imgur.com/k2e5y7y.jpg"
    }
    st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
    }
