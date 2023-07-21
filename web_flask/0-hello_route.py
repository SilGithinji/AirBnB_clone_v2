#!/usr/bin/python3
"""To start a Flask web application

It listens on 0.0.0.0, port 5000.
Routes:
    /: To display 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
