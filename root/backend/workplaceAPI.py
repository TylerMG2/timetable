from backend import app

# setting up a basic workplace, "Dont know if this is exactly what you wanted @TylerMG2"
@app.route("/workplace/<id>")
def get_workplace(id: str):
    return "Here is a workplace with the id: " + id