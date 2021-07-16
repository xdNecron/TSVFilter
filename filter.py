from os import sep
from tkinter.constants import LAST
import pandas as pd 
from pandas import DataFrame
import time

#start = time.time()

# obtain file uploaded thrugh GUI file dialog
def obtain_file(file):

    global source_file
    source_file = open(f"{file}")


    global df
    df = DataFrame(pd.read_csv(source_file, sep="\t"))


start = time.time()

# ! experimental file (if needed for test)
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
    last = rows[0] - first

    global pvalues

    pvalues = df2[0:last]
    df.drop(df.index, inplace=True)

    print(pvalues)

    #return pvalues


def rt_tol(rt_min, rt_max):

    global pvalues
    global rt_filter

    rt_filter = DataFrame(pvalues)

    rt_filter.sort_values(by=['rtmed'])
    print(rt_filter)


    # find rt_min
    rows = rt_filter.loc[rt_filter['rtmed'] >= rt_min].index
    #print(rows)
    first = rows[0]

    rt_filter2 = rt_filter[first:-1]
    #print(rt_filter2)

    # find rt_max
    rows = rt_filter2.loc[rt_filter2['rtmed'] >= rt_max].index
    #last = rows[0] - first
    #print(rows)

    #rt_final = rt_filter2[0:last]

    #print(rt_final)


def fold_tol():

    pass


def mz_tol():

    pass


def updown():

    pass

#pvalue_tol(0.5, 0.6)
#rt_tol(0, 3)
#end = time.time()
#print(end - start)