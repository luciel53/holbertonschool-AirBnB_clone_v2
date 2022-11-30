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


@app.route('/states', strict_slashes=False)
def display_states():
    """displays states"""
    states = storage.all(State)
    return render_template('9-states.html', all_states=states)

@app.route('/states/<id>', strict_slashes=False)
def display_state_id():
    """displays id states"""
    states_id = storage.all(State)

    for state in states_id:
        if state.id == states_id:
            return render_template('9-states.html', states_id=states_id)
        else:
            return render_template('9-states.html', n_found=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
