from os import stat_result
from tkinter import *
from tkinter import filedialog
import webbrowser
import getpass

root = Tk()
root.configure(bg="white")
root.title("XCMSDataAnalysis")
root.geometry('1000x600')
root.resizable(height=False, width=False)


##################################################################################################################################

#* FUNCTIONS FOR SWOTCHING BETWEEN PAGES

def page1_clear():

    canvas.delete(ALL)
    next_btn.place_forget()
    file_open.place_forget()
    docmbtn.place_forget()
    display.place_forget()


def page2_clear():

    canvas.delete(ALL)
    prev_btn.place_forget()


def next_page():

    page2()


def prev_page():

    page1()




#* ELEMENTS AND WIDGETS WHICH STAY THE SAME FOR BOTH PAGES

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


#* next button - re-renders root

# tooltip function
def next_hover(e):

    tooltip.config(
        text="Load next page where you may choose tolerance(s) which will determine the final output."
    )



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

next_btn.bind(
    "<Enter>",
    next_hover
)


#* TEXTURES FOR PAGE 1

fld_texture = PhotoImage(
    file="textures/xxx_filedisplay.png"
)

logo = PhotoImage(
    file="textures/xxx_logo.png"
)

tm = PhotoImage(
    file="textures/tm.png"
)

docmbtn_txtr = PhotoImage(
    file="textures/xxx_docmbtn.png"
)

opn_texture = PhotoImage(
    file="textures/xxx_openfile.png"
)


#* WIDGETS FOR PAGE 1 AND THEIR FUNCTIONS

#* documentation button
# open documentation in default browser
def opensite():

    webbrowser.open_new_tab("www.youtube.com") # TODO: #3 change link when the documentation is done


# hover function
def docmbtn_onhover(e):

    tooltip.config(
        text="Redirects you to GitHub documentation for the script."
    )


docmbtn = Button(
    root,
    image=docmbtn_txtr,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    command=opensite,
    bg="white"
)

docmbtn.bind(
    "<Enter>",
    docmbtn_onhover
)


#* openfile button
def openfile():

    # obtain current username
    user = getpass.getuser()

    filepath = filedialog.askopenfilename(
        title="Open a file, you cunt", # TODO #1 also change this later 
        filetypes=(
            ("CSV files", "*.csv"),
            ("text files", "*.txt"),
            ("All files", "*.*")
            ),
        initialdir=f"C:/Users/{user}/Desktop"      
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


file_open = Button(
    root,
    text="Open File",
    command=openfile,
    image=opn_texture,
    borderwidth=0,
    bg="white",
    pady=30
)

file_open.bind(
    "<Enter>", opn_hover
)


#* file display
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

display.bind(
    "<Enter>", dpl_hover
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




#* PAGE 2 ELEMENTS AND WIDGETS

#* textures of elements
title_txtr = PhotoImage(
    file="textures/page2_title.png"
)

mainfield_txtr = PhotoImage(
    file="textures/page2_mainfield.png"
)

prevbtn_txtr = PhotoImage(
    file="textures/page2_prevbtn.png"
)


#* widgets

def prev_hover(e):

    tooltip.config(
        text="Back to file upload"
    )


prev_btn = Button(
    root,
    image=prevbtn_txtr,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    bg="white",
    command=prev_page
)

prev_btn.bind(
    "<Enter>",
    prev_hover
)



#######################################################################################################################################

#* PAGE 1   

def page1():

    tooltip.config(
        text=""
    )

    page2_clear()

    #* MAIN ELEMENTS for page 1
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


    canvas.create_image(
        53, 53,
        anchor=NW,
        image=logo
    )


    canvas.create_image(
        937, 0,
        anchor=NW,
        image=tm
    )


    #* DOCUMENTATION BUTTON
    docmbtn.place(
        x=53, y=305,
        height=35,
        width=173
    )

    #* NEXT BUTTON
    next_btn.place(
        x=52, y=408,
        width=173,
        height=35
    )


    #*IMPORTING DATAFILE
    # TODO settings
    file_open.place(
        x=53, y=256,
        width=175,
        height=35,
    )


    #* FILE DISPLAY
    display.place(
        x=323, y=130
    )


page1()


###############################################################################################################################


def page2():

    page1_clear()

    # clear tooltip
    tooltip.config(
        text=""
    )


    canvas.create_rectangle(
        0, 0, 1000, 177,
        fill="black"
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


    prev_btn.place(
        x=77, y=502,
        height=35,
        width=173
    )


mainloop()



"""
TODO:
- make a button which opens GitHub docunentation
- create a local README file in case the device has no internet access

"""