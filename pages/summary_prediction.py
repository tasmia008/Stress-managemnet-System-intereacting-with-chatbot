import streamlit as st
import numpy as np
import joblib

def summary_prediction(column_names, unique_values):
    st.subheader("Page 5: Summary and Prediction")

    # Load the saved model
    loaded_model = joblib.load('decision_tree_model.pkl')

    # Create a form to input all values
    with st.form("my_form"):
        symptoms_of_depression_frequency = st.selectbox('Symptoms of depression frequency:', unique_values['symptoms_of_depression_frequency'])
        engage_in_stress_relief_activities = st.selectbox('Engage in stress-relief activities:', unique_values['engage_in_stress_relief_activities'])
        feel_pressure_to_excel_academically = st.selectbox('Feel pressure to excel academically:', unique_values['feel_pressure_to_excel_academically'])
        academic_counseling_or_support = st.selectbox('Academic counseling or support:', unique_values['academic_counseling_or_support'])
        engaging_in_self_harming_behaviors = st.selectbox('Engaging in self-harming behaviors:', unique_values['engaging_in_self_harming_behaviors'])
        professional_help_or_counseling_for_self_harm = st.selectbox('Professional help or counseling for self-harm:', unique_values['professional_help_or_counseling_for_self_harm'])
        facing_discrimination_related_to_your_mental_health_issues = st.selectbox('Facing discrimination related to your mental health issues:', unique_values['facing_discrimination_related_to_your_mental_health_issues'])
        accessible_counseling_services = st.selectbox('Accessible counseling services:', unique_values['accessible_counseling_services'])
        contribution_of_lack_of_sleep_on_stress_level = st.selectbox('Contribution of lack of sleep on stress level:', unique_values['contribution_of_lack_of_sleep_on_stress_level'])
        gender = st.selectbox('Gender:', unique_values['gender'])
        diagnosed_with_depression = st.selectbox('Diagnosed with depression:', unique_values['diagnosed_with_depression'])
        professional_help_or_counseling_for_depression_target = st.selectbox('Professional help or counseling for depression_target:', unique_values['professional_help_or_counseling_for_depression_target'])

        submitted = st.form_submit_button("Predict")

    if submitted:
        # Convert selected values to numeric
        test_data = np.array([
            symptoms_of_depression_frequency,
            1 if engage_in_stress_relief_activities == 'Yes' else 0,
            1 if feel_pressure_to_excel_academically == 'Yes' else 0,
            1 if academic_counseling_or_support == 'Yes' else 0,
            1 if engaging_in_self_harming_behaviors == 'Yes' else 0,
            1 if professional_help_or_counseling_for_self_harm == 'Yes' else 0,
            1 if facing_discrimination_related_to_your_mental_health_issues == 'Yes' else 0,
            accessible_counseling_services,
            contribution_of_lack_of_sleep_on_stress_level,
            1 if gender == 'Male' else 0,
            1 if diagnosed_with_depression == 'Yes' else 0,
            1 if professional_help_or_counseling_for_depression_target == 'Yes' else 0,
        ])

        test_data = test_data.reshape(1, test_data.shape[0])

        # Make prediction and display the result
        predictions = loaded_model.predict(test_data)
        prediction_labels = {
            0: "Not experiencing any symptoms of depression.",
            1: "Mild symptoms of depression, such as occasional feelings of sadness or low energy.",
            2: "Moderate symptoms of depression, with more frequent feelings of sadness, difficulty concentrating, and decreased motivation.",
            3: "Moderate to severe symptoms of depression, including persistent feelings of sadness, hopelessness, and significant difficulty in functioning in daily life.",
            4: "Extreme symptoms of depression, with a high level of impairment in functioning and a significant risk of self-harm or suicidal thoughts."
        }

        predicted_label = int(predictions[0])  # Convert to integer
        result = prediction_labels[predicted_label]
        st.write(f"Prediction Result: {result}")
