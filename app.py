# app.py
import streamlit as st
import pandas as pd
import pickle

# Load saved model & encoders
model = pickle.load(open("best_model.pkl", "rb"))
le_state = pickle.load(open("state_encoder.pkl", "rb"))
le_district = pickle.load(open("district_encoder.pkl", "rb"))
le_crime = pickle.load(open("crime_encoder.pkl", "rb"))

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🔮 Crime Type Prediction App")
st.write("Predict the **most likely type of crime** based on Year, State, and District.")

year = st.number_input("Enter Year", min_value=2000, max_value=2030, step=1)
state_name = st.text_input("Enter State Name (exactly as in dataset)")
district_name = st.text_input("Enter District Name (exactly as in dataset)")

if st.button("Predict Crime Type"):
    try:
        s_enc = le_state.transform([state_name])[0]
        d_enc = le_district.transform([district_name])[0]
    except:
        st.error("❌ State or District not found in training data!")
        st.stop()

    X_new = pd.DataFrame([[year, s_enc, d_enc]], columns=['year', 'state_name', 'district_name'])
    pred = model.predict(X_new)[0]
    crime_label = le_crime.inverse_transform([pred])[0]

    st.success(f"🎯 Predicted Crime Type: **{crime_label.replace('_', ' ').title()}**")
