###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Column, Entry

################
## OPERATIONS ##
################

# Move Element
def move_element(container : list, element, container_to : list = None, element_position : int = 0):
    if (container_to != None):
        add_element(container_to, element)
        remove_element(container, container.index(element))
    else:
        remove = container.index(element)
        if (element_position < len(container)):
            # Insert After Element Position
            container.insert(element_position+1, element)
            remove_element(container, remove)
        else:
            add_element(container, element)
            remove_element(container, remove)

# Add / Append Element
# TODO OPTIONAL : ADD POSITION
def add_element(container : list, element):
    container.append(element)

# Remove Element BY INDEX
def remove_element(container : list, index : int):
    container.pop(index)

# Get Element BY INDEX
def get_element(container : list, index : int):
    try:
        return container[index]
    except Exception:
        return None
# NOTE : READ / UPDATE is addressed by board_drawer and <object>., DELETE is addressed by garbage collection and remove_element

# Create Entries (One Group)
def create_entries(entries_data : list) -> list:
    entries = []
    if (entries_data != None):
        for name, content in entries_data:
            entries.append(Entry(name, content))
    return entries

# Create Columns
def create_columns(columns_data : list) -> list:
    columns = []
    if (columns_data != None):
        for name, content in columns_data:
            if (content == ""):
                entries = create_entries(content)
            else:
                entries = create_entries(eval(content))
            columns.append(Column(name, entries))
    return columns

if __name__ == "__main__":
    pass