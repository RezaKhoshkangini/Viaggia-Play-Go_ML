from sklearn.neighbors import KNeighborsClassifier

'''
Created on Dec 5, 2017

@author: rezakhoshkangini
'''
def my_classifier(X_train, X_test, y_train, y_test):
    
    
    model = KNeighborsClassifier(n_neighbors=1)
    model.fit(X_train, y_train)
    
    return model
    