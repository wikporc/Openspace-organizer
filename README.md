# Openspace organizer

This Python package allows the user to allocate people to tables (seats) for openspace-style sessions.It provides simple Table and Seat models and an Openspace component to shuffle and assign names to seats.

## Project development
Took about 8-9 hours to make.
## Repository layout
- utils/
  - openspace.py — Openspace class that organizes and displays allocations
  - table.py — Table and Seat classes
  - file_utils.py — (expected) helpers to read/write participant lists and output (not included here)
  - __init__.py - empty initialiser file to allow importing modules
- main.py — example script that ties reading names, organizing and writing allocation
- new_colleagues.csv - the default input file. The script will read names from this file and assign the names listed in the file onto Tables by random. 


## Requirements
- Python 3.8+
- pandas - for reading the input csv file  


## Usage
- Run main.py. By default, it will use the new_colleagues.csv as an input_path. If you want to use a different
directory, provide it as an argument to the utils.file_utils.read_names().() function.
- The output path for the file with the allocated seats can be adjusted by changing the output_path variable in file_utils.py


#Changelog
- 1.0 - first working version of the script. 
- 1.1 - added __str__ methods for all 3 of the classes
- 1.2 - added the possibility to add a new



#To be done
- Consider raising a ValueError if there are more names than available seats. 
- the .left_capacity() method is currently unused
- the .remove_occupant() method is currently unused
- 
- Allow the possibility to define the room setup from a config.json file. Allow the possibility to change dynamically the setup and re-run the program.
- Make the program more dynamic and interactive by adding the possibilty to add someone in the room (a new colleague arriving or someone being late) and the possibilty to add a table if the room is full.
- Improve the algorithm to avoid having someone alone at a table
- Allow the possibility of which list (or black list) in the excel file → _X wants to be seated beside Y_ or _X doesn't want to be seated beside Y_
- Allow the possibility to ask : 
  - how much seats are in the room
  - how much people are in the room
  - how much seats are left