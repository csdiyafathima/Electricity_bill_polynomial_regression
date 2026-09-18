import streamlit as st
import pandas as pd
import joblib
model_data = joblib.load("polynomial_regression_model_Electricitybill.pkl") 
poly = model_data["poly"] 
model = model_data["model"]
st.title("Electricity_Bill_prediction")
st.write(
    "Enter theAC Units to predict the Electricity Bill."
)
ac_units = st.number_input(
    " AC (units)",
    value=50.0,
    step=1.0
)
fan_units=st.number_input(
    "Fan(Units)",
    value=45.0,
    step=1.0
)
if st.button("Predict Electric Bill"): 
  if ac_units < 10:
    st.error("❌ AC Units must be 10 or above.")
  elif ac_units > 150:
    st.error("❌ AC Units must not be greater than 150.")
  elif fan_units <20:
      st.error("❌ Fan Units must be 20 or above.")
  elif fan_units >120:
      st.error("❌ Fan Units must not be greater than 120.)
  else:
   new_data = pd.DataFrame({ 
     "AC_Units": [ac_units],
     "Fan_Units":[fan_units]
    })
   new_data_poly = poly.transform(new_data)
      
   predicted_bill = model.predict(new_data_poly) 
   st.success( 
   f"Predicted Electric Bill: ₹{predicted_bill[0]:.2f}" )
