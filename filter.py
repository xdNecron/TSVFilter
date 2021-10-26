from os import sep
from tkinter import messagebox
from tkinter.constants import TRUE
from typing import final
import pandas as pd 
from pandas import DataFrame


# ! experimental file (if needed for test)
#source_file = open("testfile.tsv")
#df = DataFrame(pd.read_csv(source_file, sep="\t"))

sources = []

#* obtain file uploaded thrugh GUI file dialog
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
        return list(tmp_df.columns)

        

"""
def missing_column(column):

    messagebox.showerror(
        "Error",
        f"A column required to run the script is missing: {column}"
    )


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
"""


# filter a column
def column_filter(*sources, columns, filter_type): # filter a list of collumns
#TODO - finish after completing configuration menu in 'main.py'

    def minmax_filter(columns, min, max):

        for column in columns:
            
            df.sort_values(by=[column], inplace=True, ignore_index=False)
            above_min_indexes = df.loc[df[column] >= min].index
            first_above = above_min_indexes[0]

            above_min = df[first_above:-1]
            df = DataFrame(above_min)


            df.sort_values(by=[column], inplace=True, ignore_index=True)
            under_max_indexes = df.loc[df[column] <= max].index
            last_under = under_max_indexes[0]

            under_max = df[0:last_under]
            df = DataFrame(under_max)

 
    for source in sources:
    
        #minmax_filter()
        #onevalue_filter()
        pass

        
    
    


def out_tsv(df):

    df.to_csv("out.tsv", sep="\t")


