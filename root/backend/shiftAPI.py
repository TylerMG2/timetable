from flask import request
from backend import app

# Return all the shifts in a workplace
@app.route("/shifts/<id>")
def get_shifts(id: str):
    return "Heres some shifts from the workplace with the id: " + id 

# Add a shift to the database
@app.route("/shifts", methods=['POST'])
def add_shift():
    details = request.get_json()
    return "Adding the shift with the details: " + details

# Get the details about a specific shift
@app.route("/shift/<id>")
def get_shift(id: str):

    # Return the shift
    return "Here is the shift with the id: " + id

# Update a shifts details
@app.route("/shift/<id>", methods=['POST'])
def get_shift(id: str):

    # Get the new shifts details
    details = request.get_json()

    # Return the shift
    return "Here is the shift with the id: " + id
