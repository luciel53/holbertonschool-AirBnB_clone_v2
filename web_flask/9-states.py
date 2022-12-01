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


@app.route("/states", strict_slashes=False)
def display_state():
    """displays states"""
    all_states = storage.all(State)
    return render_template('7-states_list.html', all_states=all_states)


@app.route("/states/<id>", strict_slashes=False)
def display_states_cities(id):
    """displays states and cities"""
    all_states = storage.all(State).values()

    for state in all_states:
        if state.id == id:
            return render_template('9-states.html', state=state,
                                   s_cities=state.cities)
    return render_template('9-states.html', nf=True)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
