from flask import *
import pickle
import os
import pandas as pd
import sklearn
import numpy as np
app = Flask(__name__) #creating the Flask class object   
 
@app.route('/pred',methods = ['GET','POST']) #decorator drfines the   
def home(): 
    homepage_featured=request.form['homepage_featured']  
    food_type=request.form['food_type'] 
    model = pickle.loads(open('fdemand.pkl','rb').read())
    features = [1 for x in request.form.values()]
    feature_value = [np.array(features)]
    prediction = model.predict(feature_value)
    output = prediction[0]
    
    return "The Number of Orders is : "+str(output)
    
if __name__ =='__main__':  
    app.run(debug = True)  