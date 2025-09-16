from flask import Flask, render_template, request
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from predict import predict_life_expectancy
from utils import normalize_input
from predict import load_model

app = Flask(__name__)
model, feature_names = load_model()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = request.form.to_dict()
        cleaned_input = normalize_input(input_data)
        prediction = predict_life_expectancy(cleaned_input)
        return render_template('result.html', prediction=round(prediction, 2))
    
    return render_template('index.html', features=feature_names)

if __name__ == '__main__':
    app.run(debug=True)
