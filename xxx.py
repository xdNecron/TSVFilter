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
    file="textures/xxx_filedisplay.png"
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
    file="textures/xxx_logo.png"
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



#*IMPORTING DATAFILE
# TODO settings - may not be a popup window :D 


def openFile():

    filepath = filedialog.askopenfilename(
        title="Open a file, you cunt", # TODO #1 also change this later 
        filetypes=(
            ("text files", "*.txt"),
            ("CSV files", "*.csv"),
            ("All files", "*.*")
            ),      
    )
    datafile = open(filepath, 'r')
    

    display.config(
        state=NORMAL
    )

    display.delete(
        1.0, END
    )

    display.insert(
        END,
        datafile.read()
    )

    display.config(
        state=DISABLED
    )


def opn_hover(e):

    tooltip.config(
        text="Import mother file(s) which the script will take data from."
    )


opn_texture = PhotoImage(
    file="textures/xxx_openfile.png"
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
        text="In this window the content of the imported file will be displayed."
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



#* PAGE 2


# textures of new elements
title_txtr = PhotoImage(
    file="textures/page2_title.png"
)

mainfield_txtr = PhotoImage(
    file="textures/page2_mainfield.png"
)



def page2():

    # clear current canvas and widgets
    canvas.delete(ALL)
    display.destroy()
    next_btn.destroy()
    file_open.destroy()


    rctngl = canvas.create_rectangle(
        0, 0, 1000, 177,
        fill="black",

    )


    canvas.create_image(
        77, 46,
        anchor=NW,
        image=title_txtr
    )


    # ! main field - might be removed later
    # ! textures are defined outside the fucntion

    canvas.create_image(
        100, 120,
        anchor=NW,
        image=mainfield_txtr
    )


    # tooltip bar
    tooltip = Label(
        root,
        text="",
        anchor=NW,
        bg="white",
        bd=1,
        relief=SUNKEN
    )
    tooltip.place(
        x=0, y=560,
        height=40,
        width=1000
    )



#* next button - re-renders root

# tooltip function
def next_hover(e):

    tooltip.config(
        text="Load next page where you may choose tolerance(s) which will determine the final output."
    )



def next_page():

    page2()


btn_texture = PhotoImage(
    file="textures/xxx_nextbtn.png"
)

next_btn = Button(
    image=btn_texture,
    highlightthickness=0,
    borderwidth=0,
    command=next_page,
    pady=30,
    bg="white"
)
next_btn.place(
    x=53, y=408,
    height=35,
    width=175,
)

next_btn.bind(
    "<Enter>",
    next_hover
)


mainloop()


"""
TODO:
- make a button which opens GitHub docunentation
- create a local README file in case the device has no internet access

"""