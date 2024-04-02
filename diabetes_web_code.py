
import  pickle
import streamlit as st
import numpy as np
import pandas as pd

#Loading the saved models
diabetes_model = pickle.load(open("C:\\Users\\hp\\Desktop\\Diabetes_Prediction_model\\diabetes_model.sav",'rb'),errors='ignore',encoding='latin1')


with st.sidebar:

       selected = st.selectbox(
        'Diabetes Disease Prediction System',
        ('Diabetes Prediction',)
        )
#Diabetes Prediction page
if(selected == 'Diabetes Prediction'):
    #Page title
    st.title('Diabetes Prediction Using ML')
    
    #Input Fields for Variables Column wise
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Level')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    with col2:
        Age = st.text_input('Age of the Patient')
        
    
    
    #Code for Prediction
    diabetes_diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diabetes_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,
                                                       DiabetesPedigreeFunction,Age]])
        if diabetes_prediction[0] == 1:
            diabetes_diagnosis = 'The Person is Likely to be Diabetic'
        else:
            diabetes_diagnosis = 'The Person is NOT likely to be diabetic'
    st.success(diabetes_diagnosis)
        
        
    


