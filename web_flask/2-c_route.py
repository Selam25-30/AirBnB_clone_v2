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


if __name__ == "__main__":
    app.run(host='0.0.0.0')
