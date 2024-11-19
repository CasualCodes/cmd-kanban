###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
from typing import List

#############
## ENTRIES ##
#############
# Define Entries
class Entry:
    def __init__(self, name : str, content : str):
        self.name : str = name
        self.content : str = content

    def set(self, name : str, content : str) -> None:
        if (name != ""):
            self.name : str = name
        if (content != ""):
            self.content : str = content
    
    def as_list(self) -> list:
        return [self.name, self.content]

#############
## COLUMNS ##
#############
# Define Columns
class Column:
    def __init__(self, name : str, content : List[Entry] = []):
        self.name : str = name
        self.content : List[Entry] = content

    def set(self, name: str, content : List[Entry] = []) -> None:
        if (name != None):
            self.name : str = name
        if (content != []):
            self.content : list[Entry] = content

    def as_list(self):
        content_as_list = []
        for element in self.content:
            content_as_list.append(element.as_list())
        return [self.name, content_as_list]