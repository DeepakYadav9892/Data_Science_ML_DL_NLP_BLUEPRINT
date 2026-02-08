import pickle
from flask import Flask,request,jsonify,render_template
import numpy as np 
import pandas as pd
application=Flask(__name__)
app=application

##import ridge regression and standard pickle 

ridge_model=pickle.load(open('models/ridge.pkl','rb'))

standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/predictdata',methods=['GET','POST'])

def predict_datapoint():
    if request.method=="POST":
        # Get values from form (9 features)
            Temperature = float(request.form.get('Temperature'))
            RH = float(request.form.get('RH'))
            Wind = float(request.form.get('Wind'))
            Rain = float(request.form.get('Rain'))
            FFMC = float(request.form.get('FFMC'))
            DMC = float(request.form.get('DMC'))
            ISI = float(request.form.get('ISI'))
            BUI = float(request.form.get('BUI'))
            FWI = float(request.form.get('FWI'))

            new_data_scaled=standard_scaler.transform([[Temperature,RH,Wind,Rain,FFMC,DMC,ISI,BUI,FWI]])
            result=ridge_model.predict(new_data_scaled)

            return render_template('home.html',results=result[0])





    else:
        return render_template('home.html')
if __name__=="__main__":
    app.run(host="0.0.0.0")