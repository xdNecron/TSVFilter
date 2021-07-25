from os import sep
from tkinter.constants import FIRST, LAST
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


def filter(column, min, max):

    global df
    

    if min == "":
        
        pass
    else:

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] >= float(min)].index
        row = rows[0]

        df2 = df[row:-1]

        df = DataFrame(df2)

    
    if max == "":

        pass
    else:

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] <= float(max)].index
        row = rows[-1]

        df2 = df[0:row]

        df = DataFrame(df2)


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
        last = rows[0]

        df2 = df[0:last]

        df = DataFrame(df2)


    empty = ""
    nans = df.loc[df['updown'] == empty].index
    print(nans)

    for x in nans:

        df.drop(df.index == x)


def out_tsv():

    df.to_csv("out.tsv", sep="\t")


# TODO find out how to do this and do it wtf even are those comments
def heatmap():

    pass

#filter('pvalue', "", 0.51)
