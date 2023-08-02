# Imports
import uuid
from task import Task
from datetime import date

# Class that represents a given shift
class Shift:

    # Member vars
    id : str
    start : date
    end : date
    tasks : [Task]