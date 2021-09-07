from os import sep
from tkinter.constants import FIRST, LAST
from tkinter import messagebox
from typing import final
import pandas as pd 
from pandas import DataFrame



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

    def check_existing(column):
        global df
        
        try:
            print(df.at[0, column])
        except:
            messagebox.showerror("Error", f"There was an error while importing the source file. *\nDoes not contain: {column}")

    check_existing(column)

    if min == "":
        
        pass
    else:

        try:

            min = float(min)
        
        except ValueError:

            messagebox.showerror("Error", "Please insert a number.")

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] >= min].index
        row = rows[0]

        df2 = df[row:-1]

        df = DataFrame(df2)
    

    if max == "":

        pass
    else:
        
        try:

            max = float(max)
        except ValueError:

            messagebox.showerror("Error", "Please insert a number.")

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] <= max].index
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

#filter('pvalue', "", 0.51)
