# coding: utf-8
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn import metrics
from flask import Flask, request, render_template
import pickle

app = Flask("__name__")

df_1=pd.read_csv("first_telc.csv")

q = ""

@app.route("/")
def loadPage():
	return render_template('home.html', query="")


@app.route("/", methods=['POST'])
def predict():
    
    '''
    SeniorCitizen
    MonthlyCharges
    TotalCharges
    gender
    Partner
    Dependents
    PhoneService
    MultipleLines
    InternetService
    OnlineSecurity
    OnlineBackup
    DeviceProtection
    TechSupport
    StreamingTV
    StreamingMovies
    Contract
    PaperlessBilling
    PaymentMethod
    tenure
    '''
    

    
    inputQuery1 = request.form.get('query1')
    inputQuery2 = request.form['query2']
    inputQuery3 = request.form['query3']
    inputQuery4 = request.form.get('query4')
    inputQuery5 = request.form.get('query5')
    inputQuery6 = request.form.get('query6')
    inputQuery7 = request.form.get('query7')
    inputQuery8 = request.form.get('query8')
    inputQuery9 = request.form.get('query9')
    inputQuery10 = request.form.get('query10')
    inputQuery11 = request.form.get('query11')
    inputQuery12 = request.form.get('query12')
    inputQuery13 = request.form.get('query13')
    inputQuery14 = request.form.get('query14')
    inputQuery15 = request.form.get('query15')
    inputQuery16 = request.form.get('query16')
    inputQuery17 = request.form.get('query17')
    inputQuery18 = request.form.get('query18')
    inputQuery19 = request.form['query19']

    model = pickle.load(open("model.sav", "rb"))
    
    data = [[inputQuery1, inputQuery2, inputQuery3, inputQuery4, inputQuery5, inputQuery6, inputQuery7, 
             inputQuery8, inputQuery9, inputQuery10, inputQuery11, inputQuery12, inputQuery13, inputQuery14,
             inputQuery15, inputQuery16, inputQuery17, inputQuery18, inputQuery19]]
    
    new_df = pd.DataFrame(data, columns = ['SeniorCitizen', 'MonthlyCharges', 'TotalCharges', 'gender', 
                                           'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService',
                                           'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',
                                           'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling',
                                           'PaymentMethod', 'tenure'])
    
    df_2 = pd.concat([df_1, new_df], ignore_index = True) 
    # Group the tenure in bins of 12 months
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]
    
    df_2['tenure_group'] = pd.cut(df_2.tenure.astype(int), range(1, 80, 12), right=False, labels=labels)
    #drop column customerID and tenure
    df_2.drop(columns= ['tenure'], axis=1, inplace=True)   
    
    print(df_2.columns)
    
    
    new_df__dummies = pd.get_dummies(df_2[['gender', 'Partner', 'Dependents', 'PhoneService',
           'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
           'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
           'Contract', 'PaperlessBilling', 'PaymentMethod','tenure_group']])

    
   
    
    single = model.predict(new_df__dummies.tail(1))
    probablity = model.predict_proba(new_df__dummies.tail(1))[:,1]
    
    if single==1:
        o1 = "This customer is likely to be churned!!"
        o2 = "Confidence: {}".format(probablity*100)
    else:
        o1 = "This customer is likely to continue!!"
        o2 = "Confidence: {}".format(probablity*100)
        
    return render_template('home.html', output1=o1, output2=o2, 
                            inputQuery1 = request.form.get('query1'),
                            inputQuery2 = request.form['query2'],
                            inputQuery3 = request.form['query3'],
                            inputQuery4 = request.form.get('query4'),
                            inputQuery5 = request.form.get('query5'),
                            inputQuery6 = request.form.get('query6'),
                            inputQuery7 = request.form.get('query7'),
                            inputQuery8 = request.form.get('query8'),
                            inputQuery9 = request.form.get('query9'),
                            inputQuery10 = request.form.get('query10'),
                            inputQuery11 = request.form.get('query11'),
                            inputQuery12 = request.form.get('query12'),
                            inputQuery13 = request.form.get('query13'),
                            inputQuery14 = request.form.get('query14'),
                            inputQuery15 = request.form.get('query15'),
                            inputQuery16 = request.form.get('query16'),
                            inputQuery17 = request.form.get('query17'),
                            inputQuery18 = request.form.get('query18'),
                            inputQuery19 = request.form['query19'])
    
if __name__ == '__main__':
    app.debug = True   
    app.run()

