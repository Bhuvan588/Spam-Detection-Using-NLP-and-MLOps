from flask import Flask, render_template, request, jsonify
import pickle
from sklearn.feature_extraction.text import CountVectorizer


app = Flask(__name__)


#Here we load the model and the vectorizer
model = pickle.load(open('models/model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizers/vectorizer.pkl', 'rb'))


#Defining the routes
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict():

    try:

        extracted_text =  request.form['extracted_text']

        #Transforming text into numerical data through vectorizer
        features = vectorizer.transform([extracted_text])

        #Prediction
        prediction = model.predict(features)

        output='prediction_value'

        #Ham-> 0 , Spam -> 1
        if prediction[0]==1:
            output = 'Spam'
        else:
            output='Not Spam'

        
        return render_template('index.html', prediction_text = f'Prediction: {output}')
    
    except Exception as e:

        return jsonify({'error': str(e)})


if __name__ =='__main__':
    app.run(debug=True)