import pandas as pd
import numpy as np
import glob



'''
Created on Dec 1, 2017


@author: rezakhoshkangini
'''

class mydata_load(object):
    '''
    classdocs
    '''
    
    #my_path='/Users/rezakhoshkangini/Documents/workspace/Drexel_Work/Play&GO-ML-PS'
    def __init__(self):
        #self.path = path
        self.getData()
        

    def getData(self):
        path='/Users/rezakhoshkangini/Documents/workspace/Drexel_Work/Play&GO-ML-PS'
        csvFiles = glob.glob(path + "/*.csv")
        listoflist={}
        for files in csvFiles:
            csvlist=pd.read_csv(files)
            listoflist[files]=csvlist
            #HisData(listoflist) # caculating the Histogram      
            df = pd.DataFrame(csvlist)
        
        
        #newdata = df[['PLAYER_ID', 'MODEL_NAME','TARGET','BONUS_SCORE','START','END','WEEK','COUNTER_NAME','COMPLETED']]
        newdata = df[['PLAYER_ID', 'MODEL_NAME','TARGET','BONUS_SCORE','COUNTER_NAME','COMPLETED']]
        newdata=newdata[(newdata.MODEL_NAME == 'absoluteIncrement')|(newdata.MODEL_NAME=='percentageIncrement')]
        return newdata
# 

        
    
#  
        