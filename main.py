###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
import board_drawer
import crud_handler
import command_handler
import file_manager
from classes_util import Entry
from classes_util import Column

# Basic Interface Display

def main():
    # TESTING # 1: INITIAL RUN 
    column_name = "Research"
    column = crud_handler.create_column(column_name) # Create Column

    entry_placeholders = {"name" : "value",
                        "name2" : "value2"}
    entries : Entry = []
    for key, value in entry_placeholders.items(): 
        entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry

    board_drawer.display_column(column, entries)

    # TESTING # 2: SETTERS AND GETTERS
    # entries[0].set_entry("new_name", "new_value", column_name)

    # print(entries[0].get_entry().name)
    # board_drawer.display_column(column, entries)


if __name__ == "__main__":
    main()

