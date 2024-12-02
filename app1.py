import streamlit as st
import pandas as pd
import pickle
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Load the saved model
with open("pcos_model_v2.pkl", "rb") as f:
    model = pickle.load(f)

# Function to make predictions
def predict_pcos(input_data):
    # Convert input to DataFrame
    input_df = pd.DataFrame(input_data, index=[0])
    
    # Predict using the model
    prediction = model.predict(input_df)
    return prediction[0]

# Streamlit user interface
st.title('PCOS Prediction')

st.write("""
### Please enter the following information for the prediction
""")

# User input fields
skin_darkening = st.selectbox('Skin Darkening (Y/N)', ['Y', 'N'])
hair_growth = st.selectbox('Hair Growth (Y/N)', ['Y', 'N'])
weight_gain = st.selectbox('Weight Gain (Y/N)', ['Y', 'N'])
cycle = st.number_input('Cycle (R/I)', min_value=0)  # Numerical input for cycle
fast_food = st.selectbox('Fast Food (Y/N)', ['Y', 'N'])
pimples = st.selectbox('Pimples (Y/N)', ['Y', 'N'])
follicle_no_r = st.number_input('Follicle No. (Right)', min_value=0)
follicle_no_l = st.number_input('Follicle No. (Left)', min_value=0)
amh = st.number_input('AMH (ng/ml)', min_value=0.0)
weight = st.number_input('Weight (kg)', min_value=0.0)

# Prepare input data for prediction
input_data = {
    'skin darkening (y/n)': skin_darkening,
    'hair growth(y/n)': hair_growth,
    'weight gain(y/n)': weight_gain,
    'cycle(r/i)': cycle,
    'fast food (y/n)': fast_food,
    'pimples(y/n)': pimples,
    'follicle no. (r)': follicle_no_r,
    'follicle no. (l)': follicle_no_l,
    'amh(ng/ml)': amh,
    'weight (kg)': weight
}

# Make prediction button
if st.button('Predict PCOS'):
    prediction = predict_pcos(input_data)
    
    if prediction == 'Y':
        st.write('### Prediction: Positive for PCOS (Y)')
    else:
        st.write('### Prediction: Negative for PCOS (N)')
