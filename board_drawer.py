###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Column, Entry
from typing import List
from math import ceil, floor

############
## DRAWER ##
############

# TODO: VALIDATION
# OPTIONAL TODO : ADDRESS LIMITATION - REDUNDANCY ON DRAWER PADDING AND COLUMN LENGTH
class Drawer:
    def __init__(self):
        self.canvas = []
        self.width = 0
        self.width_limit = 0
        self.height = 0 # Potentially Unused
        self.graphic = ""
        self.padding = 0
        
        self.stored_elements = []

        self.default_width = 135
        self.default_width_limit = 3
        self.default_height = 0
        self.default_graphic = "="

        # Default Parameter Initialization
        self.set_canvas(self.width, self.height, self.graphic)
    
    def set_canvas(self, width : int = 0, width_limit : int = 0, height : int = 0, graphic : str = ""):
        # Zero = Dynamic
        if (width == 0):
            self.width = self.default_width
        if (width_limit == 0):
            self.width_limit = self.default_width_limit
        if (height == 0):
            self.height = self.default_height
        if (graphic == ""):
            self.graphic = self.default_graphic

        # Padding for Indentation [Default Value = 40]
        self.padding : int = floor(self.width/(self.width_limit*10)) * 10
    

    # TODO : COLUMN APPENDING <CHECKING>
    # IDEA : print(max(node.y for node in path.nodes)) # max(len(element.content) for content in element)
    def add_element(self, element, container : list = None, row : int = 0):

        if (element == None or element == []):
            return 

        if (type(element) == list):
            
            for sub_element in element:
                self.add_element(sub_element, element, row)

        elif (type(element) == Column):
            tolerance = 2
            
            # [======================================]
            row = self.add_border(row)
            # [[N] COLUMN_NAME]
            row = self.add_wrapped_text(row, container, element)
            # [======================================]
            row = self.add_border(row)

            ## <LIST> [[N] ENTRY_NAME [e] [mv] [rm]]
            # self.add_element(element.content, container, row)
            for entry in element.content:
                row = self.add_wrapped_text(row, element.content, entry)
            i = len(element.content)
            while (i < max(len(element.content)*tolerance for element in container)):
                row = self.add_blank_padding(row)
                i+=1

            # ## [======================================]
            row = self.add_border(row)
            i = len(element.content)
            while (i < max(len(element.content)*tolerance for element in container)):
                row = self.add_blank_padding(row)
                i+=1

        elif (type(element) == Entry):
            ## [[N] ENTRY_NAME [e] [mv] [rm]]
            row = self.add_wrapped_text(row, container, element)
            
        return  
        
## DRAW BORDERS AND NAME
    # TODO : PROPER ALGO [APPENDING MULTI COLUMNS] <CHECKING>
    def add_border(self, row : int):
        text_value = self.padding*self.graphic
        try:
            self.canvas[row] += text_value + append_padding(self.padding, text_value)
        except Exception: # Assumption: activates if self.canvas[row] = None
            self.canvas.append(text_value + append_padding(self.padding, text_value))
        row += 1
        return row

    def add_blank_padding(self, row : int):
        text_value = self.padding*" "
        try:
            self.canvas[row] += text_value + append_padding(self.padding, text_value)
        except Exception: # Assumption: activates if self.canvas[row] = None
            self.canvas.append(text_value + append_padding(self.padding, text_value))
        row += 1
        return row

    # TODO: TEXT WRAPPING <CHECKING>
    def add_wrapped_text(self, row : int, container : list, element):
        
        wrapped = text_wrap(element.name).split("\n")
        wrapped_row = 0
        wrapped_len = len(wrapped) - 1
        
        entry_formatting = ""
        if (type(element) == Entry):
            entry_formatting = "[e] [mv] [rm] "

        text_value = f"[{container.index(element)}] {wrapped[wrapped_row]} " + entry_formatting
        try:
            self.canvas[row] += text_value + append_padding(self.padding, text_value)
        except Exception: # Assumption: activates if self.canvas[row] = None
            self.canvas.append(text_value + append_padding(self.padding, text_value))

        row += 1
        wrapped_row += 1
        if (wrapped_len > 1):
            while(wrapped_row < wrapped_len):
                text_value = f"{wrapped[wrapped_row]}"
                try:
                    self.canvas[row] += text_value + append_padding(self.padding, text_value)
                except Exception: # Assumption: activates if self.canvas[row] = None
                    self.canvas.append(text_value + append_padding(self.padding, text_value))
                row += 1
                wrapped_row += 1

        return row

    def draw(self):
        for row in self.canvas:
            print(row)
    
    def clear(self):
        self.canvas = []
    
    def refresh(self, element : list):
        self.clear()
        self.add_element(element)

#######################
## UTILITY FUNCTIONS ##
#######################
# Text Wrapping

"""TEXT WRAP IDEA
        Returns wrapped string:
        Sample: 
            text_limit = 25
            Input: LoremLoremLoremLoremLoremLorem (30 characters)
            Output: LoremLoremLoremLoremLorem\nLorem (25 characters + newline + 5 characters)
        Application: Splitting string with \n, printing wrapped text""" 

# NOTE: Returned String, When \n Split, Is +1 more than intended
def text_wrap(text : str, limit : int = 2) -> str:
    text_limit = 21
    wrapped_string = ""
    string_index = 0
    
    chunks = ceil(len(text) / text_limit)
    if (limit != None):
        if (chunks > limit):
            chunks = limit

    for i in range(chunks):
        wrapped_string += text[string_index:string_index+text_limit] + "\n" 
        string_index += text_limit
    return wrapped_string

def append_padding(padding_value : int, text : str):
    return (" "*(padding_value-len(text))) + " "

# Testing and Validation
from file_manager import initializer
if __name__ == "__main__":

    """""""""
    Research,"[['res', 'conss']]"
    Planning,"[['planning', 'conss'],['planningsss', 'conss']]"
    Doing,"[['do dis', 'content'],['planningsss', 'conss'],['planningsss', 'conss']]"
    Done,"[['im', 'done'],['planningsss', 'conss']]"
    """""""""

    data = initializer()
    board = Drawer()
    # for d in data:
    #     print(d.content)
    #     print(d.content == [])
    board.add_element(data)
    board.draw()
    # print(board.canvas)
