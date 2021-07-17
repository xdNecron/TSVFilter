from os import sep
from tkinter.constants import LAST
import pandas as pd 
from pandas import DataFrame
import time


#start = time.time()

# ! experimental file (if needed for test)
#source_file = open("XC-MS_test.tsv")
#df = DataFrame(pd.read_csv(source_file, sep="\t"))


# obtain file uploaded thrugh GUI file dialog
def obtain_file(file):

    global source_file
    source_file = open(f"{file}")

    global df
    df = DataFrame(pd.read_csv(source_file, sep="\t"))



def pvalue_tol(pvalue_min, pvalue_max):

    global df

    df.sort_values(by=['pvalue'], inplace=True, ignore_index=True)


    # find pvalue_min
    rows = df.loc[df['pvalue'] >= pvalue_min].index
    first = rows[0]
    print(first)

    df2 = df[first:-1]  


    # find pvalue_max
    rows = df2.loc[df2['pvalue'] >= pvalue_max].index
    last = rows[0] - first


    pvalues = df2[0:last]

    df = DataFrame(pvalues)
    print(df)


def rt_tol(rt_min, rt_max):

    global df

    df.sort_values(by=['rtmed'], inplace=True, ignore_index=True)


    # find rt_min
    rows = df.loc[df['rtmed'] >= rt_min].index
    first = rows[0]
    print(first)


    df2 = df[first:-1]  


    # find rt_max
    rows = df2.loc[df2['rtmed'] >= rt_max].index
    last = rows[0] - first

    rt = df2[0:last]

    df = DataFrame(rt)
    print(df)


    # ! tepmorary, for testing
    #df.to_csv("out.tsv", sep="\t")


def fold_tol():

    pass


def mz_tol():

    pass


def updown():

    pass

#pvalue_tol(0.5, 0.51)
#rt_tol(1, 3)
#end = time.time()
#print(end - start)