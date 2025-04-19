from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model.joblib")
species = ["setosa", "versicolor", "virginica"]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = data.get("features")
    if features is None:
        return jsonify({"error": "features not provided"}), 400
    X = np.array(features).reshape(1, -1)
    prediction = model.predict(X)[0]
    predicted_class = species[int(prediction)]
    return jsonify({"prediction": predicted_class})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
