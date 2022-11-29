#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session: """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_cities_by_states():
    """displays states"""
    all_states = storage.all(State)
    return render_template('8-cities_by_states', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
