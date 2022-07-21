#!/usr/bin/env python
# coding: utf-8

# In[3]:
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
from dtreeviz.trees import dtreeviz

app = Flask(__name__)
model = pickle.load(open("model.pkl", 'rb'))


# In[9]:


@app.route('/')
def home():
    return render_template('index.html')

# In[16]:

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    value = None
    if request.method == 'POST':
        submit_button_1 = request.form.get('submit_button_1', None)
        submit_button_2 = request.form.get('submit_button_2', None)
        if submit_button_1:
#             int_features = [x for x in request.form.values() if request.form.values()!="Prediction" if request.form.values()!="Visualisation"]
            age = request.form.get("age")
            avg_glucose_level = request.form.get("avg_glucose_level")
            bmi = request.form.get("bmi")
            gender = request.form.get("gender")
            hypertention = request.form.get("hypertention")
            heart_disease = request.form.get("heart_disease")
            ever_married = request.form.get("ever_married")
            work_type = request.form.get("work_type")
            residence_type = request.form.get("residence_type")
            smoking_status = request.form.get("age")
            
            int_features = [age, avg_glucose_level,bmi, gender,hypertention,heart_disease,ever_married,work_type,residence_type,smoking_status]                  
            final_features = [np.array(int_features)]
            prediction = model.predict(final_features)
            output = round(prediction[0], 2)
            positive_percent= model.predict_proba(final_features)[0][0]*100;
            positive_percent= int(positive_percent)  
            if output==0 :
                return render_template('index.html', prediction_text='"Probability that you can have stroke is {}%"'.format(positive_percent))
            elif output==1 :
                return render_template('index.html', prediction_text='"you cannot have stroke"')
        elif submit_button_2:
            age = request.form.get("age")
            avg_glucose_level = request.form.get("avg_glucose_level")
            bmi = request.form.get("bmi")
            gender = request.form.get("gender")
            hypertention = request.form.get("hypertention")
            heart_disease = request.form.get("heart_disease")
            ever_married = request.form.get("ever_married")
            work_type = request.form.get("work_type")
            residence_type = request.form.get("residence_type")
            smoking_status = request.form.get("age")
            int_features = [age, avg_glucose_level,bmi, gender,hypertention,heart_disease,ever_married,work_type,residence_type,smoking_status]                  
            final_features = [np.array(int_features)]
            prediction = model.predict(final_features)
            output = round(prediction[0], 2)
            df1=pd.read_csv("C:/Users/Hp/ML Algorithm Visualiser/Encoded_data.csv")
            x = df1.drop(columns = ['stroke'])
            y = df1['stroke']
            fn=['gender','age','hypertension','heart_disease','ever_married','work_type','Residence_type','avg_glucose_level','bmi','smoking_status']
            cn=[1,0]
            viz = dtreeviz(model.estimators_[0],x,y,target_name="stroke",feature_names=fn,class_names=list(cn),title="1st decision tree")
            viz.save("static/images/Visualisation2.svg")
            return render_template('visualisation.html',visualisation_text="RANDOM FOREST")
            

# In[18]:
if __name__ == "__main__":
    app.run(debug=True)

