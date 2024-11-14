###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# Entry:
#   init - name, content
#   set - name, content
#   get / delete > operations utility
# Column:
#   init - name, content(list)
#   set - name, content(list)
#   get / delete > operations utility
###########################################################################################

#############
## ENTRIES ##
#############
# Define Entries
class Entry:
    def __init__(self, name : str, content : str):
        self.name : str = name
        self.content : str = content

    def set(self, name : str, content : str) -> None:
        if (name != None):
            self.name : str = name
        if (content != None):
            self.content : str = content

#############
## COLUMNS ##
#############
# Define Columns
class Column:
    def __init__(self, name : str, content : list = [], length : int = 40):
        self.name : str = name
        self.content : list = content
        self.length : int = length

    def set(self, name: str, content : list = []) -> None:
        if (name != None):
            self.name : str = name
        if (content != []):
            self.content : list = content