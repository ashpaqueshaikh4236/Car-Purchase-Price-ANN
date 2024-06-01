import streamlit as st
import numpy as np
from keras.models import load_model


model = load_model('model.keras')
st.write(model)

st.title("Car Purchase Predictor")

age = st.text_input('Age')
annual_salary = st.text_input('Annual Salary')
credit_card_debt = st.text_input('Credit Card Debt')
net_worth = st.text_input('Net Worth')
	
Selected_data = (age,annual_salary,credit_card_debt,net_worth)

try:
    if st.button('predict'):
        reshaped_data = np.asarray(Selected_data, dtype=float).reshape(1, -1)
	    
        if '' in reshaped_data:
            st.warning('Please fill all values')
        else:
            prediction = model.predict(reshaped_data)
            st.success('Car Purchase Amount ' + str(prediction[0]))
except Exception as e:
    st.warning(f'An error occurred: {e}')
