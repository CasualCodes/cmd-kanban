###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# Drawer:
# def __init__(self, width : int = 0, height : int = 0):
# > self.canvas = ""
# > self.canvas_paramenters = []
# set_canvas(self, width : int = 0, height : int = 0): sets width and height of the canvas bordered by #s 
# > zero is considered dynamic.
# > sets canvas parameters
#
# add_element(self, element): checks element type and sets to canvas according to element
# > if Container / List: add columns
# > if Column: draw borders and name and command map (to the left of name), then add entries, then add footer
# > if Entry : draw entry, with text wrap (limit to two lines and then ...), with command map to the right
#
# draw_canvas(self):
# > draws canvas
# 
# Utility Functions:
# text_wrap(string_limit, string): returns a string with \n to emulate string wrapping
###########################################################################################

from classes_util import Column, Entry
from math import ceil

############
## DRAWER ##
############

class Drawer:
    def __init__(self):
        self.canvas = []
        self.width = 0
        self.height = 0 # Potentially Unused
        self.graphic = ""

        self.default_width = 135
        self.default_height = 0
        self.default_graphic = "#"

        # Default Parameter Initialization
        self.set_canvas(self.width, self.height, self.graphic)
    
    def set_canvas(self, width : int = 0, height : int = 0, graphic : str = ""):
        # Zero = Dynamic
        if (width == 0):
            self.width = self.default_width
        if (height == 0):
            self.height = self.default_height
        if (graphic == ""):
            self.graphic = self.default_graphic
    
    # TODO : REIMPLEMENT DRAWING, WITH CANVAS LIMITATIONS
    def add_element(self, element, container : list = None):
        if (type(element) == list):
            for sub_element in element:
                # TODO : PROPER ALGO [APPENDING MULTI COLUMNS]
                self.add_element(sub_element)
        elif (type(element) == Column):

            ## IDEA: TURN CANVAS into a List of strings that are length canvas_length
            """Pseudo Code
            1. For Each COLUMN Element:
                - WRITE HEADERS (ATTATCH EACH COLUMN HEADER TO the canvas list)
                    - for text wrapping, attach a dynamic indent to each before \n
                        - suggestion: for readability sake, add setting to limit text lines to 2
                - WRITE ENTRIES (ATTACH EACH ENTRY OF EACH COLUMN TO the canvas list)
                    - for text wrapping, attach a dynamic indent to each before \n
                        - suggestion: for readability sake, add setting to limit text lines to 2
                - WRITE FOOTERS (ATTACH EACH COLUMN FOOTER TO the canvas list)
            """
            ## DRAW BORDERS AND NAME
            # TODO : PROPER ALGO [APPENDING MULTI COLUMNS]
            self.canvas.append(element.length*self.graphic + " ")
            # TODO: TEXT WRAPPING
            self.canvas += (element.name + " ")
            self.canvas.append(element.length*self.graphic + " ")

            ## DRAW ENTRIES
            self.add_element(element.content)

            ## DRAW FOOTER
            self.canvas.append(element.length*self.graphic + " ")


        elif (type(element) == Entry):
            ## Draw Entry
            # TODO : ALGO PROPER
            entry_contents = text_wrap(element).split("\n")
            
            # TODO: TEXT WRAPPING
            self.canvas += entry_contents[0]
    
    def draw_canvas(self):
        print(self.canvas) # TODO : TURN INTO FOR ROW IN CANVAS

#######################
## UTILITY FUNCTIONS ##
#######################
# Text Wrapping
# TODO : REDO TEXT LIMIT AND PADDING FUNCTION

# TEXT WRAP
# Returns wrapped string:
#   Sample: text_limit = 25
#       Input: LoremLoremLoremLoremLoremLorem (30 characters)
#       Output: LoremLoremLoremLoremLorem\nLorem (25 character + newline + 5 characters)
# Application: Splitting string with \n, printing wrapped text
def new_text_wrap(text : str) -> str:
    text_limit = 25
    wrapped_string = ""
    string_index = 0
    
    chunks = ceil(len(text) / text_limit)

    for i in range(chunks):
        wrapped_string += text[string_index:string_index+text_limit] + "\n" 
        string_index += text_limit
    return wrapped_string





def text_wrap(text : str, append : str = "" , padding : int = 0) -> str:
    text_limit = 25
    split_string = ""
    string_index = 0
    
    chunks = ceil(len(text) / text_limit)

    for i in range(chunks):
        if (i == 0):
            split_string = split_string + text[string_index:string_index+text_limit] + " "*(text_limit-len(text)) + append + "\n"
            string_index = string_index + text_limit
        else:
            split_string = split_string + text[string_index:string_index+text_limit] + "\n" 
            string_index = string_index + text_limit
    return split_string[0:(len(split_string)-1)]




def display_columns(column_list : list) -> None:
    padding = 40

    # HEADERS #
    display = ""
    for column in column_list:
        display += column.headerTop + " "*(padding-len(column.headerTop)) + "  "
    print(display)
    display = ""
    for column in column_list:
        display += column.name + " "*(padding-len(column.name)) + "  "
    print(display)
    display = ""
    for column in column_list:
        display += column.headerBottom + " "*(padding-len(column.headerBottom)) + "  "
    print(display)

    ################################################################
    # DELETE THIS CODE IF YOU MANAGE TO IMPLEMENT A BETTER SOLUTION
    ################################################################
    column_entry_counts = []
    for column in column_list:
        column_entry_counts.append(len(column.content))
    display = ""
    turns = max(column_entry_counts)
    
    for turn in range(turns):
        backlogs = []
        for column in column_list:
            try:
                display += text_wrap(f"[{column.content[turn].id}] {column.content[turn].name}", " [e] [mv] [rm]")
                border = display.rfind(" [e] [mv] [rm]")
                # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
                # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
                backlogs.append(display[border+len(" [e] [mv] [rm]")+1:len(display)])
                display = display[0:border+len(" [e] [mv] [rm]")] + " "*(padding-(25 + len(" [e] [mv] [rm]"))) + "  " 
            except (Exception):
                display += " "*(padding) + "  "
                backlogs.append('')
        
        print(display)
        display = ""
        # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
        # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
        # print(backlogs)
        for backlog in backlogs:
            display += backlog + " "*(padding-len(backlog)) + "  "
        print(display)
        display = ""

    # footers #
    display = ""
    for column in column_list:
        display += column.footer + " "*(padding-len(column.footer)) + "  "
    print(display)









# Display A Column
# TODO: INDEXING [DONE]
def display_column(column : Column, entries : list) -> None:
    print(column.headerTop)
    print(column.name)
    print(column.headerBottom)
    display_entries(column.name, entries) # display_entries(column.name, column.content)
    print(column.footer)

def display_entry(entry : Entry) -> None:
    # e - edit
    # mv - move
    # rm - remove
    print(text_wrap(f"[{entry.id}] {entry.name}", " [e] [mv] [rm]"))

def display_entries(column_name : str, entries : list) -> None:
    for entry in entries:
        display_entry(entry)



def display_columns(column_list : list) -> None:
    padding = 40

    # HEADERS #
    display = ""
    for column in column_list:
        display += column.headerTop + " "*(padding-len(column.headerTop)) + "  "
    print(display)
    display = ""
    for column in column_list:
        display += column.name + " "*(padding-len(column.name)) + "  "
    print(display)
    display = ""
    for column in column_list:
        display += column.headerBottom + " "*(padding-len(column.headerBottom)) + "  "
    print(display)

    ################################################################
    # DELETE THIS CODE IF YOU MANAGE TO IMPLEMENT A BETTER SOLUTION
    ################################################################
    column_entry_counts = []
    for column in column_list:
        column_entry_counts.append(len(column.content))
    display = ""
    turns = max(column_entry_counts)
    
    for turn in range(turns):
        backlogs = []
        for column in column_list:
            try:
                display += text_wrap(f"[{column.content[turn].id}] {column.content[turn].name}", " [e] [mv] [rm]")
                border = display.rfind(" [e] [mv] [rm]")
                # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
                # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
                backlogs.append(display[border+len(" [e] [mv] [rm]")+1:len(display)])
                display = display[0:border+len(" [e] [mv] [rm]")] + " "*(padding-(25 + len(" [e] [mv] [rm]"))) + "  " 
            except (Exception):
                display += " "*(padding) + "  "
                backlogs.append('')
        
        print(display)
        display = ""
        # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
        # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
        # print(backlogs)
        for backlog in backlogs:
            display += backlog + " "*(padding-len(backlog)) + "  "
        print(display)
        display = ""

    # footers #
    display = ""
    for column in column_list:
        display += column.footer + " "*(padding-len(column.footer)) + "  "
    print(display)
    
