###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

from board_drawer import Drawer
import command_handler
from file_manager import initializer, saver
from os import system

def main():
    # Startup Settings [DEBUGGING]
    DEBUG : int = 0

    if (DEBUG == 0):
        # Initialize / Load Data #
        data = initializer()

        # Print Board #
        board = Drawer()

        # Main Loop
        while (True):
            system('cls')
            # Draw the board
            board.refresh(data)
            # Command loop
            command_handler.column_ops(data)
            # Exit Prompt
            if (command_handler.exit_program() == 'Y'):
                saver(data)
                system('cls')
                break

if __name__ == "__main__":
    main()

