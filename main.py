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
from os import scandir, sep, stat_result, supports_dir_fd
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from typing import runtime_checkable
import webbrowser
import getpass
from numpy import right_shift
import getpass

from ttkbootstrap import Style
from tkinter import ttk


#* import the filter & file-transfering functions
import filter

#* app window
def window():

    global root, style

    root = Tk()
    root.title("TSVFilter v2.0.0")
    #root.geometry('1280x720')
    root.resizable(height=False, width=False)

    # configure style of the application
    style = Style(theme='flatly')

    global iid_value
    iid_value = 0

    return root


# open files and send them to the filter script
def open_files():

    global iid_value

    source_files = filedialog.askopenfilenames(
        title="Choose a file",
        filetypes=(("CSV and TSV files", "*.csv *.tsv"), ("All files", "*.*")))

    filter.obtain_source(list(source_files))

    iid_value = fill_menu()
    

#* TABS
def tab_menu():

    global main_tab

    tab_selection = ttk.Notebook(root)
    tab_selection.grid(row=0, column=0)

    main_tab = ttk.Frame(tab_selection)
    tab2 = ttk.Frame(tab_selection)

    ttk.Label(tab2, text="lol").grid(row=0, column=0)

    tab_selection.add(main_tab, text="Main menu")
    tab_selection.add(tab2, text="Tab 2", state=DISABLED)


#* Generate file menu
def file_menu(): 

    global file_menu_frame, fill_menu, open_config, iid_value, current_iid

    file_menu_frame = ttk.LabelFrame(main_tab, text="Select files", padding=20)
    file_menu_frame.grid(row=1, column=0, padx=5, pady=5)

    #* File menu
    file_menu = ttk.Treeview(file_menu_frame)
    file_menu.heading(column="#0", text="Select a file")

    file_menu.grid(row=0, column=0)

    # scrollbar
    file_menu_scrollbar = ttk.Scrollbar(file_menu_frame, orient='vertical', command=file_menu.yview)
    file_menu_scrollbar.grid(row=0, column=1, ipady=96)

    file_menu.configure(yscrollcommand=file_menu_scrollbar.set)


    def fill_menu(): # function to display imported files and their collumns in 'file_menu'

        global iid_value, current_iid

        _files = ["1", "2", "3"]


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

        return iid_value


        # open config window by double-clicking an item 
        def open_config():

            config_window()

    
    # delete items from list on clicking a button
    def remove_items():
            
        for focus in file_menu.selection():

            file_menu.delete(focus)
        
    
    file_menu_delete = ttk.Button(file_menu_frame, text="-", style="primary.Outline.TButton", command=remove_items)
    file_menu_delete.grid(row=1, column=0, sticky=E, ipadx=1, ipady=1)


#* configuration window
def config_window():

    # frame window 
    config_window_frame = ttk.LabelFrame(main_tab, text="Configure filter options", padding=5)
    config_window_frame.grid(row=1, column=1, sticky=N, padx=5, pady=5)
    
    # open config button
    config_open_button = ttk.Button(config_window_frame, text="Configure")
    config_open_button.grid(row=1, column=0, sticky="", columnspan=2, padx=10, pady=10)
    
    # description label
    ttk.Label(config_window_frame, text="Select a method to use:  ").grid(row=0, column=0)
    
    #TODO dropdown menu to choose a filtering style
    method_var = StringVar()
    
    method_choice_menu = ttk.Combobox(config_window_frame, textvariable=method_var)
    
    method_menu_options = ("One value", "Minimum and maximum tol.")
    method_choice_menu['values'] =  method_menu_options

    method_choice_menu['state'] = 'readonly'


    def combobox_selected(e):

        print(method_choice_menu.get())

    method_choice_menu.bind('<<ComboboxSelected>>', combobox_selected)
    method_choice_menu.grid(row=0, column=1)

    #TODO entries to insert tolerances etc.
    #TODO set working comunication with function script


def path_settings():

    # frame for the menu
    path_setting_frame = ttk.LabelFrame(main_tab, text="Output path settings", padding=20)
    path_setting_frame.grid(row=2, column=1, sticky=N) 

    # entry box for the path to show in
    path_setting_entry = ttk.Entry(path_setting_frame)
    path_setting_entry.grid(row=0, column=0, columnspan=2) # TODO fix placement

    path_setting_defpath = f"C:/Users/{getpass.getuser()}" 
    path_setting_entry.insert(0, path_setting_defpath)

    # set default path and dispaly it
    for file in os.listdir('.'):

        if file.startswith("userpth"):

            with open(file, 'r') as file:
                path_setting_entry.delete(0, END) 
                path_setting_defpath = file.readline()
                path_setting_entry.insert(0, file.readline())

    os.scandir('.')
            

    path_setting_entry['state'] = 'readonly'


    def path_setting_setusrpath():

        #TODO secure that the 'userpth.txt' file will be rewritten each time - nevermind, it rewrites itself every time
        path_setting_setusrpath_dir = filedialog.askdirectory(initialdir=path_setting_defpath)

        with open("userpth.txt", "w") as file:

            file.write(path_setting_setusrpath_dir)
            file.close()

        messagebox.showinfo("Changed default directory", "Default directory has been saved to \'usrpth.txt\' and will be loaded as default.")

        path_setting_entry['state'] = 'normal'
        path_setting_entry.insert("0", path_setting_setusrpath_dir)
        path_setting_entry['state'] = 'readonly'

    # create button for changing default directory
    path_setting_changepath_button = ttk.Button(path_setting_frame, text="Change directory", command=path_setting_setusrpath)
    path_setting_changepath_button.grid(row=1, column=0, sticky="")


#* SCRIPT BODY
def main(window):

    tab_menu()
    file_menu()
    config_window()
    path_settings()


    submit_button=ttk.Button(file_menu_frame, text="Open", style='primary.TButton', command=open_files)
    submit_button.grid(row=1, column=0, pady=5, sticky="")

    root.mainloop()



#* PROCESS FUNCTIONS
def filter_process():

    for file in filter.sources:

        filter.get_dataframe(file)



#* execute the code
if __name__ == '__main__':
    main(window())