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
@app.route("/states/<id>", strict_slashes=False)
def display_states_cities():
    """displays states and cities"""
    states_all = storage.all(State).values()
    var = None

    if id is not None:
        for state in states_all:
            if state.id == id:
                var = state

    return render_template('9-states.html', states_all=states_all, var=var, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
