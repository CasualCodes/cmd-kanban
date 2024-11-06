###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
import board_drawer
import crud_handler
import command_handler
import file_manager
from classes_util import Entry

# Basic Interface Display

def main():
    column_name = "Research"
    column = crud_handler.create_column(column_name) # Create Column

    entry_placeholders = {"name" : "value",
                        "name2" : "value2"}
    entries : Entry = []
    for key, value in entry_placeholders.items(): 
        entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry

    board_drawer.display_column(column, entries)


if __name__ == "__main__":
    main()

