###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Column, Entry
from math import ceil, floor
from os import system

############
## DRAWER ##
############

# TODO : 4 Column Per Row Implementation
"""- IDEA : if len > 2, make new row list.
        then for each row of cols, print"""

class Drawer:
    def __init__(self):
        # TODO : refactor self.canvas and self.new_canvas
        self.canvas = []
        self.new_canvas = []
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
    
    def add_element(self, element, container : list = None, row : int = 0):
        
        column : list = []

        if (element == None or element == []):
            return 

        if (type(element) == list):
            
            for sub_element in element:
                column = self.add_element(sub_element, element, row)
                self.canvas.append(column)
                column = []

        elif (type(element) == Column):
            # [======================================]
            row = self.add_border(column, row)
            # [[N] COLUMN_NAME]
            row = self.add_wrapped_text(column, row, container, element)
            # [======================================]
            row = self.add_border(column, row)
            ## <LIST> [[N] ENTRY_NAME [e] [mv] [rm]]
            for entry in element.content:
                row = self.add_wrapped_text(column, row, element.content, entry)
            # ## [======================================]
            row = self.add_border(column, row)
        return column
        
## DRAW BORDERS AND NAME
    def add_border(self, canvas : list, row : int):
        text_value = self.padding*self.graphic
        canvas.append(text_value + append_padding(self.padding, text_value))
        return row+1

    def add_wrapped_text(self, canvas : list, row : int, container : list, element):
        
        wrapped = text_wrap(element.name).split("\n")
        wrapped_row = 0
        wrapped_len = len(wrapped) - 1
        
        entry_formatting = ""
        if (type(element) == Entry):
            entry_formatting = "[e] [mv] [rm] "

        text_value = f"[{container.index(element)}] {wrapped[wrapped_row]} " + entry_formatting
        canvas.append(text_value + append_padding(self.padding, text_value))
        row+=1

        wrapped_row += 1
        if (wrapped_len > 1):
            while(wrapped_row < wrapped_len):
                text_value = f"{wrapped[wrapped_row]}"
                try:
                    canvas[row] += text_value + append_padding(self.padding, text_value)
                except Exception: # Assumption: activates if self.canvas[row] = None
                    canvas.append(text_value + append_padding(self.padding, text_value))
                wrapped_row += 1
                row+=1
        return row


    def add_blank_padding(self, canvas : list, row : int):
        text_value = self.padding*" "
        try:
            canvas[row] += text_value + append_padding(self.padding, text_value)
        except Exception: # Assumption: activates if self.canvas[row] = None
            canvas.append(text_value + append_padding(self.padding, text_value))
        return row+1


    def draw(self):
        for row in self.canvas:
            render_row = 0
            while (render_row < len(row)):
                try:
                    self.new_canvas[render_row] += row[render_row]
                except Exception:
                    self.new_canvas.append(row[render_row])
                render_row+=1
                if(render_row >= len(row)):
                    i = len(row)
                    while (i < len(max(self.canvas, key=len))):
                        render_row = self.add_blank_padding(self.new_canvas, render_row)
                        i+=1
            render_row = 0
        for row in self.new_canvas:
            print(row)
            
    
    def clear(self):
        self.canvas = []
        self.new_canvas = []
    
    def refresh(self, element : list):
        self.clear()
        system('cls')
        self.add_element(element)
        self.draw()

#######################
## UTILITY FUNCTIONS ##
#######################

# Text Wrapping
# NOTE: Returned String, When \n Split, Is +1 more than intended
def text_wrap(text : str, limit : int = 3) -> str:
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
    data = initializer()
    board = Drawer()
    # for d in data:
    #     print(d.content)
    #     print(d.content == [])
    board.add_element(data)
    board.draw()
    # print(board.canvas)