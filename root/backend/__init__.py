from flask import Flask, request

# Create app
app = Flask(__name__)

# Import views
import backend.shiftAPI
import backend.workplaceAPI

# Main index
@app.route("/")
def hello_world():
    return "Hello, World!"