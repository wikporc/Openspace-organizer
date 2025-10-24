import pandas as pd
from pathlib import Path


class Table:
    def __init__(self,capacity):
        self.capacity=capacity
        self.seats = [Seat() for _ in range (self.capacity)] 
        """ this creates a loop that runs capacity times 
        in each iteration creating a new Seat() object -> 
        Then it collects these objects into a list
        TLDR: this makes the table automatically have a list of Seat objects equal to  its capacity """
        
    def has_free_spot(self):
        #self.seats is our list of Seat() objects
        
        for seat in self.seats:
            if seat.free==True:
                return True # If there is a free seat, this returns True and terminates the loop. 
        return False # if there is no seat with seat.free==True, it goes here and returns false.
        
            
    def assign_seat(self,name):
        
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return seat
            
        
    def left_capacity(self):
            remaining_spots=0
            for seat in self.seats:
                if seat.free:
                    remaining_spots=remaining_spots+1
            return remaining_spots


# Your code here


class Seat:
    def __init__ (self): # initially tried doing (self,free,occupant) -> But since we assign default values, we do this instead
        self.free = True # default value -> seat is free 
        self.occupant = None # by default there is no occupant. If a seat is free, it cannot have an occupant
    

        
    def set_occupant(self,name):
        if self.occupant is None:
            self.free = False # this makes the seat taken
            self.occupant= name # this assigns the new occupant
            return (self.occupant)
            
        else:
            raise ValueError(f"Seat is already taken by: {self.occupant}")



    def remove_occupant(self):
        occupant = self.occupant
        self.occupant= None
        self.free= True