import streamlit as st
import pandas as pd
import joblib

# --- App Config ---
st.set_page_config(page_title="EcoSwap Demo", layout="wide")

# --- Sidebar ---
st.sidebar.title("EcoSwap Demo")
st.sidebar.markdown("""
Welcome to the EcoSwap Seller Credibility & Waste Demo!  
Use the main panel to predict seller scores, visualize waste types, and discover recyclers near you.
""")

section = st.sidebar.radio("Choose a section:", ["Credibility Score", "Waste Image Generator", "Recycler Recommendations"])

# --- Load Model ---
model = joblib.load("credibility_model.pkl")

# --- Section: Credibility Score ---
if section == "Credibility Score":
    st.title("Predict Seller Credibility Score")

    quantity = st.number_input("Quantity (kg)", min_value=0.0, step=0.1)
    price = st.number_input("Price per kg (₦)", min_value=0.0, step=0.01)
    distance = st.number_input("Delivery Distance (km)", min_value=0.0, step=0.1)
    saving = st.number_input("Estimated Cost Saving (₦)", min_value=0.0, step=1.0)

    if st.button("Predict Seller Score"):
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

    waste_types = ["Plastics", "Paper", "Textiles", "Organics", "Mixed_Industrial"]
    selected_waste = st.selectbox("Choose Waste Type", waste_types)

    sample_images = {
        "Plastics": "https://copilot.microsoft.com/th/id/BCO.c37bb345-9c08-4f57-a85e-fcecd80b203e.png",
        "Paper": "https://copilot.microsoft.com/th/id/BCO.2cc0fa88-a133-4e80-b3e0-25f9ff72e3ef.png",
        "Textiles": "https://copilot.microsoft.com/th/id/BCO.98f99866-f964-4caa-aa95-2613bf168311.png",
        "Organics": "https://copilot.microsoft.com/th/id/BCO.97d8d2d3-dd8e-435c-a2d6-5eec59203677.png",
        "Mixed_Industrial": "https://copilot.microsoft.com/th/id/BCO.5be61b44-40f0-424d-8928-b67fd83b1d17.png"
    }

    if st.button("Generate Waste Image"):
        st.image(sample_images[selected_waste], caption=f"{selected_waste} Waste", use_column_width=True)
        
# --- Section: Recycler Recommendations ---
elif section == "Recycler Recommendations":
    st.title("Recycler Company Recommendations (Lagos)")

    waste_types = ["Plastics", "Paper", "Textiles", "Organics", "Mixed_Industrial"]
    selected_waste = st.selectbox("Select Waste Type", waste_types)

    # Lagos recycler dataset
    recycler_data = {
        "Plastics": [
            {
                "Name": "Green Space Recycling Services Ltd",
                "Location": "Afa, Igbe Rd, Ikorodu, Lagos",
                "Focus": "Transforming PET plastic waste into valuable resources",
                "Contact": "+234 706 218 9738"
            },
            {
                "Name": "Chris Pet Plastics Industry",
                "Location": "Ojo Local Government Secretariat, Ojo-Costain Rd, Iyana-Iba, Lagos",
                "Focus": "PET plastics recycling",
                "Contact": "+234 802 345 6789"
            }
        ],
        "Paper": [
            {
                "Name": "Globetech Remedial Nig Ltd",
                "Location": "13B Ikorodu Rd, Maryland, Lagos",
                "Focus": "Waste resource management including paper recycling",
                "Contact": "+234 909 484 6633"
            }
        ],
        "Textiles": [
            {
                "Name": "Street Waste Company Ltd",
                "Location": "159 Igbosere Rd, Opposite Court of Appeal, Lagos",
                "Focus": "Sustainable waste management including textiles",
                "Contact": "info@streetwaste.com.ng"
            }
        ],
        "Organics": [
            {
                "Name": "Agoa Waste Management Co. Ltd",
                "Location": "124A Ayilara Bus Stop, Ojuelegba Rd, Lagos",
                "Focus": "General waste management including organic waste",
                "Contact": "+234 803 456 7890"
            }
        ],
        "Mixed_Industrial": [
            {
                "Name": "Globetech Remedial Nig Ltd",
                "Location": "13B Ikorodu Rd, Maryland, Lagos",
                "Focus": "Industrial waste resource management",
                "Contact": "+234 909 484 6633"
            }
        ]
    }

    # Display recommendations based on selected waste type
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
