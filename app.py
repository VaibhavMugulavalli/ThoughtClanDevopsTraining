from flask import Flask, request, render_template
import pandas as pd
import joblib
import os

app = Flask(__name__)
MODEL_PATH = "model.pkl"
ENCODER_PATH = "credit_history_encoded.pkl"

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

def load_encoder():
    if os.path.exists(ENCODER_PATH):
        return joblib.load(ENCODER_PATH)
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    inputs = None

    if request.method == "POST":
        inputs = {
            'credit_history': request.form['credit_history'],
            'credit_amount': float(request.form['credit_amount']),
            'age': float(request.form['age']),
            'existing_credits': int(request.form['existing_credits'])
        }

        df = pd.DataFrame([inputs])
        encoder = load_encoder()
        df['credit_history'] = encoder.transform(df['credit_history'])

        model = load_model()
        prediction = model.predict(df)[0]

    return render_template("index.html", prediction=prediction, inputs=inputs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)

