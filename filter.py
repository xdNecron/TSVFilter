from os import sep
from tkinter import messagebox
from typing import final
import pandas as pd 
from pandas import DataFrame



#start = time.time()

# ! experimental file (if needed for test)
#source_file = open("XC-MS_test.tsv")
#df = DataFrame(pd.read_csv(source_file, sep="\t"))

sources = []

# obtain file uploaded thrugh GUI file dialog
def obtain_source(source):

    global get_dataframe, get_dataframe_columns

    global sources
    sources = list(source)

    
    def get_dataframe(source):

        global df
        df = DataFrame(pd.read_csv(source, sep="\t"))  


    def get_dataframe_columns(source):

        global file_columns

        tmp_df = DataFrame(pd.read_csv(source, sep="\t"))
        return tmp_df.columns


"""
def missing_column(column):

    messagebox.showerror(
        "Error",
        f"A column required to run the script is missing: {column}"
    )
"""

def filter(column, min, max):

    global df
    global missing

    if min == "":
            
        pass    
    elif column in df.columns:

        try:

            min = float(min)
        
        except ValueError:

            messagebox.showerror("Error", "Please insert a number.")

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] >= min].index
        row = rows[0]

        df2 = df[row:-1]

        df = DataFrame(df2)

    else:
        missing = column
        raise NameError("a column is missing.")

    if max == "":

        pass
    elif column in df.columns:
        
        try:

            max = float(max)
        except ValueError:

            messagebox.showerror("Error", "Please insert a number.")

        df.sort_values(by=[column], inplace=True, ignore_index=True)

        rows = df.loc[df[column] <= max].index
        row = rows[-1]

        df2 = df[0:row]

        df = DataFrame(df2)

    else:
        missing = column

        raise NameError("a column is missing.")



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


