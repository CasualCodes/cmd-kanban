###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# 1. Move
# 2. Delete
###########################################################################################












from classes_util import Column, Entry

#####################
## LIST OPERATIONS ##
#####################

############
##  MOVE  ##
############
# MOVE ENTRY
def move_entry(container : list, entry_position : int, entry_destination : int, container_to : list = None, entry : Entry = None) -> list:
    ###################################################
    # 1, 2, 3 
    # 1, 2, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 2, 3, 2
    # 1, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 3, 2
    ###################################################

    entry : Entry = container[entry_position]
    container.pop(entry_position)
    if (container_to != None):
        container_to.insert(entry_destination, entry)
    else:
        container.insert(entry_destination, entry)
    return container
# MOVE COLUMN
def move_column(container : list, column_position : int, column_destination : int) -> list:
    column : Column = container[column_position]
    container.insert(column_destination, column)
    container.pop(column_position)
    return container

##############
##  DELETE  ##
##############
# NON URGENT TODO : POLISH
# DELETE ENTRY
def delete_entry(container : list, entry_position) -> list:
    container.pop(entry_position)
    return container

# DELETE COLUMN
def delete_column(container : list, column_position) -> list:
    container.pop(column_position)
    return container

###########
##  GET  ##
###########
def get_element(container : list, name : int):
    for element in container:
        if (name == element.id):
            return element
    return None