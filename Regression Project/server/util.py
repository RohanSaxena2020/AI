import json
import pickle
from sklearn.linear_model import LinearRegression

def load_model():
    # Load the pre-trained model
    with open('artifacts/scoring_avg_model.pickle', 'rb') as f:
        model = pickle.load(f)
    return model

def load_columns():
    # Load the model columns
    with open('artifacts/columns.json', 'r') as f:
        data = json.load(f)
        columns = data['data_columns']  # Accessing the list correctly
    return columns

def predict_scoring_average(model, input_data):
    columns = load_columns()
    # Ensure input data is in the correct order as expected by the model
    input_vector = [input_data[col] for col in columns]
    prediction = model.predict([input_vector])
    return prediction[0]

