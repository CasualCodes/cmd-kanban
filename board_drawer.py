###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Board Drawer - An Ascii Display of the Board containing all entries
#    1. Text Wrapping - All stored text have wrapping
#       1. How it works: All inputted text are divided into chunks seperated by a new line
#    2. Four Columns - Research, Planning, Doing, Done
#       1. Optional: Customize Column Count
###########################################################################################

# Text Wrapping
def text_wrap(text : str) -> str:
    text_limit = 30
    # If text limit is reached, divide, and append \n
    pass

# Define Columns
class Column:
    def __init__(self, name : str, content : str):
        self.headerTop = "="*40
        self.name = name
        self.headerBottom = "="*40
        self.content = content
        self.footer = "="*40

# Display A Column
def display_column(columns : int) -> None:
    pass

def display_defaults(defaults : int) -> None:
    pass

# Generate Each Default Column
#   Research
#   Planning
#   Doing
#   None
def generate_defaults(defaults : int) -> str:
    pass

