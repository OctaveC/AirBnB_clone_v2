#!/usr/bin/python3
"""
Launches Flask Web App
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def filters(id=None):
    """ Displays an HTML page for filters """
    stuff = storage.all(State)
    states = []

    for ite in stuff:
        states.append(stuff[ite])

    stuff = storage.all(Amenity)
    amenities = []

    for ite in stuff:
        amenities.append(stuff[ite])

    return render_template('10-hbnb_filters.html', states=states,
        amenities=amenities)

@app.teardown_appcontext
def teardown_data(self):
    """ Closes SQALchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
