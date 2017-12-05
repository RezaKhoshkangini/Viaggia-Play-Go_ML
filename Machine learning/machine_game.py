from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np
from my_classifier import my_classifier
'''
Created on Dec 5, 2017

@author: rezakhoshkangini
'''

def machine_game(mydata):
    #print(mydata)
    
    for key in mydata.keys():
        myInddata=mydata[key]
        mydata_data=pd.DataFrame(myInddata)
        

        X=mydata_data.iloc[:, mydata_data.columns !='COMPLETED']
        y=mydata_data.iloc[:,-1]
        
        train, test, train_labels, test_labels=train_test_split(X, y, train_size=11, test_size=3, random_state=0)
        # Initialize our classifier
        Knn=my_classifier(train, test, train_labels, test_labels)
        
        

        # Train our classifier
        model = gnb.fit(train, train_labels)

        # Make predictions
        preds = gnb.predict(test)
        print(preds)

    # Evaluate accuracy
        print(accuracy_score(test_labels, preds))
        
        
        print("stop")
        

    
    
     
     