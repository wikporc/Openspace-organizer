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
        #the capacity is hard-coded to 4, change it later


    def organize(self,names_list):
        random.shuffle(names_list)
        for name in names_list:
            assigned=False #flag to detect if the inner loop was never assigned the name
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    assigned=True
                    break
            if not assigned: # this makes it that the ValueError below is printed only for names in names_list that could not be assigned.
                raise ValueError(f"No free seats available for {name}")

    def display(self):
        for x in range(len(self.tables)):
            table=self.tables[x]
            print(f"Table: {x+1}")
            for seat in table.seats:
                if not seat.free:
                    print(seat.occupant)
                else:
                    print("Free")

    def store(self):
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