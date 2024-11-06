###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Entries
# 2. Columns
###########################################################################################

# Define Entries
class Entry:
    def __init__(self, name : str, content : str, column_name : str):
        self.name = name
        self.content = content
        self.column = column_name

# Define Columns
class Column:
    def __init__(self, name : str, content : str):
        self.headerTop = "="*40
        self.name = name
        self.headerBottom = "="*40
        self.content = content
        self.footer = "="*40