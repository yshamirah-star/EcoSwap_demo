
  import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="EcoSwap Demo", layout="wide")

# Sidebar navigation
st.sidebar.title("EcoSwap Demo")
section = st.sidebar.radio(
    "Choose a section:",
    ["Credibility Score", "Waste Image Generator", "Recycler Recommendations"]
)

# Load model once
model = joblib.load("credibility_model.pkl")

# --- Section: Credibility Score ---
if section == "Credibility Score":
    st.title("Predict Seller Credibility Score")

    with st.form("credibility_form"):
        quantity = st.number_input("Quantity (kg)", min_value=0.0, step=0.1)
        price = st.number_input("Price per kg (₦)", min_value=0.0, step=0.01)
        distance = st.number_input("Delivery Distance (km)", min_value=0.0, step=0.1)
        saving = st.number_input("Estimated Cost Saving (₦)", min_value=0.0, step=1.0)
        submitted = st.form_submit_button("Predict Seller Score")

        if submitted:
            input_data = pd.DataFrame({
                "quantity_kg": [quantity],
                "price_per_kg(₦)": [price],
                "delivery_distance_km": [distance],
                "estimated_cost_saving(₦)": [saving]
            })
            prediction = model.predict(input_data)
            st.success(f"Predicted Seller Score: {prediction[0]}")

# --- Section: Waste Image Generator ---
elif section == "Waste Image Generator":
    st.title("Generate Waste Image")

    with st.form("waste_image_form"):
        waste_types = ["Plastics", "Paper", "Textiles", "Organics", "Mixed_Industrial"]
        selected_waste = st.selectbox("Choose Waste Type", waste_types)

        sample_images = {
            "Plastics": "https://copilot.microsoft.com/th/id/BCO.c37bb345-9c08-4f57-a85e-fcecd80b203e.png",
            "Paper": "https://copilot.microsoft.com/th/id/BCO.2cc0fa88-a133-4e80-b3e0-25f9ff72e3ef.png",
            "Textiles": "https://copilot.microsoft.com/th/id/BCO.98f99866-f964-4caa-aa95-2613bf168311.png",
            "Organics": "https://copilot.microsoft.com/th/id/BCO.97d8d2d3-dd8e-435c-a2d6-5eec59203677.png",
            "Mixed_Industrial": "https://copilot.microsoft.com/th/id/BCO.5be61b44-40f0-424d-8928-b67fd83b1d17.png"
        }

        submitted = st.form_submit_button("Generate Waste Image")
        if submitted:
            st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)

# --- Section: Recycler Recommendations ---
elif section == "Recycler Recommendations":
    st.title("Recycler Company Recommendations (Lagos)")

    with st.form("recycler_form"):
        waste_types = ["Plastics", "Paper", "Textiles", "Organics", "Mixed_Industrial"]
        selected_waste = st.selectbox("Select Waste Type", waste_types)
        submitted = st.form_submit_button("Find Recyclers")

        if submitted:
            recycler_data = {
                "Plastics": [
                    {"Name": "Green Space Recycling Services Ltd", "Location": "Ikorodu, Lagos", "Focus": "PET plastics recycling", "Contact": "+234 706 218 9738"},
                    {"Name": "Chris Pet Plastics Industry", "Location": "Ojo, Lagos", "Focus": "PET plastics recycling", "Contact": "+234 802 345 6789"}
                ],
                "Paper": [
                    {"Name": "Globetech Remedial Nig Ltd", "Location": "Maryland, Lagos", "Focus": "Paper & resource management", "Contact": "+234 909 484 6633"}
                ],
                "Textiles": [
                    {"Name": "Street Waste Company Ltd", "Location": "Igbosere Rd, Lagos", "Focus": "Textile & sustainable waste management", "Contact": "info@streetwaste.com.ng"}
                ],
                "Organics": [
                    {"Name": "Agoa Waste Management Co. Ltd", "Location": "Ojuelegba, Lagos", "Focus": "Organic waste recycling", "Contact": "+234 803 456 7890"}
                ],
                "Mixed_Industrial": [
                    {"Name": "Globetech Remedial Nig Ltd", "Location": "Maryland, Lagos", "Focus": "Industrial waste resource management", "Contact": "+234 909 484 6633"}
                ]
            }

            companies = recycler_data.get(selected_waste, [])
            if companies:
                for recycler in companies:
                    st.subheader(recycler["Name"])
                    st.markdown(f"📍 **Location:** {recycler['Location']}")
                    st.markdown(f"🔄 **Focus:** {recycler['Focus']}")
                    st.markdown(f"📞 **Contact:** {recycler['Contact']}")
                    st.markdown("---")
            else:
                st.warning("No recycler companies found for this waste type in Lagos.")  


            
