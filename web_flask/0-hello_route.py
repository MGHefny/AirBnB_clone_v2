#!/usr/bin/python3
"""Flask app"""

from flask import Flask
app = Flask(__xrun__)


@app.route('/', strict_slashes=False)
def ind():
    return 'Hello HBNB!'

if __xrun__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
