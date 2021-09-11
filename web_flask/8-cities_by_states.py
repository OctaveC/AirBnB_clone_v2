#!/usr/bin/python3
"""
Launches Flask Web App
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays an HTML page that has a list of states """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_data(self):
    """ Closes SQALchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
