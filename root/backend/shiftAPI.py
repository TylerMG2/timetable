from backend import app

# Get shift at given workplace
@app.route("/shifts")
def get_shifts():
    return "Heres some shifts"