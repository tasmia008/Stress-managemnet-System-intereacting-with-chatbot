import streamlit as st

def self_harm_discrimination(unique_values):
    st.subheader("Page 3: Self-Harm and Discrimination")
    engaging_in_self_harming_behaviors = st.selectbox('Engaging in self-harming behaviors:', unique_values['engaging_in_self_harming_behaviors'])
    professional_help_or_counseling_for_self_harm = st.selectbox('Professional help or counseling for self-harm:', unique_values['professional_help_or_counseling_for_self_harm'])
    facing_discrimination_related_to_your_mental_health_issues = st.selectbox('Facing discrimination related to your mental health issues:', unique_values['facing_discrimination_related_to_your_mental_health_issues'])
    return engaging_in_self_harming_behaviors, professional_help_or_counseling_for_self_harm, facing_discrimination_related_to_your_mental_health_issues
