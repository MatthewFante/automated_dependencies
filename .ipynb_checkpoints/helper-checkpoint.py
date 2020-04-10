from time import sleep
from IPython.display import clear_output
import sys

def five_dots(sec):
    elipsis = '.....'
    for dot in elipsis:
        sleep(sec/len(elipsis))
        print(dot, end = '')


        
def check_dependency_prompt(dependency_list):
    yn = ''
    
    print("Greetings! I can help you install or update the dependencies for this notebook!")
    
    while yn.lower() not in ['yes', 'no']:
        clear_output()
        yn = input("Do you want to check dependencies for updates? ")
    
    if yn.lower() == 'yes':
        clear_output()
        print("Great! Let's get started", end='')
        five_dots(1)
        check_dependencies(dependency_list)
        clear_output()
        
    elif yn.lower() == 'no':
        clear_output()
        print("Okay, attempting to import dependencies", end='')
        five_dots(1)
        
        
def check_dependencies(list_of_dependencies):
    dependency_summary = []
    for library in list_of_dependencies:
        clear_output()
        print('Checking', library, end = '')
        five_dots(1)
        clear_output()
        
        if library in sys.modules:
            dependency_summary.append(library + "is ready to use")
        elif library not in sys.modules:
            dependency_summary.append(library + "is NOT ready to use")       
#     if ready == len(list_of_dependencies):
#         print("All dependencies are ready to import!")
#     else:
#         print("Please run the cell below to install or update dependencies")
    
    print(dependency_summary)
        
#     if ready < len(list_of_dependencies):
#         print("Please run the cell below to install or update dependencies")

        
        
        
        

# if install_dep_yn.lower() == 'yes':
#     print("Great! Let's get started!")
#     sleep(1)
#     clear_output()
#     print("Checking pandas")
#     
#     sleep(1)
#     clear_output()
#     print("Checking sqlite3")
#     !conda install --yes --prefix {sys.prefix} sqlite3
#     sleep(1)
#     clear_output()
#     print("Checking matplot")
#     !conda install --yes --prefix {sys.prefix} matplotlib
#     sleep(1)
#     clear_output()
#     print("Checking bokeh")
#     !conda install --yes --prefix {sys.prefix} bokeh
#     sleep(1)
#     clear_output()
#     print("SUCCESS! Dependencies are ready to use!")

# elif install_dep_yn.lower() == 'no':

#     elipsis = '.......'
#     for period in elipsis:
#         sleep(.5)
#         print(period, end='')
#     sleep(2)
    
# import pandas as pd
# from pandas.io.json import json_normalize
# import sqlite3
# import matplotlib.pyplot as plt
# from bokeh.plotting import ColumnDataSource, figure, show, output_notebook

# clear_output()
# print("SUCCESS! Dependencies are ready to use!")

# drag_race_data_base = sqlite3.connect("drag_race_data.db")