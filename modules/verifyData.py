import numpy as np
import pandas as pd
import collections

def test_create_dataframe(dataFrame,columnNames,dataTypes,nRows = 10):
    
    
    ##STEP - 1
    
    #Obtain actual column names from dataFrame
    actualColNames = list(dataFrame.columns)
    
    
    if(len(columnNames) == len(actualColNames)) : #Check for no. of columns match
        if(collections.Counter(columnNames) != collections.Counter(actualColNames)): #Check if column names match irrespective of order
            print("Column name mismatch")
            return False
    else:
        print("Column number mismatch")
        return False
            
    ## STEP-2
    
    #initialize step flag value to true
    flag = True
    
    #For each actual column name
    for i in actualColNames:
        flag = flag & (dataFrame[i].dtype == dataTypes[columnNames.index(i)]) #Check for that column name index data type
                                                                                #And update step flag
    
    if(flag==False):
        print("Data type mismatch")
        return False
    
    
    ## STEP-3
    
    if(nRows <= dataFrame.shape[0]): #check that number of rows are at least nRows
        flag = True
    else:
        print("Minimum number of rows criterion not met")
        flag = False
    
    #return flag value
    return flag

