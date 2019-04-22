import numpy as np
import pandas as pd

##Function that reads data from an online data source
def readData(dataLink,separator = ','):
    return pd.read_csv(dataLink,sep = separator)

##Function to verify column count is atleast 3
def checkColumns(dataFrame):
    if(dataFrame.shape[1]<3):
        return False
    return True

##Function that creates a dataframe from read data, and returns a dataframe if column count >=3, otherwise returns null
def importData(dataLink, separator = ','):
    df = readData(dataLink,separator)
    if(checkColumns(df)):
        return df
    return None
