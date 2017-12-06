from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

import seaborn as sns
import matplotlib.pyplot as plt
import time
 
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
 
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

'''
Created on Dec 5, 2017

@author: rezakhoshkangini
'''
def my_classifier(X_train, Y_train, X_test, Y_test, verbose = True):
    
    dict_classifiers = {
        "Logistic Regression": LogisticRegression(),
        "Nearest Neighbors": KNeighborsClassifier(),
        "Linear SVM": SVC(),
        "Gradient Boosting Classifier": GradientBoostingClassifier(),
        "Decision Tree": tree.DecisionTreeClassifier(),
        "Random Forest": RandomForestClassifier(n_estimators = 18),
        "Neural Net": MLPClassifier(alpha = 1),
        "Naive Bayes": GaussianNB()
        }
    no_classifiers = len(dict_classifiers.keys())

    df_results = pd.DataFrame(data=np.zeros(shape=(no_classifiers,4)), columns = ['classifier', 'train_score', 'test_score', 'training_time'])
    count = 0
    for key, classifier in dict_classifiers.items():
        t_start = time.clock()
        classifier.fit(X_train, Y_train)
        t_end = time.clock()
        t_diff = t_end - t_start
        train_score = classifier.score(X_train, Y_train)
        test_score = classifier.score(X_test, Y_test)
        df_results.loc[count,'classifier'] = key
        df_results.loc[count,'train_score'] = train_score
        df_results.loc[count,'test_score'] = test_score
        df_results.loc[count,'training_time'] = t_diff
        if verbose:
            print("trained {c} in {f:.2f} s".format(c=key, f=t_diff))
        count+=1
    return df_results
    