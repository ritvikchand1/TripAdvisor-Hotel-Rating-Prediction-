from flask import Flask, render_template, request
import ml

app = Flask(__name__)

@app.route("/")
def render_home():
   return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST": 
        print(request.method)
        review_text = request.form.get("review-content")

        # predictions
        pred_rating = ml.pred(review_text)
        return render_template("index.html", rating = pred_rating)
    else:
        print(request.method)
        return render_template("index.html", rating = 0)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8080, debug=True)