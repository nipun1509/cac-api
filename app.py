from flask import Flask, request
import random

app = Flask(__name__)

def mock_score():
    score = random.randint(0, 500)
    if score == 0:
        risk = "No risk, no treatment needed"
    elif score <= 100:
        risk = "Low risk, monitor"
    elif score <= 400:
        risk = "Moderate risk, consider treatment"
    else:
        risk = "High risk, treatment required"
    return score, risk

@app.route("/predict", methods=["POST"])
def predict():
    score, risk = mock_score()
    return {"score": score, "risk": risk}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
