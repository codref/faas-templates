#!/usr/bin/env python
from flask import Flask
from flask_cors import CORS
from waitress import serve

# we instantiate Flask first, to support future blueprinting
app = Flask(__name__)
CORS(app)

# We then load our function handler
from function import handler

# Start wsgi application through Waitress server
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=5000)
