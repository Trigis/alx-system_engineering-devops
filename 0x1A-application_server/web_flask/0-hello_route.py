#!/usr/bin/python3
"""
Starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

@app.route('/airbnb-onepage/', strict_slashes=False)
def airbnb_onepage():
    """Display 'AirBnB Clone onepage'"""
    return 'AirBnB Clone onepage'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
