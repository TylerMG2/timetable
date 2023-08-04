from flask import Flask
from flask_restful import Api

# Create app
application = Flask(__name__)
api = Api(application)

# Import routes
import app.route.shift
import app.route.site
import app.route.task
import app.route.workplace