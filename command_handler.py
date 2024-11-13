###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 2. Command Handler - Command Handler on Editing, Adding New Entries, Moving Entries, and Deleting Entries
#    1. Command Mapping
#    
###########################################################################################
#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#  
###########################################################################################

from classes_util import Entry, Column
from operations_util import get_element, move_entry, delete_entry

# Command Mapping
def column_select(container : list, default_query : str = "Select Column [Name]\n> "):
    column = input(default_query)

    columns = []
    for col in container:
        columns.append(col.id)

    if column in columns:
        print(f"Column {column} selected")
        entry_operations(container, get_element(container, column))
    else:
        print("Invalid Input")

def entry_operations(top_container : list, container : list, default_query : str = "Select Action\n> "):
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
            entry = get_element(container.content, name)
            if (entry != None):
                name = input("Enter New Entry Name\n> ")
                content = input("Enter New Entry Contents\n> ")
                entry.set_entry(name, content, container.name)
            else:
                print("Entry does not exist")
        case 'mv':
            # Call Move Entry   [mv]
            name = input("Select Element [ID]\n> ")
            entry = get_element(container.content, name)
            move_to = input("Select Column [Name]\n> ")
            
            columns = []
            for col in top_container:
                columns.append(col.id)

            if move_to in columns:
                move_entry(container.content, (container.content).index(entry), len(move_to)+1, get_element(top_container,move_to).content)
                print(f"Moved To Column {move_to}")
            else:
                print("Invalid Column")

        case 'rm':
            # Call Delete Entry [rm]
            name = input("Select Element [ID]\n> ")
            entry = get_element(container.content, name)
            top_container = delete_entry(container.content, (container.content).index(entry))

        case _:
            print("Invalid Command")