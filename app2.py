import numpy as np
from flask import Flask, request, render_template
import spacy

app = Flask(__name__)
nlp = spacy.load('model5')

@app.route('/')
def home_page():
    return render_template('index3.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    
    resume_text = request.form['Resume_text']
    
    doc = nlp(resume_text)
    result = []
    
    for ent in doc.ents:
        result.append(str(ent.label_.upper())+"   --    " +str(ent.text))
        
        #print(f'{ent.label_.upper():{30}} - {ent.text}')
    
    return render_template('result.html', results=result)
    #return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(final_features))


if __name__ == "__main__":
    app.run(debug=True)
    # -*- coding: utf-8 -*-

