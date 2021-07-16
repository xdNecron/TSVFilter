from os import sep
import pandas as pd 
from pandas import DataFrame
import time

start = time.time()

#* uploading experimental file 
tsv_file = open("XC-MS_test.tsv")
df = DataFrame(pd.read_csv(tsv_file, sep="\t"))


def pvalue_tol(pvalue_min, pvalue_max):

    global df

    df.sort_values(by=['pvalue'])

    # find pvalue_min
    rows = df.loc[df['pvalue'] >= pvalue_min].index
    first = rows[0]

    df2 = df[first:-1]  

    # find pvalue_max
    rows = df2.loc[df2['pvalue'] >= pvalue_max].index
    last_row = rows[0]
    last = last_row - first

    df_final = df2[0:last]

    df.drop(df.index, inplace=True)

    
    print(df_final)


def rt_tol():

    pass



def fold_tol():

    pass


def mz_tol():

    pass


def updown():

    pass


#pvalue_tol(0.1, 0.8)
#end = time.time()
#print(end - start)