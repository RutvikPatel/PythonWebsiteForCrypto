from flask import Flask, render_template, request
import bitcoin


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/prices")
def prices():
    latest_price = bitcoin.get_price()
    return render_template("prices.html", live_prices=latest_price)


if __name__ == "__main__":
    app.run(debug=True)