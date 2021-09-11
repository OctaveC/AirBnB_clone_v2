#!/usr/bin/python3
"""
Launches Flask Web App
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hi_hbnb():
    """ hbnb page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def lone_hbnb():
    """ lone hbnb """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
