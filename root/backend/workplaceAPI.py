from flask import request
from backend import app

# Add a workplace
@app.route("/workplaces", methods=['POST'])
def add_workplace():
    details = request.get_json()
    return "Editing the workplace with the id: " + id

# Get a workplace by id
@app.route("/workplace/<id>")
def get_workplace(id: str):
    return "Here is a workplace with the id: " + id

# Edit a workplace by id
@app.route("/workplace/<id>", methods=['POST'])
def edit_workplace(id: str):
    details = request.get_json()
    return "Editing the workplace with the id: " + id