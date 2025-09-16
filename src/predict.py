import joblib
import numpy as np

MODEL_PATH = 'models/life_expectancy_model.pkl'

def load_model():
    model, feature_names = joblib.load(MODEL_PATH)
    return model, feature_names

def predict_life_expectancy(input_dict):
    model, feature_names = load_model()
    
    input_data = np.array([input_dict[feature] for feature in feature_names]).reshape(1, -1)
    
    prediction = model.predict(input_data)[0]
    return round(prediction, 2)
