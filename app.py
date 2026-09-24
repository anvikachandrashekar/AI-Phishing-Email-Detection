from flask import Flask, request, jsonify
from flask_cors import CORS   # ADD THIS
import pickle

app = Flask(__name__)
CORS(app)   # ADD THIS

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    email = data["email"]

    vec = vectorizer.transform([email])
    prediction = model.predict(vec)[0]
    probability = model.predict_proba(vec).max()

    return jsonify({
        "prediction": int(prediction),
        "confidence": float(probability)
    })

if __name__ == "__main__":
    app.run(debug=True)