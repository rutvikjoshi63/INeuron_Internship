import json
import pickle
from flask import Flask, request,app,jsonify,url_for,render_template,redirect
import numpy as np
import pandas as pd
import os 
from mlProject.pipeline.prediction import PredictionPipeline

app = Flask(__name__)
# Load model

# regmodel = pickle.load(open('regmodel.pkl','rb'))
# scalar = pickle.load(open('scaling.pkl','rb'))

@app.route('/',methods = ['GET',"POST"])
def home():
    if request.method=="GET":
        return render_template('form2.html')
    # else:
    #     return redirect(url_for("predict"))
@app.route('/Modeltwo',methods = ['GET',"POST"])
def Modeltwo():
    if request.method=="GET":
        return render_template('Model2.html')
    elif request.method=="POST":
        return redirect(url_for("train"))
    
@app.route('/train',methods = ['GET',"POST"])
def train():
    print('Inside Training')
    if request.method=="GET":
        os.system('python main.py')
        return "Training succeddful"

@app.route('/predict_two',methods=['POST','GET']) # route to show the predictions in a web UI
def predict_two():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            cement =float(request.form['cement'])
            blast_furnace_slag =float(request.form['blast_furnace_slag'])
            fly_ash =float(request.form['fly_ash'])
            water =float(request.form['water'])
            superplasticizer =float(request.form['superplasticizer'])
            coarse_aggregate =float(request.form['coarse_aggregate'])
            fine_aggregate =float(request.form['fine_aggregate'])
            age =int(request.form['age'])
            # pH =float(request.form['pH'])
            # sulphates =float(request.form['sulphates'])
            # alcohol =float(request.form['alcohol'])
            data = [cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age]
            data = np.array(data).reshape(1, 8)
            
            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template('results.html', prediction = str(predict))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('Model2.html')


# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     data = request.json['data']
#     print(data)
#     print(np.array(list(data.values())).reshape(1,-1))
#     new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
#     output=regmodel.predict(new_data)
#     print(output[0])
#     return jsonify(output[0])

@app.route('/predict', methods=["GET",'POST'])
def predict():
    if request.method=="GET":
        return render_template('home.html')
    # else:
    #     data=[float(x) for x in request.form.values()]
    #     final_input = scalar.transform(np.array(data).reshape(1,-1))
    #     print(final_input)
    #     output = regmodel.predict(final_input)[0]
    #     return render_template("home.html", prediction_text="The House price prediction is {}".format(output))


if __name__=='__main__':
    app.run(host="0.0.0.0",port = 8080,debug=True)