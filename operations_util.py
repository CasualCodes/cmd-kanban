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
def move_entry(container : list, entry_position : int, entry_destination : int) -> list:
    entry : Entry = container[entry_position]
    container.insert(entry_destination, entry)
    container.pop(entry_position)
    return container

# MOVE COLUMN
def move_column(container : list, column_position : int, column_destination : int) -> list:
    # 1, 2, 3 
    column : Column = container[column_position]
    container.insert(column_destination, column)
    # 1, 2, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 2, 3, 2
    container.pop(column_position)
    # 1, 2, 3 X
    ## DESTINATION should be AFTER intended position ##
    # 1, 3, 2
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