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
    # data = load_csv_data(filename)
    # test_load = initializer()
    # print(f"{test_load} \nTEST LOAD NONE: {test_load == None}")
    # test_struct = [["colname", [ ["entname1", "entcont1"], ["entname2", "entcont2"], ["entname3", "entcont3"] ] ],
    #                ["colname2", [ ["entname1", "entcont1"], ["entname2", "entcont2"], ["entname3", "entcont3"] ] ]]
    # save_csv_data(filename, test_struct)
    # data = load_csv_data(filename)
    # test_load = initialize(data)
    pass