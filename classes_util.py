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
    def __init__(self, id, name : str, content : str):
        self.name = name
        self.content = content

    def set_entry(self, name : str, content : str) -> None:
        self.name = name
        self.content = content

#############
## COLUMNS ##
#############
# Define Columns
class Column:
    def __init__(self, id, name : str, content : list = []):
        self.name = name
        self.content : list = content

    def set_column(self, name: str, content : list = "") -> None:
        self.name = name
        self.content = content