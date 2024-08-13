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

if __name__ == "__main__":
    # Example usage
    user_input = input("Enter the text for prediction: ")
    
    result = predict(user_input)
    if result is not None:
        print(f"Prediction: {result}")