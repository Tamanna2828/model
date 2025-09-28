from flask import Flask,render_template,request
import joblib
import pandas as pd
app= Flask(__name__)

model=joblib.load("marks_model.pkl")



@app.route('/',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def add():
    return render_template('add.html')

@app.route('/predictmarks',methods=['POST'])
def addData():
    h= float(request.form['hours'])
    att= float(request.form['attendance'])
    input=pd.DataFrame([[h,att]],columns=["study_hours","attendance"])
    marks=model.predict(input)[0]
    marks= round(marks,2)
    return render_template('show.html',hours=h,attendance=att,marks=marks)

@app.route('/list',methods=['GET'])
def show_list():
    return 'data delivered'

if __name__=='__main__':
   app.run(debug=True)