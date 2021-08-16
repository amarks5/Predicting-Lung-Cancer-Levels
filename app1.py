from flask import Flask, render_template, request, session, url_for, redirect, jsonify
import numpy as np
import pandas as pd
import pickle
import pymysql

app = Flask(__name__)
model = pickle.load(open("cancer_detector.pickle", "rb"))

#Database Connection
def dbConnection():
    connection = pymysql.connect(host="localhost", user="postgres", password="Ali176150", database="cancerdata")
    return connection


#default welcome page
@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=["GET","POST"])
def predict():
     
        if request.method == "POST":
            v1 = request.form.get("para1")
            v2 = request.form.get("para2")
            v3 = request.form.get("para3")
            v4 = request.form.get("para4")
            v5 = request.form.get("para5")
            v6 = request.form.get("para6")
            v7 = request.form.get("para7")
            v8 = request.form.get("para8")
            v9 = request.form.get("para9")
            v10 = request.form.get("para10")
            v11 = request.form.get("para11")
            v12 = request.form.get("para12")
            v13 = request.form.get("para13")
            v14 = request.form.get("para14")
            v15 = request.form.get("para15")
            v16 = request.form.get("para16")
            v17 = request.form.get("para17")
            v18 = request.form.get("para18")
            v19 = request.form.get("para19")
            v20 = request.form.get("para20")
            v21 = request.form.get("para21")
            v22 = request.form.get("para22")
            v23 = request.form.get("para23")


            test_list = []
            valofall = v1 + ',' + v2 + ',' + v3 + ',' + v4 + ',' + v5 + ',' + v6 + ',' + v7 + ',' + v8 + ',' + v9 + ',' + v10 + ',' + v11 + ',' + v12 + ',' + v13 + ',' + v14 + ',' + v15 + ',' + v16 + ',' + v17 + ',' + v18 + ',' + v19 + ',' + v20 + ',' + v21 + ',' + v22 + ',' + v23 
    
            print(valofall)
            valofsplit = valofall.split(",")
            print(valofsplit)
            for i in range(0, len(valofsplit)):
                test_list.append(int(valofsplit[i]))
                # print(test_list)
            # X_std = scaler.fit_transform(X)
            print(test_list)
            print(np.array([test_list]))
            loaded_model = pickle.load(open("cancer_detector.pickle", 'rb'))
            y_gotdata = loaded_model.predict(np.array([test_list]))
            print(y_gotdata[0])
            class_obt={1:'low',2:'medeium',3:'high'}
            print("predicted cancer is " + class_obt.get(y_gotdata[0]))
            result = class_obt.get(y_gotdata[0])
            
        return render_template('predict.html', result=result)


if __name__ == '__main__':
    app.run(debug=True,port=5000)
