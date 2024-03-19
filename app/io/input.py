import pandas as pd
def coninput():
    '''Used for console text input'''
    return input()
def readfile(filename):
    '''Used for reading files using built-in Python functions'''
    f = open(filename, 'r')
    return f
def pd_readfile(filename):
    '''Used for reading files using Pandas library'''
    df = pd.read_csv(filename)
    return df