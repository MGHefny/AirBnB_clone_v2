#!/usr/bin/python3
"""Flask app"""

from flask import Flask, render_template
from models import storage
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    stat = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', stat=stat)


@app.teardown_appcontext
def db_dow(exception):
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
