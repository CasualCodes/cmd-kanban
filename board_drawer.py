###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Board Drawer - An Ascii Display of the Board containing all entries
#    1. Text Wrapping - All stored text have wrapping
#       1. How it works: All inputted text are divided into chunks seperated by a new line
#    2. Four Columns - Research, Planning, Doing, Done
#       1. Optional: Customize Column Count
###########################################################################################
from classes_util import Column, Entry

# Text Wrapping
def text_wrap(text : str) -> str:
    text_limit = 30
    # If text limit is reached, divide, and append \n
    pass

# Display A Column
# TODO: INDEXING
def display_column(column : Column, entries : list) -> None:
    print(column.headerTop)
    print(column.name)
    print(column.headerBottom)
    display_entries(column.name, entries)
    print(column.footer)

def display_entries(column_name : str, entries : list) -> None:
    for entry in entries:
        print(entry.name)
        # print(entry.content)

def display_defaults(defaults : int) -> None:
    pass

# Generate Each Default Column
#   Research
#   Planning
#   Doing
#   None
def generate_defaults(defaults : int) -> str:
    pass

