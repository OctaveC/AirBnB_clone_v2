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


@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list_id(id=None):
    """ Displays an HTML page that has a list of states """
    data = []
    states = storage.all(State)
    if id is None:
        for ite in states:
            data.append(states[ite])
    else:
        id = 'State.' + id
        data = states.get(id)
    return render_template('9-states.html', states=data, id=id)
    return render_template('9-states.html', state=id)


@app.teardown_appcontext
def teardown_data(self):
    """ Closes SQALchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
