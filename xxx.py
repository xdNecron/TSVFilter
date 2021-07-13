from os import stat_result
from tkinter import *
from tkinter import filedialog


root = Tk()
root.configure(bg="white")
root.title("XCMSDataAnalysis")
root.geometry('1000x600')
root.resizable(height=False, width=False)



#* MAIN ELEMENTS
canvas = Canvas(
    root,
    height=600,
    width=1000, 
    bd=0,
    highlightthickness=0, 
    bg="white", 
    relief=RIDGE)
canvas.place(
    x=0, y=0
)


fld_texture = PhotoImage(
    file="textures/file_display.png"
)

canvas.create_image(
    316, 120,
    anchor=NW,
    image=fld_texture,
)


rctngl = canvas.create_rectangle(
    0, 0, 1000, 177,
    fill="black" 
)

canvas.tag_lower(rctngl)


logo = PhotoImage(
    file="textures/logo.png"
)

canvas.create_image(
    53, 53,
    anchor=NW,
    image=logo
)


tm = PhotoImage(
    file="textures/tm.png"
)

canvas.create_image(
    937, 0,
    anchor=NW,
    image=tm
)



# tooltip bar
tooltip = Label(
    root,
    text="",
    bg="white",
    bd=1,
    relief=SUNKEN,
    anchor=NW,
)
tooltip.place(
    x=0, y=560,
    height=40,
    width=1000
)



#* CONFIGURATION WINDOW
def settings():

    conf = Toplevel()
    conf.config(background="white")
    conf.geometry('200x200')
    conf.resizable(height=False, width=False)



    #checklist
    check_1 = Checkbutton(
        conf,
        text="Check 1",
        bg="white"
    )
    check_1.place(
        x=60, y=40
    )


    check_2 = Checkbutton(
        conf,
        text="Check 2",
        bg="white"
    )
    check_2.place(
        x=60, y=70
    )


    check_3 = Checkbutton(
        conf,
        text="Check 3",
        bg="white"
    )
    check_3.place(
        x=60, y=100
    )


    check_4 = Checkbutton(
        conf,
        text="Check 4",
        bg="white"
    )
    check_4.place(
        x=60, y=130
    )

# tooltip function
def settings_hover(e):

    tooltip.config(
        text="Here you can configurate which tolerances the script will use to find desired values."
    )


# settings button - opens config list
btn_texture = PhotoImage(
    file="textures/stg_button.png"
)

stg_button = Button(
    image=btn_texture,
    highlightthickness=0,
    borderwidth=0,
    command=settings,
    pady=30,
    bg="white"
)
stg_button.place(
    x=53, y=321,
    height=35,
    width=175,
)

stg_button.bind("<Enter>", settings_hover)



#*IMPORTING DATAFILE
# TODO finish import system, settings - may not be a popup window :D


def openFile():

    filepath = filedialog.askopenfilename(
        title="Open a file, you cunt", # TODO #1 also change this later 
        filetypes=(
            ("text files", "*.txt"),
            ("all files", "*.*")
            ),      
    )
    datafile = open(filepath)


def opn_hover(e):

    tooltip.config(
        text="Import mother file(s) which the script will take data from."
    )


opn_texture = PhotoImage(
    file="textures/open_file.png"
)

file_open = Button(
    root,
    text="Open File",
    command=openFile,
    image=opn_texture,
    borderwidth=0,
    bg="white",
    pady=30
)
file_open.place(
    x=53, y=256,
    width=175,
    height=35,
)

file_open.bind(
    "<Enter>", opn_hover
)


#* FILE DISPLAY

def dpl_hover(e):

    tooltip.config(
        text="In this window will be displayed the content of the imported file"
    )


display = Text(
    root,
    borderwidth=0,
    highlightthickness=0,
    height=21,
    width=73,
    padx=5,
    state=DISABLED
)
display.place(
    x=323, y=130
)

display.config(
    state=NORMAL
)
display.insert(
    END,
    "Hi, this is just a temporary text, which will change after imporing\na file."
)
display.config(
    state=DISABLED
)

display.bind(
    "<Enter>", dpl_hover
)


mainloop()