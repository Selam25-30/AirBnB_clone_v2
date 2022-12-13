#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask, escape
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_Hbnb():
    """Return a string at the root route"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Return a string at the /hbnb route"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def message(text):
    """Return a string at the /c/<text> route"""
    new_str = text.replace('_', ' ')
    return "C %s" % escape(new_str)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>")
def pythoniscool(text="is cool"):
    """Retun string at the /python route with default
    string "is cool" or at the /python/<text> route
    """
    new = text.replace('_', ' ')
    return "Python %s" % escape(new)


@app.route("/number/<int:n>")
def integernumber(n):
    """Return string at /number/<int:n> route"""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host='0.0.0.0')
