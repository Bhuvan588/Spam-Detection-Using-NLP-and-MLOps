import pytest
from app import app
import pickle


@pytest.fixture
def client():

    app.config['TESTING'] =  True

    with app.test_client() as client:

        yield client



def test_index(client):

    #Testing the home or index route to ensure its successfull working

    response = client.get('/')
    assert response.status_code==200
    assert b"Spam Email Detection" in response.data


#Testing predict route when the email content is classified as spam

def test_predict_spam(client, monkeypatch):

    def mock_model_predict(features):

        return [1] # 1 output means spam
    
    def mock_vectorizer_transform(text):

        return text
    
    monkeypatch.setattr('app.model.predict', mock_model_predict)
    monkeypatch.setattr('app.vectorizer.transform', mock_vectorizer_transform)


    #Sending a POST request to the /predict route with email content
    response =  client.post('/predict', data = {'extracted_text': 'Hi, you can win free money now!!'})

    assert response.status_code ==200
    assert b"Prediction: Spam" in response.data



#Testing predict route when email is classified as non-spam

def test_predict_ham(client, monkeypatch):

    def mock_model_predict(features):

        return [0] #0 means not spam / ham
    

    def mock_vectorizer_transform(text):

        return text
    
    monkeypatch.setattr('app.model.predict', mock_model_predict)
    monkeypatch.setattr('app.vectorizer.transform', mock_vectorizer_transform)

    #Sending a POST request to the /predict route with email content
    response =  client.post('/predict', data = {'extracted_text': 'This is regarding your job application.'})

    assert response.status_code ==200
    assert b"Prediction: Not Spam" in response.data

