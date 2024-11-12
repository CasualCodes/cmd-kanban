###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 2. Command Handler - Command Handler on Editing, Adding New Entries, Moving Entries, and Deleting Entries
#    1. Command Mapping
#    3. Color Coding Responses
#    
###########################################################################################
from classes_util import Entry, Column
from operations_util import get_element

# Command Mapping
def column_select(container : list, default_query : str = "Select Column [Name]\n> "):
    column = input(default_query)

    columns = []
    for col in container:
        columns.append(col.name)

    if column in columns:
        print(f"Column {column} selected")
        entry_operations(get_element(container, column))
    else:
        print("Invalid Input")

def entry_operations(container : list, default_query : str = "Select Action\n> "):
    action = input(default_query)

    match(action):

        case '+':
            # Call Create Entry [+]
            name = input("Enter Entry Name\n> ")
            content = input("Enter Entry Contents\n> ")
            container.content.append(Entry(len(container.content)+1, name, content, container.name))
        case 'e':
            # Call Update Entry [e]
            name = input("Select Element [ID]\n> ")
            entry = get_element(container.content, id)
            if (entry != None):
                name = input("Enter New Entry Name\n> ")
                content = input("Enter New Entry Contents\n> ")
                entry.set_entry(name, content, container.name)
            else:
                print("Entry does not exist")
        
            # Call Move Entry   [mv]
            name = input("Select Element [ID]\n> ")
            entry = get_element(container.content, id)

            # Call Delete Entry [rm]
            name = input("Select Element [ID]\n> ")
            
        case _:
            print("Invalid Command")

# Color Coding Repsonses
