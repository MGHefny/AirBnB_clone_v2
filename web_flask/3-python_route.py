#!/usr/bin/python3
"""Flask app"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def ind():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def cfun(text):
    return "C" + text.replace("_", " ")


@app.route("/python/<text>", strict_slashes=False)
def pythcool(text="is cool"):
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
