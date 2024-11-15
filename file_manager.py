###########################################################################################
# CMD - Kanban (Python)
###########################################################################################

import csv
from typing import List
from classes_util import Column, Entry
from operations_util import create_columns
filename = "kanban.csv"

"""
Column-Entry List:
[ [ name, [[name,content],...]], ... ]
"""
###########################
## FILE LOADING / SAVING ##
###########################

# Load CSV Data
def load_csv_data(filename : str = filename) -> list:
    loaded_data = []
    try :
        with open(filename,'r') as data:
            for row in csv.reader(data):
                loaded_data.append(row)
    except Exception:
        # No Data Loaded : Loading Defaults
        return get_defaults()
    return loaded_data
    
# Save CSV Data
def save_csv_data(data : list, filename : str = filename) -> None:
    sav_csv = open(filename, 'w+', newline ='')
    with sav_csv:
        writer = csv.writer(sav_csv)
        writer.writerows(data)

#########################
## DATA INITIALIZATION ##
#########################

# Load Column-Entry Data
def initialize(data : list) -> list:
    if (data == None):
        return None
    else:
        return create_columns(data)

# Defaults
def get_defaults() -> list:
    defaults = [["Research", ""],["Planning", ""],["Doing", ""],["Done", ""]]
    return defaults

#################
## INITIALIZER ##
#################

# Returns Data Proper
def initializer() -> List[Column]:
    loaded_data = load_csv_data(filename)
    return initialize(loaded_data)

# Gets Data and Writes
def saver(data : List[Column]) -> None:
    to_list = []
    for row in data:
        to_list.append(row.as_list())
    save_csv_data(to_list, filename)


# VALIDATION
if __name__ == "__main__":
    pass
    # data = load_csv_data(filename)
    # test_load = initializer()
    # print(f"{test_load} \nTEST LOAD NONE: {test_load == None}")
    # test_struct = [["colname", [ ["entname1", "entcont1"], ["entname2", "entcont2"], ["entname3", "entcont3"] ] ],
    #                ["colname2", [ ["entname1", "entcont1"], ["entname2", "entcont2"], ["entname3", "entcont3"] ] ]]
    # save_csv_data(filename, test_struct)
    # data = load_csv_data(filename)
    # test_load = initialize(data)


# # 1. File Opening
# file = open('kanban.txt', 'r')
# for line in file:
#     print (line)


# # 2. File Saving
# # Save Entries - Save the entry contents on the file
# def save_entries():
#     # File management
#     pass

# # Parse Entries - Parse the text file contents through board_drawer
# def parse_entries():

#     pass

# # Save Columns - Save the entry contents on the file
# def save_columns():
#     pass

# # Parse Columns - Parse the text file contents through board_drawer
# def parse_columns():
#     pass

# # 3. Importer

# # 4. Exporter


# # GEEKS FOR GEEKS SAMPLE CODE: https://www.geeksforgeeks.org/file-handling-python/
# # a file named "geek", will be opened with the reading mode.
# file = open('geek.txt', 'r')

# # This will print every line one by one in the file
# for each in file:
#     print (each)

# # Python code to illustrate read() mode
# file = open("geeks.txt", "r") 
# print (file.read())

# # Python code to illustrate split() function
# with open("geeks.txt", "r") as file:
#     data = file.readlines()
#     for line in data:
#         word = line.split()
#         print (word)

# # Python code to create a file
# file = open('geek.txt','w')
# file.write("This is the write command")
# file.write("It allows us to write in a particular file")
# file.close()

# # Python code to illustrate with() alongwith write()
# with open("file.txt", "w") as f: 
#     f.write("Hello World!!!") 

# # Python code to illustrate append() mode
# file = open('geek.txt', 'a')
# file.write("This will add this line")
# file.close()

# import os

# def create_file(filename):
#     try:
#         with open(filename, 'w') as f:
#             f.write('Hello, world!\n')
#         print("File " + filename + " created successfully.")
#     except IOError:
#         print("Error: could not create file " + filename)

# def read_file(filename):
#     try:
#         with open(filename, 'r') as f:
#             contents = f.read()
#             print(contents)
#     except IOError:
#         print("Error: could not read file " + filename)

# def append_file(filename, text):
#     try:
#         with open(filename, 'a') as f:
#             f.write(text)
#         print("Text appended to file " + filename + " successfully.")
#     except IOError:
#         print("Error: could not append to file " + filename)

# def rename_file(filename, new_filename):
#     try:
#         os.rename(filename, new_filename)
#         print("File " + filename + " renamed to " + new_filename + " successfully.")
#     except IOError:
#         print("Error: could not rename file " + filename)

# def delete_file(filename):
#     try:
#         os.remove(filename)
#         print("File " + filename + " deleted successfully.")
#     except IOError:
#         print("Error: could not delete file " + filename)


# if __name__ == '__main__':
#     filename = "example.txt"
#     new_filename = "new_example.txt"

#     create_file(filename)
#     read_file(filename)
#     append_file(filename, "This is some additional text.\n")
#     read_file(filename)
#     rename_file(filename, new_filename)
#     read_file(new_filename)
#     delete_file(new_filename)

# # https://www.geeksforgeeks.org/load-csv-data-into-list-and-dictionary-using-python/
# # importing module 
# import csv
  
# # csv fileused id Geeks.csv
# filename="Geeks.csv"
 
# # opening the file using "with"
# # statement
# with open(filename,'r') as data:
#    for line in csv.reader(data):
#             print(line)
         
# # then data is read line by line 
# # using csv.reader the printed 
# # result will be in a list format 
# # which is easy to interpret

# import csv

# filename ="Geeks.csv"

# # opening the file using "with"
# # statement
# with open(filename, 'r') as data:
#     for line in csv.DictReader(data):
#         print(line)


# from csv import DictReader
# # open file in read mode
# with open("geeks.csv", 'r') as f:
     
#     dict_reader = DictReader(f)
     
#     list_of_dict = list(dict_reader)
   
#     print(list_of_dict)
