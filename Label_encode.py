import pandas as pd
import numpy as np
from sklearn import preprocessing
'''
Created on Dec 6, 2017

@author: rezakhoshkangini
'''


def Label_encode(df,columns):
    OldData=df
    for col in columns:
        le = preprocessing.LabelEncoder()
        col_values_unique = list(df[col].unique())
        le_fitted = le.fit(col_values_unique)
 
        col_values = list(df[col].values)
        le.classes_
        col_values_transformed = le.transform(col_values)
        df[col] = col_values_transformed    
        
    return df