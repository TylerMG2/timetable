from flask import Flask

# Create app
app = Flask(__name__)

import backend.shiftAPI

# Main index
@app.route("/")
def hello_world():
    return "Hello, World!"

# Import blueprints
#import shiftAPI