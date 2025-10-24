import pandas as pd
from pathlib import Path
output_path=Path(__file__).parent/"allocation.csv" #this is the output file



def read_names (input_path=None): 
    if input_path is None:
        input_path=Path(__file__).parents[1]/"new_colleagues.csv"
    names_list=pd.read_csv(input_path,header=None)
    return names_list[0].tolist()
"""Did this to avoid immediately reading the file when importing file_utils.py onto main.py.
Wrapping it in a function allows us to call it in main.py when needed"""

def write_allocation(output_path,lines=None):
    with open(output_path, "w", encoding="utf-8-sig") as f:
        for line in lines:
            f.write(line + "\n")


