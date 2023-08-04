from app import api
from flask_restful import reqparse
from flask.views import MethodView

# Class that handles routes to /api/workplaces
class Workplace(MethodView):

    # Get request
    def get(self, workplace_id):
        return 'Here is a workplace with the id: ' + str(workplace_id)
    
# Add route
api.add_resource(Workplace, '/workplaces/<string:workplace_id>')