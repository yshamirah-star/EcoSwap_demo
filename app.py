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

