###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Board Drawer - An Ascii Display of the Board containing all entries
#    1. Text Wrapping - All stored text have wrapping
#       1. How it works: All inputted text are divided into chunks seperated by a new line
#    2. Four Columns - Research, Planning, Doing, Done
#       1. Optional: Customize Column Count
###########################################################################################
from classes_util import Column, Entry
from math import ceil

# Text Wrapping
# TODO : DECIDE - Execute Text-Wrapping when storing the text? or only execute it when displaying?
def text_wrap(text : str, append : str = "" , padding : int = 0) -> str:
    text_limit = 25
    # If text limit is reached, divide, and append \n
    # Is there a library for this?

    # IDEA: https://stackoverflow.com/questions/7111068/split-string-by-count-of-characters
    # def chunks(s, n):
    # """Produce `n`-character chunks from `s`."""
    # for start in range(0, len(s), n):
    #     yield s[start:start+n]

    # nums = "1.012345e0070.123414e-004-0.1234567891.21423"
    # for chunk in chunks(nums, 12):
    #     print chunk

    split_string = ""
    string_index = 0
    # calculate chunks by text_limit
    chunks = ceil(len(text) / text_limit)
    for i in range(chunks):
        if (i == 0):
            split_string = split_string + text[string_index:string_index+text_limit] + " "*(text_limit-len(text)) + append + "\n"
            string_index = string_index + text_limit
        else:
            split_string = split_string + text[string_index:string_index+text_limit] + "\n" 
            string_index = string_index + text_limit
    return split_string[0:(len(split_string)-1)]

# Display A Column
# TODO: INDEXING [DONE]
def display_column(column : Column, entries : list) -> None:
    print(column.headerTop)
    print(column.name)
    print(column.headerBottom)
    display_entries(column.name, entries) # display_entries(column.name, column.content)
    print(column.footer)

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
    

def display_entry(entry : Entry) -> None:
    # e - edit
    # mv - move
    # rm - remove
    print(text_wrap(f"[{entry.id}] {entry.name}", " [e] [mv] [rm]"))

def display_entries(column_name : str, entries : list) -> None:
    for entry in entries:
        display_entry(entry)







def display_defaults(defaults : int) -> None:
    pass

# Generate Each Default Column
#   Research
#   Planning
#   Doing
#   None
def generate_defaults(defaults : int) -> str:
    pass

