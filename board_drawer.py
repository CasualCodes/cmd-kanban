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
def text_wrap(text : str) -> str:
    text_limit = 29
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
        split_string = split_string + text[string_index:string_index+text_limit] + "\n"
        string_index = string_index + text_limit
    return split_string

# Display A Column
# TODO: INDEXING [DONE]
def display_column(column : Column, entries : list) -> None:
    print(column.headerTop)
    print(column.name)
    print(column.headerBottom)
    display_entries(column.name, entries)
    print(column.footer)

def display_entries(column_name : str, entries : list) -> None:
    for entry in entries:
        print(text_wrap(entry.name))

def display_defaults(defaults : int) -> None:
    pass

# Generate Each Default Column
#   Research
#   Planning
#   Doing
#   None
def generate_defaults(defaults : int) -> str:
    pass

