###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
import board_drawer
# import crud_handler
import command_handler
import file_manager
from classes_util import Entry, Column, move_column, move_entry, delete_column, delete_entry

# Basic Interface Display

def main():
    # Startup Settings [DEBUGGING]
    DEBUG : int = 1

    if (DEBUG == 0):
        pass
    if (DEBUG == 1):
        # Run Testing Code

        # TESTING # 1: INITIAL RUN 
        column_name = "Research"
        column = Column(column_name, "")
        # column = crud_handler.create_column(column_name) # Create Column

        entry_placeholders = {"name" : "value",
                            "name2" : "value2",
                            "name3" : "value3"}
        entries : Entry = []
        for key, value in entry_placeholders.items(): 
            # entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry
            entries.append(Entry(key, value, column_name))

        board_drawer.display_column(column, entries)

        # TESTING # 2: SETTERS AND GETTERS
        entries[0].set_entry("new_name", "new_value", column_name)

        print(entries[0].get_entry().name)
        board_drawer.display_column(column, entries)

        # TESTING # 3: TEXT WRAP
        lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
        print(board_drawer.text_wrap(lorem))

        # TESTING # 4: MOVING ENTRIES AND DELETE
        board_drawer.display_column(column, entries)
        entries = move_entry(entries, 1, 2)
        board_drawer.display_column(column, entries)
        entries = delete_entry(entries, 2)
        board_drawer.display_column(column, entries)


if __name__ == "__main__":
    main()

