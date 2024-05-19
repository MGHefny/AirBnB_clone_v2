#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def ind():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cfun(text):
    return "C " + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def pythcool(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def inumb(n):
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbtemp(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
