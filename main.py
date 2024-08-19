import os
from flask import Flask, jsonify, request
from datetime import datetime
import numpy as np
import json
import joblib


model = joblib.load("scam_detection_model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

def preprocess_input(text):
    # You can add any necessary preprocessing steps here
    return text

def predict(text):
    # Preprocess the input text
    preprocessed_text = preprocess_input(text)

    # Transform the preprocessed text using the vectorizer
    vectorized_text = vectorizer.transform([preprocessed_text])

    # Make a prediction using the model
    prediction = model.predict(vectorized_text)

    return prediction[0]

class Record:
    def __init__(self, status, name, text, date):
        self.status = status
        self.name = name
        self.text = text
        self.datee = date

    def to_dict(self):
        print(type(self.name))
        return {
            'name': self.name,
            'status': self.status,
            'text': self.text,
            'date': self.datee.isoformat()  # Convert date to a string
        }

# Create a list of Record objects
records = [
    Record(1, 'Alice', 'lerem ipsum dolor sit amet', datetime.now()),
]

# Convert records to a list of dictionaries
def records_dict():
    return [record.to_dict() for record in records]

app = Flask(__name__)

@app.route("/")
def hello_world():
  """Example Hello World route."""
  name = os.environ.get("NAME", "World")
  return 'Welcome to scam detector'

@app.route('/history')
def get_history():
    item = request.get_data
    return jsonify(records_dict()), 200

@app.route('/test', methods=['POST'])
def update_itemb():
    item = request.json
    status = predict(item['text'])
    records.append(Record(int(status), item['name'], item['text'], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print(records.__len__())
    return json.dumps({"status":  str(status)  }), 200

if __name__ == "__main__":
  app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))