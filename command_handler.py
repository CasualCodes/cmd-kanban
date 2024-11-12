###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 2. Command Handler - Command Handler on Editing, Adding New Entries, Moving Entries, and Deleting Entries
#    1. Command Mapping
#    3. Color Coding Responses
#    
###########################################################################################
from classes_util import Entry, Column
import operations_util

# Command Mapping
def column_select(container : list, default_query : str = "\n> "):
    column = input("Select Column [Name]\n> ")
    columns = []
    for col in container:
        columns.append(col.name)
    if column in columns:
        print(f"Column {column} selected")
        entry_operations(column)
    else:
        print("Invalid Input")

def entry_operations(container : list, default_query : str = "\n> "):
    action = input(default_query)

    match(action):
        case '+':
            # Call Create Entry [+]
            name = input("Enter Entry Name\n> ")
            content = input("Enter Entry Contents\n> ")
            container.append(Entry(len(container)+1, name, content, container.name))
            # Call Update Entry [e]

            # Call Move Entry   [mv]

            # Call Delete Entry [rm]
        case _:
            print("Invalid Command")



# Color Coding Repsonses

