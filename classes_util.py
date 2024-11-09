###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Entries
#    1. Create
#    2. Read
#    3. Update
#    4. Delete
#    5. Move
# 2. Columns
#    1. Create
#    2. Read
#    3. Update
#    4. Delete
#    5. Move
###########################################################################################

# TODO : ADD IDS

#############
## ENTRIES ##
#############

# Define Entries
class Entry:
    # CREATE
    def __init__(self, name : str, content : str, column_name : str): # -> Entry
        self.name = name
        self.content = content
        self.column = column_name

    # GET (READ)
    def get_entry(self): # -> Entry
        return self
    
    # SET (UPDATE)
    def set_entry(self, entry_name : str, entry_content : str, entry_column : str) -> None:
        if (entry_name == ""):
            self.name = self.name
        else:
            self.name = entry_name
        if (entry_content == ""):
            self.content = self.content
        else:
            self.content = entry_content
        if (entry_column == ""):
            self.column = self.column
        else:
            self.column = entry_column

#############
## COLUMNS ##
#############
# Define Columns
class Column:
    # CREATE
    def __init__(self, name : str, content : str): # -> Column
        self.headerTop = "="*40
        self.name = name
        self.headerBottom = "="*40
        self.content = content
        self.footer = "="*40

    # GET (READ)
    def get_column(self): # -> Column
        return self

    # SET (UPDATE)
    def set_column(self, column_name: str) -> None:
        if (column_name == ""):
            self.name = self.name
        else:
            self.name = column_name
    
#####################
## LIST OPERATIONS ##
#####################

############
##  MOVE  ##
############
# MOVE ENTRY
def move_entry(container : list, entry_position : int, entry_destination : int) -> list:
    entry : Entry = container[entry_position]
    container.insert(entry_destination, entry)
    container.pop(entry_position)
    return container

# MOVE COLUMN
def move_column(container : list, column_position : int, column_destination : int) -> list:
    # 1, 2, 3 
    column : Column = container[column_position]
    container.insert(column_destination, column)
    # 1, 2, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 2, 3, 2
    container.pop(column_position)
    # 1, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 3, 2
    return container

##############
##  DELETE  ##
##############
# NON URGENT TODO : POLISH
# DELETE ENTRY
def delete_entry(container : list, entry_position) -> list:
    container.pop(entry_position)
    return container

# DELETE COLUMN
def delete_column(container : list, column_position) -> list:
    container.pop(column_position)
    return container