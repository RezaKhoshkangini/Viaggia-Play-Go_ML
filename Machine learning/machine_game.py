from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from my_classifier import my_classifier
from mycorrelation import mycorrelation
from Label_encode import Label_encode



'''
Created on Dec 5, 2017

@author: rezakhoshkangini
'''

def machine_game(mydata):
    #print(mydata)
    
    for key in mydata.keys():
        myInddata=mydata[key]
        mydata_data=pd.DataFrame(myInddata)
        #mycorrelation(mydata_data)
        
        # to find missing values
        print(mydata_data.isnull().sum())
        mycolumns=['MODEL_NAME','COUNTER_NAME','COMPLETED']
        testt=Label_encode(mydata_data,mycolumns)
        
        X=mydata_data.iloc[:, mydata_data.columns !='COMPLETED']
        y=mydata_data.iloc[:,-1]
        
        train, test, train_labels, test_labels=train_test_split(X, y, train_size=11, test_size=3, random_state=10)
        # Initialize our classifier
        model2=my_classifier(train, train_labels,test, test_labels)
        
        
        print(model2)

    # Evaluate accuracy
        print(accuracy_score(test_labels, preds))
        
        
        print("stop")
        

    
    
     
     