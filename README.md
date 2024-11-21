# cmd-kanban
A kanban board as a commandline program for task tracking, built in Python 3.

## Version
- Current Version: 1.0
- Status: Usable, 
- Development Status: Hiatus

### Limitations
- Column CRUD is not Implemented
- It is assumed that the screen only shows 4 columns, and only 4 columns are initialized and not editable

## Setup
### Requirements
- Python 3

## Usage
1. Open the program through the python script (main.py) or through the command line.

### Main Loop
1. Draw Board
2. Get User Input [Column Operations: Column Selection / Program Exit]
3. Get User Input [Entry Selection]
   1. Get User Input [Entry Operations: Select / Edit / Add / Move / Remove]
   2. Refresh Board
4. Repeat Until User Exits at Step 2.

### Columns CRUD
- <WIP : To be completed when CRUD for columns is completed>

### Entries CRUD
1. CREATE : to create an entry, 
   1. in the entry operations section, 
   2. enter '+' then enter the name, 
   3. and then the content of the entry
2. READ : to view an entry's contents,
   1. in the entry operations section,
   2. enter the 'ID' of the entry to view (present in the drawn board)
3. UPDATE : to edit an entry, 
   1. in the entry operations section, 
   2. enter 'e', 
   3. then enter the 'ID' of the entry to edit (present in the drawn board) 
   4. and then enter the new name, 
   5. and the new content (enter with blank text to not edit the name, or the content)
4. DELETE : to delete an entry, 
   1. in the entry operations section, 
   2. enter 'rm' 
   3. and then select the ID of the entry to delete (present in the drawn board)
5. MOVE : to move an entry to another column,
   1. in the entry operations section,
   2. enter 'ID' of the entry to move
   3. then enter 'ID' of the column to move to