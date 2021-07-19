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

    df2 = df[first:-1]  


    # find pvalue_max
    rows = df2.loc[df2['pvalue'] >= pvalue_max].index
    print(rows)
    last = rows[0] - first


    pvalues = df2[0:last]

    df = DataFrame(pvalues)


def rt_tol(rt_min, rt_max):

    global df

    df.sort_values(by=['rtmed'], inplace=True, ignore_index=True)


    # find rt_min
    rows = df.loc[df['rtmed'] >= rt_min].index
    first = rows[0]


    df2 = df[first:-1]  


    # find rt_max
    rows = df2.loc[df2['rtmed'] >= rt_max].index
    last = rows[0] - first

    rt = df2[0:last]

    df = DataFrame(rt)


    # ! tepmorary, for testing
    #df.to_csv("out.tsv", sep="\t")


def fold_tol(fold_min, fold_max):

    global df

    df.sort_values(by=['fold'], inplace=True, ignore_index=True)


    # find fold_min
    rows = df.loc[df['fold'] >= fold_min].index
    first = rows[0]

    df2 = df[first:-1]


    # find fold_max
    rows = df2.loc[df2['fold'] >= fold_max].index
    last = rows[0] - first

    fold = df2[0:last]

    df = DataFrame(fold)

    # ! tepmorary, for testing
    #df.to_csv("out.tsv", sep="\t")


def mz_tol(mz_min, mz_max):

    global df

    df.sort_values(by=['mzmed'], inplace=True, ignore_index=True)


    # find mz_min
    rows = df.loc[df['mzmed'] >= mz_min].index
    first = rows[0]


    df2 = df[first:-1]  


    # find mz_max
    rows = df2.loc[df2['mzmed'] >= mz_max].index
    last = rows[0] - first

    rt = df2[0:last]

    df = DataFrame(rt)


    # ! tepmorary, for testing
    #df.to_csv("out.tsv", sep="\t")



# TODO finish this function after recreating gui
def updown(up_down):

    global df

    df.sort_values(by=['updown'], inplace=True, ignore_index=True)


    if up_down == "UP":

        rows = df.loc[df['updown'] == "DOWN"].index
        lastdown = rows[-1]
        first = lastdown + 1

        df2 = df[first:-1]

        df = DataFrame(df2)

    elif up_down == "DOWN":

        rows = df.loc[df['updown'] == "UP"].index
        last = rows[0] + 1

        df2 = df[0:last]

        df = DataFrame(df2)


    empty = ""
    nans = df.loc[df['updown'] == empty].index
    print(nans)

    for x in nans:

        df.drop(df[x])


def out_tsv():

    df.to_csv("out.tsv", sep="\t")


# TODO find out how to do this and do it wtf even are those comments
def heatmap():

    pass


#pvalue_tol(0.5, 0.51)

#rt_tol(1, 3)

#fold_tol(5, 10)

#mz_tol(400, 800)

#updown("UP")

#end = time.time()
#print(end - start)