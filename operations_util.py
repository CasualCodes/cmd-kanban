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

# Remove Element
def remove_element(container : list, element_identifier : int):
    container.remove(element_identifier)

# Get Element
def get_element(container : list, element_identifier : int):
    return container[element_identifier]

# NOTE : READ / UPDATE is addressed by board_drawer and <object>., DELETE is addressed by garbage collection and remove_element
# TODO : WHERE IS THE DICT FROM?
def create_entries(entries_data : dict) -> list:
    entries = []
    for name, content in entries_data.items():
        entries.append(Entry(name, content))
    return entries

def create_columns(columns_data : dict) -> list:
    columns = []
    for name, content in columns_data.items():
        columns.append(Column(name, content))
    return columns









## TO DELETE ##
# for element in container:
#         if (element_identifier == container.index(element)):
#             return element
#     return None
###############


# ############
# ##  MOVE  ##
# ############
# # MOVE ENTRY
# def move_entry(container : list, entry_position : int, entry_destination : int, container_to : list = None, entry : Entry = None) -> list:
#     ###################################################
#     # 1, 2, 3 
#     # 1, 2, 2, 3 X
#     ## DESTINATION should be AFTER intended position ##
#     # 1, 2, 3, 2
#     # 1, 2, 3 X
#     ## DESTINATION should be AFTER intended position ##
#     # 1, 3, 2
#     ###################################################

#     entry : Entry = container[entry_position]
#     container.pop(entry_position)
#     if (container_to != None):
#         container_to.insert(entry_destination, entry)
#     else:
#         container.insert(entry_destination, entry)
#     return container
# # MOVE COLUMN
# def move_column(container : list, column_position : int, column_destination : int) -> list:
#     column : Column = container[column_position]
#     container.insert(column_destination, column)
#     container.pop(column_position)
#     return container

# ##############
# ##  DELETE  ##
# ##############
# # NON URGENT TODO : POLISH
# # DELETE ENTRY
# def delete_entry(container : list, entry_position) -> list:
#     container.pop(entry_position)
#     return container

# # DELETE COLUMN
# def delete_column(container : list, column_position) -> list:
#     container.pop(column_position)
#     return container

