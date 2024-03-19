import pandas as pd
def conoutput(text):
    '''Used for console text output'''
    print(text)
def writefile(filename, inp):
    '''Used for writing files using built-in Python functions'''
    f = open(filename, 'a')
    f.write(inp)
    f.close()
def pd_writefile(filename, text):
    '''Used for writing files using Pandas library'''
    df = pd.to_csv(filename, text)