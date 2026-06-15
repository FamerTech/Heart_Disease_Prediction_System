import numpy as np
import pandas as pd
import pickle
import streamlit as st
import os

st.set_page_config(page_title="Heart Disease Prediction", page_icon=":heart:", layout="wide")


# Load the trained model
loaded_model = pickle.load(open('saved_model/heart_disease_model.sav', 'rb'))

def predict_heart_disease(input_data):
   input_data_as_numpy_array = np.asarray(input_data, dtype=np.float64)
   input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
   prediction = loaded_model.predict(input_data_reshaped)

   if prediction[0] == 0:
    return "The person does not have a Heart Disease"
   else:
    return "The person has a Heart Disease"


def main():

  # Custom CSS for styling
  st.markdown(
      """
      <style>


      .stButton>button {
          background-color: #4CAF50; /* Green button */
          color: white;
          border-radius: 5px;
          border: none;
          padding: 10px 20px;
          font-size: 16px;
          cursor: pointer;
      }
      .stButton>button:hover {
          background-color: #45a049;
      }
      </style>
      """,
      unsafe_allow_html=True
  )

  st.title("Heart Disease Prediction System")

  col1, col2, col3 = st.columns(3)

  with col1:
      age = st.text_input("Age of the person")
      sex = st.text_input("Sex of the person (0 = Female, 1 = Male)")
      cp = st.text_input("Chest Pain type (0-3)")
      trestbps= st.text_input("Resting Blood Pressure")
      chol = st.text_input("Cholesterol in mg/dl")

  with col2:
      fbs = st.text_input("Fasting Blood Sugar > 120 mg/dl (0 = No, 1 = Yes)")
      restecg = st.text_input("Resting Electrocardiographic results (0-2)")
      thalach = st.text_input("Maximum Heart Rate achieved")
      exang = st.text_input("Exercise induced angina (0 = No, 1 = Yes)")
      oldpeak = st.text_input("ST depression induced by exercise relative to rest")

  with col3:
      slope = st.text_input("Slope of the peak exercise ST segment (0-2)")
      ca = st.text_input("Number of major vessels (0-3) colored by flourosopy")
      thal = st.text_input("Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)")

  # code for prediction
  diagnosis = ''

  # creating button for prediction
  if st.button('Heart Disease Test Result'):
     try:
         # Convert all inputs to float before passing to the prediction function
         input_list = [float(age), float(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg), float(thalach), float(exang), float(oldpeak), float(slope), float(ca), float(thal)]
         diagnosis = predict_heart_disease(input_list)
         st.success(diagnosis)
     except ValueError:
         diagnosis = "Please enter valid numeric values for all fields."
         st.error(diagnosis)


if __name__ == '__main__':
  main()
