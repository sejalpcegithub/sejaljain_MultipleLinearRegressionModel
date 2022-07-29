import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle


app = Flask(__name__)
model = pickle.load(open('linearregression.pkl','rb')) 

@app.route('/')
def home():
  
    return render_template("index5.html")
  
@app.route('/predict',methods=['GET'])

def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''
    exp1 = int(request.args.get('exp1'))
    exp2 = int(request.args.get('exp2'))
    exp3 = int(request.args.get('exp3'))
    exp4 = int(request.args.get('exp4'))
    exp5 = int(request.args.get('exp5'))
    exp6 = int(request.args.get('exp6'))
    exp7 = int(request.args.get('exp7'))
    


    
    prediction = model.predict([[exp1,exp2,exp3,exp4,exp5,exp6,exp7]])
    
        
    return render_template('index5.html', prediction_text='predicted price for given condition is : {}'.format(prediction))


if __name__ == "__main__":
    app.run(debug=True)