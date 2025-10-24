from utils.openspace import Openspace 
from utils.table import Seat, Table
from utils.file_utils import read_names,write_allocation, output_path
""" had to do this utils.openspace & utils.table cause otherwise python wouldn't find it as it was not in the main folder. 
also had to create __init__.py in the utils folder, this tells Python that the folder is a package. It allows us do to imports like from folder.module import Class
"""
names_list=read_names() #You can use your own input path as an argument here- uses the default one in the main directory if none provided

instance=Openspace(4,6)
instance.organize(names_list)
instance.display()
lines=instance.store()
write_allocation(output_path,lines) 
