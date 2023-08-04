from app import api
from flask_restful import reqparse
from flask.views import MethodView

# Class that handles routes to /api/sites
class Site(MethodView):

    # Get request
    def get(self, site_id):
        return "Here is a site with the id: " + str(site_id)

# Add route
api.add_resource(Site, "/sites/<string:site_id>")