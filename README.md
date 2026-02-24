# EcoSwap Seller Credibility & Waste Demo

EcoSwap is a sustainability-focused B2B marketplace concept that enables African SMEs to trade industrial byproducts as raw materials.  
This demo app showcases two core features:

1. **Seller Credibility Prediction**  
   - A trained machine learning model (`credibility_model.pkl`) predicts seller credibility scores based on marketplace features such as:
     - Quantity (kg)
     - Price per kg (₦)
     - Delivery distance (km)
     - Estimated cost saving (₦)

2. **Waste Image Generator**  
   - Users can select a waste category (Plastics, Paper, Textiles, Organics, Mixed Industrial).  
   - The app displays sample images to illustrate different waste types.

---

## 🚀 Live Demo
Try the app here:  
👉 [EcoSwap Demo on Streamlit](https://ecoswapdemo-d6kumqpvteejsgk8e6kb5r.streamlit.app)

---

## 📂 Repository
Source code available here:  
👉 [EcoSwap_demo GitHub Repo](https://github.com/yshamirah-star/EcoSwap_demo)

---

## ⚙️ Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/yshamirah-star/EcoSwap_demo.git
cd EcoSwap_demo
pip install -r requirements.txt

🛠 Requirements
The app depends on:
• 	streamlit
    pandas
    scikit-learn
• 	joblib

📌 Notes
• 	This is a minimal demo built for submission deadlines.
• 	Maps and advanced marketplace features will be added in future iterations.
• 	The credibility model was trained using scikit-learn and saved with joblib.

🔮 Future Work
Planned enhancements include:
• 	Interactive Maps: Visualizing waste listings and trades across African cities.
• 	Credibility Dashboard: Richer scoring metrics, trust indicators, and seller/buyer profiles.
• 	Marketplace Matching Logic: Automated matching of waste types to industries with cost-saving estimates.
• 	Image Generation: AI-generated waste images for more realistic visualizations.
• 	Analytics & KPIs: Tracking sustainability impact, cost savings, and trade volumes.

✨ Author
Developed by the Data Science group 51
WTF/Tech4dev, EcoSwap Project
	
	
