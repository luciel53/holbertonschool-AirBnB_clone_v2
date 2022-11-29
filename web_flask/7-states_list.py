#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


# Declare a method to handle @app.teardown_appcontext
@app.teardown_appcontext
def close(self):
    storage.close()

@app.route('/states_list', strict_slashes=False)
def display_states(self):
    all_states = self.storage.all(State)
    return render_template('7-states.html', all_states=all_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
