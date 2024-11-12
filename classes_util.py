###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Entries
#    1. Create
#    2. Read
#    3. Update
# 2. Columns
#    1. Create
#    2. Read
#    3. Update
###########################################################################################

#############
## ENTRIES ##
#############
# Define Entries
class Entry:
    # CREATE
    def __init__(self, id : int, name : str, content : str, column_name : str): # -> Entry
        self.id = str(id)
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
    def __init__(self, id : int, name : str, content : list = []): # -> Column
        self.id = str(id)
        self.headerTop = "="*40
        self.name = name
        self.headerBottom = "="*40
        self.content : list = content
        self.footer = "="*40

    # GET (READ)
    def get_column(self, name=""): # -> Column
        if (name != "" and name == self.name):
            return self

    # SET (UPDATE)
    def set_column(self, column_name: str, content : list = "") -> None:
        if (column_name == ""):
            self.name = self.name
        else:
            self.name = column_name
            self.content = content
    
###############
## CONTAINER ##
###############
class Container:
    def __init__(self, content : list = []):
        self.content : list = content