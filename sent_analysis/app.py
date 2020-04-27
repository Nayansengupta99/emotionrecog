import tweepy
from textblob import TextBlob
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == "POST":
        b = request.form["a"]
        p=TextBlob(b).sentiment.polarity

    return render_template("result.html", p=p)


if __name__ == "__main__":
    app.run(debug=True)
