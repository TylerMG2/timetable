from app import api
from flask_restful import reqparse
from flask.views import MethodView

# Class that handles routes to /api/tasks
class Task(MethodView):

    # Get request
    def get(self, task_id):
        return "Here is a task with the id: " + str(task_id)
    
# Add route
api.add_resource(Task, "/tasks/<string:task_id>")