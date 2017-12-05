
import sys
import csv
from Load_data import mydata_load
import pandas as pd
import numpy as np
from myConfiguration import myConfiguration
from machine_game import machine_game
'''
Created on Dec 1, 2017

@author: rezakhoshkangini
'''

def main():
    print("Hi I am reza")
    
    #load the csv file as a an object
    my_data=mydata_load()
    myData=my_data.getData()  #insert the data into a dictioney
    eData=myConfiguration(myData)
    # Implementing Machine learning
    machine_game(eData)
    
    
    print(myData)
    
if __name__ == '__main__':
   try:
        
        main()
   except Exception as ex:
        print(ex)


