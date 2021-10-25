"""
TSVFilter v2.0.0 'main' script
- #! not yet completed, cannot replace v1.0.0 at the moment
- GUI is made using 'ttk' and 'ttkbootstrap'
- before running the script directly, make sure to install all requirements; otherwise run using the standalone executable

Original created by xdNecron.
Source code can be edited and distributed without distributor's financial profit.
"""


#* Import fundamentals
import os
from os import stat_result
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from typing import runtime_checkable
import webbrowser
import getpass

from ttkbootstrap import Style
from tkinter import ttk


#* import the filter algorithm
import filter


root = Tk()
root.title("TSVFilter v2.0.0")
#root.geometry('1280x720')
root.resizable(height=False, width=False)

# configure style of the application
style = Style(theme='lumen')


# open files and send them to the filter script
def open_files():

    source_files = filedialog.askopenfilenames(
        title="Choose a file",
        filetypes=[("CSV and TSV files", ["*.csv", "*.tsv"])])

    filter.obtain_source(list(source_files))

    fill_menu()


#* Generate file menu
def file_menu(): 

    global file_menu_frame, fill_menu

    file_menu_frame = ttk.LabelFrame(root, text="Select files", padding=20)
    file_menu_frame.grid(row=0, column=0, padx=5, pady=5)

    #* File menu
    file_menu = ttk.Treeview(file_menu_frame)
    file_menu.heading(column="#0", text="Select a file")

    file_menu.grid(row=0, column=0)


    def fill_menu():

        _files = ["1", "2", "3"]
        iid_value = 0 # order of items in list


        for source in filter.sources: # display each one of uploaded files and its collumns

            # insert the name of the file            
            file_name = os.path.basename(source)
            file_menu.insert("", END, text=file_name, iid=iid_value, open=FALSE)
            
            parent = iid_value # get iid of current parent 
            sub_iid = 0 # order of subitems in parent columns

            column_list = filter.get_dataframe_columns(source) # returns a list of columns in current file
            
            for column in column_list: # inserts each column under corresponding file (parent)
                
                file_menu.insert("", END, text=column, iid=iid_value, open=FALSE)
                file_menu.move(iid_value, parent, sub_iid)

                sub_iid += 1 
                iid_value += 1


# script body
def main(root):
    
    file_menu()

    submit_button=ttk.Button(file_menu_frame, text="Submit", style='primary.TButton', command=open_files)
    submit_button.grid(row=1, column=0, pady=5)

    root.mainloop()



def filter_process():

    for file in filter.sources:

        filter.get_dataframe(file)




#* execute the code
if __name__ == '__main__':
    main(root)