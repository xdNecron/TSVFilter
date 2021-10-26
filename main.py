"""
TSVFilter v2.0.0 'main' script
- #! not yet completed, cannot replace v1.0.0 at the moment
- GUI is made using 'ttk' and 'ttkbootstrap'
- before running the script directly, make sure to install all requirements; otherwise run using the standalone executable

Original created by xdNecron.
Source code can be edited and distributed without distributor's financial profit.
"""


#* Import fundamentals
import random
import os
from os import sep, stat_result
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from typing import runtime_checkable
import webbrowser
import getpass

from ttkbootstrap import Style
from tkinter import ttk


#* import the filter & file-transfering functions
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
        filetypes=(("CSV and TSV files", "*.csv *.tsv"), ("All files", "*.*")))

    filter.obtain_source(list(source_files))

    fill_menu()


#* TABS
def tab_menu():

    global main_tab

    tab_selection = ttk.Notebook(root)
    tab_selection.grid(row=0, column=0)

    main_tab = ttk.Frame(tab_selection)
    tab2 = ttk.Frame(tab_selection)

    ttk.Label(tab2, text="lol").grid(row=0, column=0)

    tab_selection.add(main_tab, text="Main menu")
    tab_selection.add(tab2, text="Tab 2")


#* Generate file menu
def file_menu(): 

    global file_menu_frame, fill_menu, open_config

    file_menu_frame = ttk.LabelFrame(main_tab, text="Select files", padding=20)
    file_menu_frame.grid(row=1, column=0, padx=5, pady=5)

    #* File menu
    file_menu = ttk.Treeview(file_menu_frame)
    file_menu.heading(column="#0", text="Select a file")

    file_menu.grid(row=0, column=0)


    def fill_menu(): # function to display imported files and their collumns in 'file_menu'

        _files = ["1", "2", "3"]
        iid_value = 0 # order of items in list


        for source in filter.sources: 

            # insert the name of the file            
            file_name = os.path.basename(source) # get filename from path
            file_menu.insert("", END, text=file_name, iid=iid_value, open=FALSE)

            column_list = filter.get_dataframe_columns(source)

            sub_iid = 0 # order of subitems in parent columns
            parent = iid_value

            iid_value += 1

            for column in column_list: # inserts each column under corresponding file (parent)

                file_menu.insert("", END, text=column, iid=iid_value, open=FALSE)
                file_menu.move(iid_value, parent, sub_iid)
                
                sub_iid += 1
                iid_value += 1


        # open config window by double-clicking an item 
        def open_config():

            config_window()


            

#* configuration window
def config_window():

    # frame window 
    config_widow_frame = ttk.LabelFrame(main_tab, text="Configure filter options", padding=5)
    config_widow_frame.grid(row=1, column=1)
    
    # test button - for frame to show
    submit_button=ttk.Button(config_widow_frame, text="Open", style='primary.TButton', command=open_files, state=DISABLED)
    submit_button.grid(row=1, column=0, pady=5)





#* SCRIPT BODY
def main(root):
    
    tab_menu()
    file_menu()
    config_window()

    submit_button=ttk.Button(file_menu_frame, text="Open", style='primary.TButton', command=open_files)
    submit_button.grid(row=1, column=0, pady=5)

    root.mainloop()



#* PROCESS FUNCTIONS
def filter_process():

    for file in filter.sources:

        filter.get_dataframe(file)



#* execute the code
if __name__ == '__main__':
    main(root)