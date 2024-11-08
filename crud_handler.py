###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 2. CRUD Handler - Editing Entries/Columns, Adding New Entries/Columns, Moving Entries/Columns, and Deleting Entries/Columns
#    1. Create Entries
#    2. Read Entries
#    3. Update Entries
#    4. Delete Entries
#    5. Move Entries
#    6. 1-5 but for Columns
###########################################################################################
from classes_util import Column
from classes_util import Entry

#############
## ENTRIES ##
#############

# Create Entries
# TODO: INDEXING [DONE]
# TODO: CRUD PROPER
def create_entry(name : str, content : str, column_name : str):
    entry = Entry(name, content, column_name)
    return entry

# Read Entries
def read_entry(column : int, index : int):
    return

# Update Entries
def update_entry(column : int, index : int, text : str):
    pass

# Delete Entries
def delete_entry(column : int, index : int):
    # POP
    # GET ENTRY LIST, THEN POP SELF (INDEX)
    pass

# Move Entries
def move_entry(column : int, index : int, columnTo : int):
    pass

# Save Entries - Save the entry contents on the file
def save_entries():
    pass

# Parse Entries - Parse the text file contents through board_drawer
def parse_entries():
    pass

#############
## COLUMNS ##
#############

# Create Columns
# TODO: INDEXING [DONE?]
def create_column(name : str, content : str = ""):
    column = Column(name, content)
    return column

# Read Column
def read_column(column : int, index : int):
    return

# Update Column
def update_column(column : int, index : int, text : str):
    pass

# Delete Column
def delete_column(column : int, index : int):
    # POP
    # GET COLUMN LIST, THEN POP SELF (INDEX)
    pass

# Move Column
def move_column(column : int, index : int, columnTo : int):
    pass

# Save Columns - Save the entry contents on the file
def save_columns():
    pass

# Parse Columns - Parse the text file contents through board_drawer
def parse_columns():
    pass