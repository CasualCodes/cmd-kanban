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

    # GET
    # TODO : RECONSIDER THIS AS READ
    def get_entry(self):
        return self
    
    # SET
    # TODO : RECONSIDER AS WRITE
    def set_entry(self, entry_name : str, entry_content : str, entry_column : str):
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

# Define Columns
class Column:
    def __init__(self, name : str, content : str):
        self.headerTop = "="*40
        self.name = name
        self.headerBottom = "="*40
        self.content = content
        self.footer = "="*40

    # GET
    # TODO : RECONSIDER THIS AS READ
    def get_column(self):
        return self

    # SET
    # TODO : RECONSIDER AS WRITE    
    def set_column(self, column_name: str):
        if (column_name == ""):
            self.name = self.name
        else:
            self.name = column_name
    
    