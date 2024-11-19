###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from classes_util import Entry, Column
from typing import List
from operations_util import get_element, move_element, remove_element
from board_drawer import text_wrap
from os import system
from math import ceil, floor

# Delete Previous Line With ANSI Escape Character
def delete_line(lines : int = 1):
    iterator = 0
    while (iterator < lines):
        print("\033[1A\x1b[2K", end="")
        iterator += 1

# IDEA : Once user submits input, previous two lines are deleted
def prompter(prompt_header : str = "Prompt Header:", prompt_input : str = "> ", deln : int = 2):
    user_input = input(f"{prompt_header}\n{prompt_input}")
    delete_line(deln)
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
                column_index = int(prompter(select_query))

                column : Column = get_element(container, column_index)
                if (column != None):
                    print(f"Selected Column [{container.index(column)}] {column.name}")
                    entry_operations(container, column.content)
                else:
                    print("Invalid Input : Column Not Found")
                    delete_line("Invalid Input : Column Not Found")
            case _:
                print("Closing")
                return

# Entry Operations
def entry_operations(top_container : list, container : list, default_query : str = "Select Action\n> "):
    while (True):
        mode_query = "Choose Entry Operation: Read [N], Add [+], Edit [e], Move [mv], Remove [rm] Return to Column Select []:"
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
                entry_index = int(prompter(sel_query))
                entry : Entry = get_element(container, entry_index)
                if (entry != None):
                    name_query = "Enter New Entry Name [enter None to not change]:"
                    name = prompter(name_query)
                    content_query = "Enter New Entry Contents [enter None to not change]:"
                    content = prompter(content_query)
                    entry.set(name, content)
                else:
                    print("Invalid Input : Entry Not Found")

            case 'mv':
                # Call Entry Move [mv]
                sel_query = "Select [ID] Element:"
                entry_index = int(prompter(sel_query))
                try:
                    entry : Entry = get_element(container, entry_index)
                except Exception:
                    entry = None
                    print("Invalid Input : Entry Not Found")

                sel_query = "Select: [ID] Column:"
                column_index = int(prompter(sel_query))
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
                entry_index = int(prompter(sel_query))
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
                if (mode == ""):
                    return
                else:
                    try:
                        entry : Entry = get_element(container, int(mode))
                        length = 0
                        print(40*"=")
                        length += 3
                        print(text_wrap(f"[{mode}] {entry.name}", None))
                        length += ceil(len(f"[{mode}] {entry.name}") / 21)
                        print(text_wrap(f"Content : {entry.content}", None))
                        length += ceil(len(f"Content : {entry.content}") / 21)
                        print(40*"=")
                        length += 3

                        prompter("Press enter to return", "> ", length)
                    except Exception:
                        entry = None
                        print("Invalid Input : Entry Not Found")
                    

def exit_program() -> str:
    exit_prompt = "Close Program? [Y/n]:"
    prompt = prompter(exit_prompt)
    return prompt

if __name__ == "__main__":
    pass