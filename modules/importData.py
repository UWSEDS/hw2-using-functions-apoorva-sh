import numpy as np
import pandas as pd

def importData(dataLink, seperator = ','):
    df = pd.read_csv(dataLink,sep=seperator)
    return df
