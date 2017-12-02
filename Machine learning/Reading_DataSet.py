'''
Created on Dec 1, 2017

@author: rezakhoshkangini
'''

class Reading_Data(object):
    
    def SimpleR(self):
        print("this is SImple function")
        return 5+4
        
    def Mlt(self):
        print("this is Mlt function")
        return 4*3 
       
    def Reading_Challenge(self):
        path = '/Users/rezakhoshkangini/Documents/CH/Player_Modeling/All'
        csvFiles = glob.glob(path + "/*.csv")
        listoflist={}
        for files in csvFiles:
            csvlist=pd.read_csv(files)
            listoflist[files]=csvlist
            #HisData(listoflist) # caculating the Histogram      
            df = pd.DataFrame(csvlist)
        return df 