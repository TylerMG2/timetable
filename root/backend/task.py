# Imports
import uuid

### TODO
# - Add task return types (like the task expects a value to be input or a image)

# Class that represents a user task (Can be global or in a shift)
class Task:

    # Member vars
    id          : str
    title       : str
    description : str
    done        : bool = False

    # Init class
    def __init__(self, title : str, description : str) -> None:

        # Create new id
        self.id          = uuid.uuid4().hex

        # Set member vars
        self.title       = title
        self.description = description
    
    # Set task to complete
    def complete(self) -> None:
        self.done = True
