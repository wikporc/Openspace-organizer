# Your code here
from pathlib import Path
from .table import Seat, Table

import random

class Openspace:
    def __init__(self,number_of_tables,table_capacity):
        self.number_of_tables=number_of_tables
        self.tables = [Table(capacity=table_capacity) for _ in range (self.number_of_tables)] 
        """iterating through all tables, creating number_of_tables instances of Table,
        each with 4 Seat object inside.""" 
        


    def organize(self,names_list):
        '''This method randomly assigns people to the Seat object in the different Table object'''
        random.shuffle(names_list)
        for name in names_list:
            assigned=False #flag to detect if the inner loop was never assigned the name
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned=True
                    break
            if not assigned: # this makes it that the ValueError below is printed only for names in names_list that could not be assigned, and not for every name.
                raise ValueError(f"No free seats available for {name}")

    def display(self):
        '''This method displays all the tables and their occupants'''
        for x in range(len(self.tables)):
            table=self.tables[x]
            print(f"Table: {x+1}")
            for seat in table.seats:
                if not seat.free:
                    print(seat.occupant)
                else:
                    print("Free")

    def store(self):
        '''This method stores the shuffled seat allocations in a list, that will later be saved in a file (see file_utils.py)
        '''
        lines=[]
        for x in range(len(self.tables)): 
            table=self.tables[x]
            lines.append(f"Table {x+1}")
            for seat in table.seats:
                if seat.free:
                    lines.append("Free")
                else:
                    lines.append(seat.occupant)
        return lines
    
    def __str__(self):
        a=1
        lines=[]
        for table in self.tables:
            lines.append(f"Table {a}:")
            lines.append(str(table)) #calls table.__str__()
            a=a+1
        return "\n".join(lines)

