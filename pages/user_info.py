import streamlit as st

def user_info(unique_values):
  symptoms_of_depression_frequency = st.selectbox('Symptoms of depression frequency:', unique_values['symptoms of depression frequency'])
  engage_in_stress_relief_activities = st.selectbox('Engage in stress-relief activities:', unique_values['engage in stress-relief activities'])
  feel_pressure_to_excel_academically = st.selectbox('Feel pressure to excel academically:', unique_values['feel pressure to excel academically'])
  return symptoms_of_depression_frequency,engage_in_stress_relief_activities,feel_pressure_to_excel_academically


