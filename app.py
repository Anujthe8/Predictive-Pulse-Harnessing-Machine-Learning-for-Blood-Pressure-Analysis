import numpy as np
import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from flask import Flask, request, render_template
app = Flask( __name__, static_url_path='/Flask/static')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=["GET"])
def home():
   return render_template('main.html' )

@app.route('/index')
def index():
   return render_template('index.html')


@app.route('/Detail', methods=["GET" ] )
def Detail():
   return render_template('Detail.html')


@app.route('/Predict' , methods=["POST", "GET"])
def Predict():
    if request.method == "POST":
        Gender = float(request.form['Gender'])
        Age = float(request.form['Age'])
        History = float(request.form['History'])
        Patient = float(request.form['Patient'])
        TakeMedication = float(request.form['TakeMedication'])
        Severity = float(request.form['Severity'])
        BreathShortness = float(request.form[ 'BreathShortness' ])
        VisualChanges = float(request.form['VisualChanges'])
        NoseBleeding = float(request.form[ 'NoseBleeding'])
        Whendiagnoused = float(request.form[ 'Whendiagnoused'])
        Systolic = float(request.form['Systolic'])
        Diastolic = float(request.form['Diastolic'])
        ControlledDiet = float(request.form['ControlledDiet'])

        features_values=np.array([[Gender,History, Age, Patient,TakeMedication, Severity, BreathShortness, VisualChanges,
                              NoseBleeding, Whendiagnoused, Systolic, Diastolic, ControlledDiet]])

        #column_names = ['Gender', 'Age', 'Patient', 'Severity', 'BreathShortness', 'VisualChanges',
        #'NoseBleeding', 'whendiagnoused', 'Systolic', 'Diastolic', 'ControlledDiet']

        df = pd.DataFrame(features_values, columns=['Gender', 'Age','History', 'Patient','TakeMedication', 'Severity', 'BreathShortness', 'VisualChanges',
                            'NoseBleeding', 'Whendiagnoused', 'Systolic', 'Diastolic', 'ControlledDiet'])
        prediction = model.predict(df)
        (prediction[0])

        if prediction[0] == 0:
            result="NORMAL"
        elif prediction [0] == 1:
            result="HYPERTENSION (Stage-1)"
        elif prediction [0] == 2:
            result='HYPERTENSION (Stage-2)'
        else:
            result='HYPERTENSIVE CRISIS'
        print (result)
        text = "Your Blood Pressure stage is:"
    return render_template("Predict.html", prediction_text=text + result ) # Render the result on predict.html

if __name__ == '__main__':
   app.run(debug= True, port = 5000)