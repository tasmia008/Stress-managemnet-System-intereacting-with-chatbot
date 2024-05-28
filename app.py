# from flask import Flask, request, render_template
# import numpy as np
# import joblib

# app = Flask(__name__)

# # Load the saved model
# loaded_model = joblib.load('decision_tree_model.pkl')

# # Define the prediction labels
# prediction_labels = {
#     0: "Not experiencing any symptoms of depression.",
#     1: "Mild symptoms of depression, such as occasional feelings of sadness or low energy.",
#     2: "Moderate symptoms of depression, with more frequent feelings of sadness, difficulty concentrating, and decreased motivation.",
#     3: "Moderate to severe symptoms of depression, including persistent feelings of sadness, hopelessness, and significant difficulty in functioning in daily life.",
#     4: "Extreme symptoms of depression, with a high level of impairment in functioning and a significant risk of self-harm or suicidal thoughts."
# }

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     result = None
#     if request.method == 'POST':
#         try:
#             # Retrieve form data
#             symptoms_of_depression_frequency = int(request.form.get('symptoms_of_depression_frequency', 0))
#             engage_in_stress_relief_activities = 1 if request.form.get('engage_in_stress_relief_activities') == 'Yes' else 0
#             feel_pressure_to_excel_academically = 1 if request.form.get('feel_pressure_to_excel_academically') == 'Yes' else 0
#             academic_counseling_or_support = 1 if request.form.get('academic_counseling_or_support') == 'Yes' else 0
#             engaging_in_self_harming_behaviors = 1 if request.form.get('engaging_in_self_harming_behaviors') == 'Yes' else 0
#             professional_help_or_counseling_for_self_harm = 1 if request.form.get('professional_help_or_counseling_for_self_harm') == 'Yes' else 0
#             facing_discrimination_related_to_your_mental_health_issues = 1 if request.form.get('facing_discrimination_related_to_your_mental_health_issues') == 'Yes' else 0
#             accessible_counseling_services = int(request.form.get('accessible_counseling_services', 0))
#             contribution_of_lack_of_sleep_on_stress_level = int(request.form.get('contribution_of_lack_of_sleep_on_stress_level', 0))
#             gender = 1 if request.form.get('gender') == 'Male' else 0
#             diagnosed_with_depression = 1 if request.form.get('diagnosed_with_depression') == 'Yes' else 0
#             professional_help_or_counseling_for_depression_target = 1 if request.form.get('professional_help_or_counseling_for_depression_target') == 'Yes' else 0

#             # Prepare data for prediction
#             test_data = np.array([
#                 symptoms_of_depression_frequency,
#                 engage_in_stress_relief_activities,
#                 feel_pressure_to_excel_academically,
#                 academic_counseling_or_support,
#                 engaging_in_self_harming_behaviors,
#                 professional_help_or_counseling_for_self_harm,
#                 facing_discrimination_related_to_your_mental_health_issues,
#                 accessible_counseling_services,
#                 contribution_of_lack_of_sleep_on_stress_level,
#                 gender,
#                 diagnosed_with_depression,
#                 professional_help_or_counseling_for_depression_target
#             ]).reshape(1, -1)

#             # Make prediction
#             prediction = loaded_model.predict(test_data)[0]
#             result = prediction_labels.get(int(prediction), "Unknown label")
#         except Exception as e:
#             result = f"Error: {str(e)}"

#     return render_template('index.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")



from flask import Flask, request, render_template, session, redirect, url_for
import numpy as np
import joblib

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Load the saved model
loaded_model = joblib.load('decision_tree_model.pkl')

# Define the prediction labels
prediction_labels = {
    0: """
Mild Depression (Level 1)
Symptoms: Persistent low mood, mild sadness, fatigue, slight changes in sleep or appetite,
reduced interest in activities.
Treatment Recommendations:
Lifestyle Changes: Regular exercise, balanced diet, good sleep hygiene.
Support Groups: Join peer support or group therapy.
Emotional Support: Reach out to friends or loved ones.
Music: Listen to or play enjoyable music.
Travel: Take short trips to break the routine.
Entertainment: Engage in hobbies, movies, books
""",

    1: """
Moderate Depression (Level 2)
Symptoms: Intense sadness, significant fatigue, noticeable changes in sleep and appetite,
reduced concentration, loss of interest.
Treatment Recommendations:
Psychotherapy: Cognitive Behavioral Therapy (CBT) or Interpersonal Therapy (IPT).
Combination Therapy: Psychotherapy and medication.
Lifestyle Changes: Regular exercise, nutritious diet, structured activities.
Music, Travel, Entertainment: Continue engaging in enjoyable activities.
""",
    2: """
Severe Depression (Level 3)
Symptoms: Intense sadness, significant weight changes, severe sleep issues, lack of
energy, feelings of worthlessness, thoughts of death or suicide.
Treatment Recommendations:
Intensive Psychotherapy: Frequent CBT or other intensive therapy.
Medication: Higher doses or combinations of antidepressants.
Hospitalization: For safety and intensive treatment.
ECT: Electroconvulsive therapy.
Supportive Care: Strong support system, case management.

""",
    3: """
Psychotic Depression (Level 4) 
Symptoms: Severe depression with psychotic symptoms like delusions or hallucinations. 
Treatment Recommendations:
Hospitalization: For stabilization and safety.
Combination Medication: Antidepressants with antipsychotics.
ECT: Highly effective for severe cases.
Intensive Psychotherapy: Post-psychosis treatment.

""",
    4: """
Treatment-Resistant Depression (Level 5)
Symptoms: Persistent severe depression unresponsive to standard treatments.
Treatment Recommendations:
Advanced Medication Strategies: Different combinations, mood stabilizers, ketamine
infusions.
ECT: Effective for many with treatment-resistant depression.
TMS: Transcranial magnetic stimulation.
VNS: Vagus nerve stimulation.
Intensive Psychotherapy: Continued or more intensive therapy like CBT or DBT.
Lifestyle Interventions: Regular exercise, healthy diet, sleep hygiene, integrative therapies.
Support Systems: Strong support network, frequent healthcare visits, support groups.

"""
}

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/page2', methods=['POST'])
def page2():
    # Store data from page 1 in session
    session['data_page1'] = request.form.to_dict()
    return render_template('index2.html')

@app.route('/page3', methods=['POST'])
def page3():
    # Store data from page 2 in session
    session['data_page2'] = request.form.to_dict()
    return render_template('index3.html')

@app.route('/', methods=['POST'])
def predict():
    # Combine data from all pages
    data = {**session.get('data_page1', {}), **session.get('data_page2', {}), **request.form.to_dict()}
    try:
        # Prepare data for prediction
        test_data = np.array([
            int(data['symptoms_of_depression_frequency']),
            int(data['engage_in_stress_relief_activities'] == 'Yes'),
            int(data['feel_pressure_to_excel_academically'] == 'Yes'),
            int(data['academic_counseling_or_support'] == 'Yes'),
            int(data['engaging_in_self_harming_behaviors'] == 'Yes'),
            int(data['professional_help_or_counseling_for_self_harm'] == 'Yes'),
            int(data['facing_discrimination_related_to_your_mental_health_issues'] == 'Yes'),
            int(data['accessible_counseling_services']),
            int(data['contribution_of_lack_of_sleep_on_stress_level']),
            int(data['gender'] == 'Male'),
            int(data['diagnosed_with_depression'] == 'Yes'),
            int(data['professional_help_or_counseling_for_depression_target'] == 'Yes')
        ]).reshape(1, -1)

        # Make prediction
        prediction = loaded_model.predict(test_data)[0]
        result = prediction_labels.get(int(prediction), "Unknown label")
        # formatted_result = result.replace("\n", "<br>")
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

# result = "This is line one.\nThis is line two.\nThis is line three."
#     formatted_result = result.replace("\n", "<br>")
#     return render_template('your_template.html', result=formatted_result)