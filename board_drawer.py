###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Column, Entry
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
    def add_element(self, element, container : list = None, row : int = 0):

        if (element == None):
            return

        if (type(element) == list):
            for sub_element in element:
                # TODO : PROPER ALGO [APPENDING MULTI COLUMNS] <CHECKING>
                if (type(sub_element) == Entry):
                    self.add_element(sub_element, element, row)
                    row += 1
                else:
                    self.add_element(sub_element, element, row)

        elif (type(element) == Column):
            
            ## IDEA: TURN CANVAS into a List of strings that are length canvas_length
            """Pseudo Code
            1. For Each COLUMN Element:
                - WRITE HEADERS (ATTATCH EACH COLUMN HEADER TO the canvas list)
                    - for text wrapping, attach a dynamic indent to each before \n
                        - suggestion: for readability sake, add setting to limit text lines to 2 <OPTIONAL>
                - WRITE ENTRIES (ATTACH EACH ENTRY OF EACH COLUMN TO the canvas list)
                    - for text wrapping, attach a dynamic indent to each before \n
                        - suggestion: for readability sake, add setting to limit text lines to 2 <OPTIONAL>
                - WRITE FOOTERS (ATTACH EACH COLUMN FOOTER TO the canvas list)
            """
            # [======================================]
            row = self.add_border(row)
            # [[N] COLUMN_NAME]
            row = self.add_wrapped_text(row, container, element)
            # [======================================]
            row = self.add_border(row)

            ## <LIST> [[N] ENTRY_NAME]
            self.add_element(element.content, container, row)

            # NOTE : BANDAID SOLUTION
            # ## [======================================]
            row += 1
            row = self.add_border(row)

        elif (type(element) == Entry):
            ## [[N] ENTRY_NAME [e] [mv] [rm]]
            # TODO : ALGO PROPER
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
def text_wrap(text : str) -> str:
    text_limit = 25
    wrapped_string = ""
    string_index = 0
    
    chunks = ceil(len(text) / text_limit)

    for i in range(chunks):
        wrapped_string += text[string_index:string_index+text_limit] + "\n" 
        string_index += text_limit
    return wrapped_string

def append_padding(padding_value : int, text : str):
    return (" "*(padding_value-len(text))) + " "

from file_manager import initializer
if __name__ == "__main__":
    pass
    # Initialize / Load Data #
    data = initializer()

    # Print Board #
    board = Drawer()
    board.add_element(data)
    # print(board.canvas)


    board.draw()

































# ###############
# ## TO DELETE ##
# ###############
# def old_text_wrap(text : str, append : str = "" , padding : int = 0) -> str:
#     text_limit = 25
#     split_string = ""
#     string_index = 0
    
#     chunks = ceil(len(text) / text_limit)

#     for i in range(chunks):
#         if (i == 0):
#             split_string = split_string + text[string_index:string_index+text_limit] + " "*(text_limit-len(text)) + append + "\n"
#             string_index = string_index + text_limit
#         else:
#             split_string = split_string + text[string_index:string_index+text_limit] + "\n" 
#             string_index = string_index + text_limit
#     return split_string[0:(len(split_string)-1)]




# def display_columns(column_list : list) -> None:
#     padding = 40

#     # HEADERS #
#     display = ""
#     for column in column_list:
#         display += column.headerTop + " "*(padding-len(column.headerTop)) + "  "
#     print(display)
#     display = ""
#     for column in column_list:
#         display += column.name + " "*(padding-len(column.name)) + "  "
#     print(display)
#     display = ""
#     for column in column_list:
#         display += column.headerBottom + " "*(padding-len(column.headerBottom)) + "  "
#     print(display)

#     ################################################################
#     # DELETE THIS CODE IF YOU MANAGE TO IMPLEMENT A BETTER SOLUTION
#     ################################################################
#     column_entry_counts = []
#     for column in column_list:
#         column_entry_counts.append(len(column.content))
#     display = ""
#     turns = max(column_entry_counts)
    
#     for turn in range(turns):
#         backlogs = []
#         for column in column_list:
#             try:
#                 display += text_wrap(f"[{column.content[turn].id}] {column.content[turn].name}", " [e] [mv] [rm]")
#                 border = display.rfind(" [e] [mv] [rm]")
#                 # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
#                 # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
#                 backlogs.append(display[border+len(" [e] [mv] [rm]")+1:len(display)])
#                 display = display[0:border+len(" [e] [mv] [rm]")] + " "*(padding-(25 + len(" [e] [mv] [rm]"))) + "  " 
#             except (Exception):
#                 display += " "*(padding) + "  "
#                 backlogs.append('')
        
#         print(display)
#         display = ""
#         # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
#         # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
#         # print(backlogs)
#         for backlog in backlogs:
#             display += backlog + " "*(padding-len(backlog)) + "  "
#         print(display)
#         display = ""

#     # footers #
#     display = ""
#     for column in column_list:
#         display += column.footer + " "*(padding-len(column.footer)) + "  "
#     print(display)









# # Display A Column
# # TODO: INDEXING [DONE]
# def display_column(column : Column, entries : list) -> None:
#     print(column.headerTop)
#     print(column.name)
#     print(column.headerBottom)
#     display_entries(column.name, entries) # display_entries(column.name, column.content)
#     print(column.footer)

# def display_entry(entry : Entry) -> None:
#     # e - edit
#     # mv - move
#     # rm - remove
#     print(text_wrap(f"[{entry.id}] {entry.name}", " [e] [mv] [rm]"))

# def display_entries(column_name : str, entries : list) -> None:
#     for entry in entries:
#         display_entry(entry)



# def display_columns(column_list : list) -> None:
#     padding = 40

#     # HEADERS #
#     display = ""
#     for column in column_list:
#         display += column.headerTop + " "*(padding-len(column.headerTop)) + "  "
#     print(display)
#     display = ""
#     for column in column_list:
#         display += column.name + " "*(padding-len(column.name)) + "  "
#     print(display)
#     display = ""
#     for column in column_list:
#         display += column.headerBottom + " "*(padding-len(column.headerBottom)) + "  "
#     print(display)

#     ################################################################
#     # DELETE THIS CODE IF YOU MANAGE TO IMPLEMENT A BETTER SOLUTION
#     ################################################################
#     column_entry_counts = []
#     for column in column_list:
#         column_entry_counts.append(len(column.content))
#     display = ""
#     turns = max(column_entry_counts)
    
#     for turn in range(turns):
#         backlogs = []
#         for column in column_list:
#             try:
#                 display += text_wrap(f"[{column.content[turn].id}] {column.content[turn].name}", " [e] [mv] [rm]")
#                 border = display.rfind(" [e] [mv] [rm]")
#                 # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
#                 # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
#                 backlogs.append(display[border+len(" [e] [mv] [rm]")+1:len(display)])
#                 display = display[0:border+len(" [e] [mv] [rm]")] + " "*(padding-(25 + len(" [e] [mv] [rm]"))) + "  " 
#             except (Exception):
#                 display += " "*(padding) + "  "
#                 backlogs.append('')
        
#         print(display)
#         display = ""
#         # CONSIDERATION : TEXT WRAPPING. CONTINUE OR CANCEL?
#         # TODO : LIMIT DISPLAY WRAPPING TO 2 LINES / CHUNKS
#         # print(backlogs)
#         for backlog in backlogs:
#             display += backlog + " "*(padding-len(backlog)) + "  "
#         print(display)
#         display = ""

#     # footers #
#     display = ""
#     for column in column_list:
#         display += column.footer + " "*(padding-len(column.footer)) + "  "
#     print(display)
    
