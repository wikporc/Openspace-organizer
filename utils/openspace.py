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
    
    def add_table(self,capacity=4):
        '''This method adds a table, with a specified capacity (4 by default)'''
        self.tables.append(Table(capacity))

    def add_colleague(self,name):
        '''This method can be used to add a new colleague and assign them a seat. If there are no free seats left, it asks the user to add a new table and assigns the new person to that table'''
        for table in self.tables:
            if table.has_free_spot():
                table.assign_seat(name)
                return
        print("No free seats available. Do you want to add a new table?")
        answer_table=input("Enter Y or N:")
        if answer_table.lower() == "y":
            print ("Adding Table:")
            answer_capacity=int(input("Specify table's capacity"))
            self.add_table(answer_capacity)
            self.add_colleague(name)
        elif answer_table.lower() == "n":
            print("Not doing anything. You can add a table later using .add_table()")
        else:
            print  ("Please enter Y or N:")


    def prevent_lonely_person(self):
        
        lonely_tables= [table for table in self.tables if (table.capacity-table.left_capacity())==1]

        """This method will iterate through all tables, detect ones with only 1 occupant, and try to move someone from 
        a table with more that 1 occupant to that table"""
        for table in lonely_tables:
                occupied_count = table.capacity - table.left_capacity() #calculates the number of people occupying the table
                print(f"Checking table {self.tables.index(table)+1}, occupied_count={occupied_count}")

                for donating_table in self.tables:
                    if donating_table is table:
                        continue #skip the table with one person- it ensure the inner loop only considers the donating_table as a potential source for moving someone
                       
                    donating_occupied_count=donating_table.capacity-donating_table.left_capacity()
                    print(f"  Donor Table {self.tables.index(donating_table)+1}, donating_occupied_count={donating_occupied_count}")
                    """ Have to do this weirdness below to check if the donating table has more than one occupant - had to do this 
                       to prevent a situation where if two tables are having only 1 person,
                       it would swap them and make another two 1-person tables"""
                    if donating_occupied_count>1:
                           #find a seat to move
                        for seat in donating_table.seats:
                            if not seat.free:
                                person_to_move=seat.occupant
                                seat.remove_occupant()
                                table.assign_seat(person_to_move)
                                print(f"    Moved {person_to_move} from Table {self.tables.index(donating_table)+1} to Table {self.tables.index(table)+1}")
                                break  # move only one person at a time
                           
                        # Recalculate occupied_count after moving someone
                    occupied_count = table.capacity - table.left_capacity()
                    if occupied_count > 1:
                        break  # table no longer lonely
                                   
                                               
                    
                       
                    




