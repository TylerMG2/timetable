from backend import app

# setting up a basic workplace, "Dont know if this is exactly what you wanted @TylerMG2"
@app.route("/workplace")
def get_workplaces():
    return "These are some workplaces!!"