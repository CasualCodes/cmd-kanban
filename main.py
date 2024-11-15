###########################################################################################
# CMD - Kanban (Python)
###########################################################################################
# COMPONENTS [OVERHAUL]
###########################################################################################
# 1. Board Drawer - Draw the [boards/containers], draw entries [Consider placing as functions in a container class]
# 2. Initializer - Gets data from file_manager.py and starts data
# 3. Classes Utility - Class Definitions for [Boards/Containers], Entries, and [Containers]
#   [1.] Container Handler - Contains Functions For Moving Entries
# 4. Command Handler - contains cmd program operations
# 5. File Manager - writes data and retrieves data
# 6. Main - Debug Area, and Main Loop
# 
# 
# 
###########################################################################################
from board_drawer import Drawer
import command_handler
from file_manager import initializer, saver

def main():
    # Startup Settings [DEBUGGING]
    DEBUG : int = 0

    if (DEBUG == 0):
    
        """ Initial Requirements
        Main Loop:
        0. Intialize Defaults
            Create Initial Column Container
            Create Default Columns
        1. Render Columns

        2. Ask User Input > Select Column
        
        3. Ask User Input > Entry CRUD
            Create
            Read
            Update
            Delete

            ! Affects Entry Container (AKA Column)
        
        Repeat Loop : Until User Enters 'exit'
        """

        # Initialize / Load Data #
        data = initializer()

        # Print Board #
        board = Drawer()
        board.add_element(data)

        # Main Loop
        while (True):
            # Draw the board
            board.refresh(data)
            board.draw()
            # Command loop
            command_handler.column_ops(data)
            # Exit Prompt
            if (command_handler.exit_program() == 'Y'):
                saver(data)
                break

#     ## OVERHAUL TESTS
#     if (DEBUG == 1):
#         pass

#     ## OLD ITERATIVE LOOP TESTS
#     if (DEBUG == 2):
#         three_cols = initialize_columns()
#         # ITERATIVE LOOP TEST : COMMANDS (PRE MAJOR OVERHAUL)
#         while (input("Exit?") != 'exit'):
#             board_drawer.display_columns(three_cols)
#             command_handler.column_select(three_cols)
#             board_drawer.display_columns(three_cols)

#     ## OLD TESTS
#     if (DEBUG == 3):
#         # Run Testing Code

#         # TESTING # 1: INITIAL RUN 
#         column_name = "Research"
#         id : int = 0
#         column = Column(id, column_name, "")
#         # column = crud_handler.create_column(column_name) # Create Column

#         entry_placeholders = {"name" : "value",
#                             "Lorem Ipsum is simply dummy text." : "value2",
#                             "name3" : "value3"}
#         entries : Entry = []
#         id : int = 0
#         for key, value in entry_placeholders.items(): 
#             # entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry
#             entries.append(Entry(id, key, value, column_name))
#             id += 1

#         board_drawer.display_column(column, entries)

#         # TESTING # 2: SETTERS AND GETTERS
#         entries[0].set_entry("new_name", "new_value", column_name)

#         print(entries[0].get_entry().name)
#         board_drawer.display_column(column, entries)

#         # TESTING # 3: TEXT WRAP
#         lorem = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
#         print(board_drawer.text_wrap(lorem))

#         # TESTING # 4: MOVING ENTRIES AND DELETE
#         board_drawer.display_column(column, entries)
#         entries = move_entry(entries, 1, 2)
#         board_drawer.display_column(column, entries)
#         # entries = delete_entry(entries, 2)
#         # board_drawer.display_column(column, entries)

#         # TESTING # 5: MULTI COLUMN RENDERING [FAIL]
#         column.set_column(column.name,entries)
#         entries_2 : Entry = []
#         id : int = 0
#         for key, value in entry_placeholders.items(): 
#             # entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry
#             entries_2.append(Entry(id, key, value, column_name))
#             id += 1
#         column_2 = Column(1, "Planning", entries_2)
#         entries_2[1].set_entry("Lorem Ipsum is simply dummy text? dummy text?", "new_value", "Planning")
#         columns = [column, column_2]
#         board_drawer.display_columns(columns)

#         # TESTING # 6 : INTER COLUMN MOVE
#         # print("\n")
#         # board_drawer.display_column(columns[0], columns[0].content)
#         # board_drawer.display_column(columns[1], columns[1].content)
#         columns[0].content = move_entry(columns[0].content, 1, 3, columns[1].content)
#         columns[1].content = move_entry(columns[1].content, 1, 3)
#         board_drawer.display_columns(columns)

#         # TESTING # 7 : COMMANDS [FAIL - NEEDS RETHINKING]
#         three_cols = initialize_columns()
#         print("\n\n\n")
#         board_drawer.display_columns(three_cols)
#         command_handler.column_select(three_cols)
#         board_drawer.display_columns(three_cols)
        


# def initialize_columns() -> list:
#     column_names = ["Planning", "Doing", "Done"]
#     columns = []
#     i = 0
#     for column_name in column_names:

#         entry_placeholders = {"name" : "value",
#                             "Lorem Ipsum is simply dummy text." : "value2",
#                             "name3" : "value3"}
#         entries : Entry = []
#         id : int = 0
#         for key, value in entry_placeholders.items(): 
#             # entries.append(crud_handler.create_entry(key, value, column_name)) # Create Entry
#             entries.append(Entry(id, key, value, column_name))
#             id += 1
        
#         columns.append(Column(i, column_name, entries))
#         i+=1
#     return columns

if __name__ == "__main__":
    main()

