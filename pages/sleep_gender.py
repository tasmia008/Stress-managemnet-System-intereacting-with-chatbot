import streamlit as st

def sleep_gender(unique_values):
    st.subheader("Page 4: Sleep and Gender")
    accessible_counseling_services = st.selectbox('Accessible counseling services:', unique_values['accessible_counseling_services'])
    contribution_of_lack_of_sleep_on_stress_level = st.selectbox('Contribution of lack of sleep on stress level:', unique_values['contribution_of_lack_of_sleep_on_stress_level'])
    gender = st.selectbox('Gender:', unique_values['gender'])
    return accessible_counseling_services, contribution_of_lack_of_sleep_on_stress_level, gender, 
