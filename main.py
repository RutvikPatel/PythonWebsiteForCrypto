from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/prices")
def prices():
    return render_template("prices.html")


if __name__ == "__main__":
    app.run(debug=True)