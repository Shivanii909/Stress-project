from flask import Flask, render_template, request
import pickle
import os

# Optional: memory issue avoid
os.environ["OMP_NUM_THREADS"] = "1"

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input values from form
        data = [float(x) for x in request.form.values()]

        # Predict
        prediction = model.predict([data])[0]

        # Convert result
        if prediction == 0:
            result = "Low Stress"
        elif prediction == 1:
            result = "Moderate Stress"
        else:
            result = "High Stress"

    except:
        result = "Invalid Input ❌"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)