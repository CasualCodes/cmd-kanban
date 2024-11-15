###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Entry, Column
from typing import List
from operations_util import get_element, move_element, remove_element

# Delete Previous Line With ANSI Escape Character
def delete_line(lines : int = 1):
    iterator = 0
    while (iterator < lines):
        print("\033[1A\x1b[2K", end="")
        iterator += 1

# IDEA : Once user submits input, previous two lines are deleted
def prompter(prompt_header : str = "Prompt Header:", prompt_input : str = "> "):
    user_input = input(f"{prompt_header}\n{prompt_input}")
    delete_line(2)
    return user_input

# Column Operations
def column_ops(container : List[Column]):
    while(True):
        # TODO : , Add [+], Edit [e]
        mode_query = "Choose Column Operation: Select [s] Exit []:" 
        select_query = "Select: [ID] Column:"
        mode = prompter(mode_query)

        match mode:
            case 's':
                column_index = prompter(select_query)

                column : Column = get_element(container, column_index)
                if (column != None):
                    print(f"Selected Column [{container.index(column)}] {column.name}")
                    entry_operations(container, column.content)
                else:
                    print("Invalid Input : Column Not Found")
            case _:
                print("Closing")
                return

# Entry Operations
def entry_operations(top_container : list, container : list, default_query : str = "Select Action\n> "):
    while (True):
        mode_query = "Choose Entry Operation: Edit [e], Move [mv], Remove [rm] Return to Column Select []:"
        mode = prompter(mode_query)
        match(mode):
            case '+':
                # Call Entry Constructor [+]
                name_query = "Enter Entry Name:"
                name = prompter(name_query)
                content_query = "Enter Entry Contents:"
                content = prompter(content_query)

                container.append(Entry(name, content))

            case 'e':
                # Call Entry Set [e]
                sel_query = "Select [ID] Element:"
                entry_index = prompter(sel_query)
                entry : Entry = get_element(container, entry_index)
                if (entry != None):
                    name_query = "Enter New Entry Name [press enter to not change]:"
                    name = prompter(name_query)
                    content_query = "Enter New Entry Contents [press enter to not change]:"
                    content = prompter(content_query)
                    entry.set(content, container.name)
                else:
                    print("Invalid Input : Entry Not Found")

            case 'mv':
                # Call Entry Move [mv]
                sel_query = "Select [ID] Element:"
                entry_index = prompter(sel_query)
                try:
                    entry : Entry = get_element(container, entry_index)
                except Exception:
                    entry = None
                    print("Invalid Input : Entry Not Found")

                sel_query = "Select Column [Name]:"
                column_index = prompter(sel_query)
                try:
                    column : Column = get_element(top_container, column_index)
                except Exception:
                    column = None

                if (column != None):
                    if (entry != None):
                        # TODO : , element_position : int = 0
                        move_element(container, entry, column.content)
                elif (entry != None):
                    sel_query = "Select New Position [0 <= N < =no._of_entries]:"
                    position = prompter(sel_query)
                    if (position <= len(container) and position >= 0):
                        move_element(container, entry, column, position)
                    else:
                        print("Invalid Input : Position Invalid")
                else:
                    print("Invalid Input : Entry Not Found")

            case 'rm':
                # Call Delete Entry [rm]
                sel_query = "Select [ID] Element:"
                entry_index = prompter(sel_query)
                try:
                    entry : Entry = get_element(container, entry_index)
                except Exception:
                    entry = None
                    print("Invalid Input : Entry Not Found")
                if (entry != None):
                    remove_element(container, container.index(entry))
                else:
                    print("Invalid Input : Entry Not Found")

            case _:
                return

if __name__ == "__main__":
    pass








# from operations_util import get_element, move_entry, delete_entry
# # # Command Mapping
# # def column_select(container : list, default_query : str = "Select Column [Name]\n> "):
# #     column = input(default_query)

# #     columns = []
# #     for col in container:
# #         columns.append(col.id)

# #     if column in columns:
# #         print(f"Column {column} selected")
# #         entry_operations(container, get_element(container, column))
# #     else:
# #         print("Invalid Input")

# def entry_operations(top_container : list, container : list, default_query : str = "Select Action\n> "):
#     action = input(default_query)

#     match(action):

#         case '+':
#             # Call Create Entry [+]
#             name = input("Enter Entry Name\n> ")
#             content = input("Enter Entry Contents\n> ")
#             container.content.append(Entry(len(container.content)+1, name, content, container.name))
#         case 'e':
#             # Call Update Entry [e]
#             name = input("Select Element [ID]\n> ")
#             entry = get_element(container.content, name)
#             if (entry != None):
#                 name = input("Enter New Entry Name\n> ")
#                 content = input("Enter New Entry Contents\n> ")
#                 entry.set_entry(name, content, container.name)
#             else:
#                 print("Entry does not exist")
#         case 'mv':
#             # Call Move Entry   [mv]
#             name = input("Select Element [ID]\n> ")
#             entry = get_element(container.content, name)
#             move_to = input("Select Column [Name]\n> ")
            
#             columns = []
#             for col in top_container:
#                 columns.append(col.id)

#             if move_to in columns:
#                 move_entry(container.content, (container.content).index(entry), len(move_to)+1, get_element(top_container,move_to).content)
#                 print(f"Moved To Column {move_to}")
#             else:
#                 print("Invalid Column")

#         case 'rm':
#             # Call Delete Entry [rm]
#             name = input("Select Element [ID]\n> ")
#             entry = get_element(container.content, name)
#             top_container = delete_entry(container.content, (container.content).index(entry))

#         case _:
#             print("Invalid Command")