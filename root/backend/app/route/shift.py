from app import api
from flask_restful import reqparse
from flask.views import MethodView

# Class that handles routes to /api/shifts
class Shift(MethodView):

    # Get request
    def get(self, shift_id):
        return "Here is a shift with the id: " + str(shift_id)

# Add route
api.add_resource(Shift, "/shifts/<string:shift_id>")