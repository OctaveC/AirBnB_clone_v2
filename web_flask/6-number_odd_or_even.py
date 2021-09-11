#!/usr/bin/python3
"""
Launches Flask Web App
"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hi_hbnb():
    """ hbnb page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def lone_hbnb():
    """ lone hbnb """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Prints C text """
    return 'C {}'.format(text).replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """ Prints Python text """
    return 'Python {}'.format(text).replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Print if n is an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ number template """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """ displays odd or even num """
    if n % 2 != 0:
        evenorodd = "odd"
    else:
        evenorodd = "even"
    return flask.render_template('6-number_odd_or_even.html', n=n,
                                 evenorodd=evenorodd)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
