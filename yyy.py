from os import sep
import pandas as pd 
from pandas import DataFrame
import time


# obtain file uploaded thrugh GUI file dialog
def obtain_file(file):

    global source_file
    source_file = open(f"{file}")


    global df
    df = DataFrame(pd.read_csv(source_file, sep="\t"))


start = time.time()

# ! experimental file (if needed for test)
#tsv_file = open("XC-MS_test.tsv")
#df = DataFrame(pd.read_csv(tsv_file, sep="\t"))


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

    global pvalues

    pvalues = df2[0:last]
    df.drop(df.index, inplace=True)

    df.append(pvalues, ignore_index=True)

    print(pvalues)


def rt_tol():

    pass


def fold_tol():

    pass


def mz_tol():

    pass


def updown():

    pass


#pvalue_tol(0.5, 0.6)
rt_tol()