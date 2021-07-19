from os import stat_result
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from typing import runtime_checkable
import webbrowser
import getpass
import filter


root = Tk()
root.configure(bg="white")
root.title("XCMSDataAnalysis")
root.geometry('1000x600')
root.resizable(height=False, width=False)


##################################################################################################################################


#* FUNCTIONS FOR SWOTCHING BETWEEN PAGES

# clears content of page 1
def page1_clear():

    canvas.delete(ALL)
    next_btn.place_forget()
    file_open.place_forget()
    docmbtn.place_forget()
    display.place_forget()

# clears content of page 2
def page2_clear():

    canvas.delete(ALL)
    prev_btn.place_forget()
    process_btn.place_forget()

    rt_check.place_forget()
    updown_check.place_forget()
    fold_check.place_forget()
    pvalue_check.place_forget()
    mz_check.place_forget()

    rtmin_entry.place_forget()
    rtmin_desc.place_forget()
    rtmax_entry.place_forget()
    rtmax_desc.place_forget()

    updown_entry.place_forget()

    foldmin_entry.place_forget()
    foldmin_desc.place_forget()
    foldmax_entry.place_forget()
    foldmax_desc.place_forget()

    pvaluemin_entry.place_forget()
    pvaluemin_desc.place_forget()
    pvaluemax_entry.place_forget()
    pvaluemax_desc.place_forget()

    mzmin_entry.place_forget()
    mzmin_desc.place_forget()
    mzmax_entry.place_forget()
    mzmax_desc.place_forget()

    reset_btn.place_forget()


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
    bg="white",
    state=DISABLED
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

    global filepath

    filepath = filedialog.askopenfilename(
        title="Open a file, you cunt", # TODO #1 also change this later 
        filetypes=(
            ("CSV and TSV files", "*.csv *.tsv"),
            ("All files", "*.*")
            ),
        initialdir=f"C:/Users/{user}"      
    )

    # send filepath to the filtration script
    filter.obtain_file(filepath)

    datafile = open(filepath, 'r')

    next_btn.config(
        state=NORMAL
    )
    

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
        text="In this window is displayed the content of imported file."
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

processbtn_txtr = PhotoImage(
    file="textures/page2_processbtn.png"
)

rt_txtr = PhotoImage(
    file="textures/page2_rt.png"
)

mz_txtr = PhotoImage(
    file="textures/page2_mz.png"
)

fold_txtr = PhotoImage(
    file="textures/page2_fold.png"
)

updown_txtr = PhotoImage(
    file="textures/page2_updown.png"
)

pvalue_txtr = PhotoImage(
    file="textures/page2_pvalue.png"
)

resetbtn_txtr = PhotoImage(
    file="textures/page2_resetbtn.png"
)


#* widgets which communicate with the filtration script
rt_var = IntVar()
updown_var = IntVar()
fold_var = IntVar()
pvalue_var = IntVar()
mz_var = IntVar()


rt_check = Checkbutton(
    root,
    bg="white",
    highlightthickness=0,
    highlightcolor="white",
    variable=rt_var,
    bd=3
)

updown_check = Checkbutton(
    root,
    bg="white",
    highlightthickness=0,
    highlightcolor="white",
    variable=updown_var,
    bd=3
)

fold_check = Checkbutton(
    root,
    bg="white",
    highlightthickness=0,
    highlightcolor="white",
    variable=fold_var
)

pvalue_check = Checkbutton(
    root,
    bg="white",
    highlightthickness=0,
    highlightcolor="white",
    variable=pvalue_var,
    bd=3
)

mz_check = Checkbutton(
    root,
    bg="white",
    highlightthickness=0,
    highlightcolor="white",
    variable=mz_var,
    bd=3
)

# rt entries and descs
rtmin_entry = Entry(
    root,
    width=20,
)

rtmax_entry = Entry(
    root,
    width=20
)

rtmin_desc = Label(
    root,
    text="Minimum",
    bg="white"
)

rtmax_desc = Label(
    root,
    text="Maximum",
    bg="white"
)

# updown dropdown menu
choice = StringVar()
choice.set("UP")

updown_entry = OptionMenu(
    root,
    choice,
    "UP",
    "DOWN",
)


# fold entries and descs
foldmin_entry = Entry(
    root,
    width=15
)

foldmax_entry = Entry(
    root,
    width=15
)

foldmin_desc = Label(
    root,
    text="Minimum",
    bg="white"
)

foldmax_desc = Label(
    root,
    text="Maxmimum",
    bg="white"
)


# pvalue entries and descs
pvaluemin_entry = Entry(
    root,
    width=20
)

pvaluemax_entry = Entry(
    root,
    width=20
)

pvaluemin_desc = Label(
    root,
    text="Minimum",
    bg="white"
)

pvaluemax_desc = Label(
    root,
    text="Maximum",
    bg="white"
)


# mz entries and descs
mzmin_entry = Entry(
    root,
    width=25
)

mzmax_entry = Entry(
    root,
    width=25
)

mzmin_desc = Label(
    root,
    text="Minimum",
    bg="white"
)

mzmax_desc = Label(
    root,
    text="Maximum",
    bg="white"
)



# previous button
def prev_hover(e):

    tooltip.config(
        text="Back to file upload."
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


# process button
def process():

    if rt_var.get() == 1:

        filter.rt_tol(float(rtmin_entry.get()), float(rtmax_entry.get()))

        rt_check.config(
            state=DISABLED
        )

        rtmin_entry.config(
            state=DISABLED
        )

        rtmax_entry.config(
            state=DISABLED
        )

        rt_var.set(0)

    if updown_var.get() == 1:

        filter.updown(choice.get())

        updown_check.config(
            state=DISABLED
        )

        updown_entry.config(
            state=DISABLED
        )

        updown_var.set(0)

    if fold_var.get() == 1:

        filter.fold_tol(float(foldmin_entry.get()), float(foldmax_entry.get()))

        fold_check.config(
            state=DISABLED
        )

        foldmin_entry.config(
            state=DISABLED
        )

        foldmax_entry.config(
            state=DISABLED
        )

        fold_var.set(0)

    if pvalue_var.get() == 1:

        filter.pvalue_tol(float(pvaluemin_entry.get()), float(pvaluemax_entry.get()))

        pvalue_check.config(
            state=DISABLED
        )

        pvaluemin_entry.config(
            state=DISABLED
        )

        pvaluemax_entry.config(
            state=DISABLED
        )

        pvalue_var.set(0)

    if mz_var.get() == 1:

        filter.mz_tol(float(mzmin_entry.get()), float(mzmax_entry.get()))

        mz_check.config(
            state=DISABLED
        )

        mzmin_entry.config(
            state=DISABLED
        )

        mzmax_entry.config(
            state=DISABLED
        )

        mz_var.set(0)

    print(filter.df)
    filter.out_tsv()



def process_hover(e):

    tooltip.config(
        text="Iniciate processing. May take longer based on the amount of data."
    )


process_btn = Button(
    root,
    image=processbtn_txtr,
    bd=0,
    borderwidth=0,
    highlightthickness=0,
    bg="white",
    command=process
)

process_btn.bind(
    "<Enter>",
    process_hover
)


#* reset button
def reset_state():

    filter.obtain_file(filepath)

    # enable disabled boxes
    rt_check.config(
        state=NORMAL
    )

    rtmin_entry.config(
        state=NORMAL
    )

    rtmax_entry.config(
        state=NORMAL
    )
    
    updown_check.config(
        state=NORMAL
    )

    updown_entry.config(
        state=NORMAL
    )

    pvalue_check.config(
        state=NORMAL
    )

    pvaluemin_entry.config(
        state=NORMAL
    )

    pvaluemax_entry.config(
        state=NORMAL
    )

    mz_check.config(
        state=NORMAL
    )

    mzmin_entry.config(
        state=NORMAL
    )

    mzmax_entry.config(
        state=NORMAL
    )

def reset_hover(e):

    tooltip.config(
        text="Discards all changes."
    )


reset_btn = Button(
    root,
    bg="white",
    highlightthickness=0,
    bd=0,
    borderwidth=0,
    image=resetbtn_txtr,
    command=reset_state
)

reset_btn.bind(
    "<Enter>",
    reset_hover
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



    #* DOCUMENTATION BUTTON
    docmbtn.place(
        x=53, y=305,
        height=35,
        width=173
    )


    #* NEXT BUTTON
    next_btn.place(
        x=776, y=502,
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

    canvas.create_image(
        123, 138,
        anchor=NW,
        image=rt_txtr
    )

    canvas.create_image(
        426, 138,
        anchor=NW,
        image=updown_txtr
    )

    canvas.create_image(
        655, 138,
        anchor=NW,
        image=fold_txtr
    )

    canvas.create_image(
        123, 268,
        anchor=NW,
        image=pvalue_txtr
    )

    canvas.create_image(
        426, 268,
        anchor=NW,
        image=mz_txtr
    )



    prev_btn.place(
        x=77, y=502,
        height=35,
        width=173
    )
    

    process_btn.place(
        x=776, y=502,
        width=173,
        height=35,
    )

    reset_btn.place(
        x=568, y=422
    )

    # check buttons
    rt_check.place(
        x=138, y=150,
        width=16,
        height=16
    )

    updown_check.place(
        x=444, y=150,
        width=16,
        height=16
    )

    fold_check.place(
        x=673, y=150,
        width=16,
        height=16
    )

    pvalue_check.place(
        x=138, y=289,
        width=16,
        height=16
    )

    mz_check.place(
        x=444, y=284,
        width=16,
        height=16
    )

    #* entries and labels

    # rt
    rtmin_entry.place(
        x=224, y=181
    )

    rtmin_desc.place(
        x=144, y=181
    )


    rtmax_entry.place(
        x=224, y=214
    )

    rtmax_desc.place(
        x=144, y=214
    )


    # updown
    updown_entry.place(
        x=480, y=188
    )


    # fold
    foldmin_entry.place(
        x=740, y=181
    )

    foldmin_desc.place(
        x=670, y=181
    )

    foldmax_entry.place(
        x=740, y=214
    )

    foldmax_desc.place(
        x=660, y=214
    )


    # pvalue
    pvaluemin_entry.place(
        x=224, y=334
    )

    pvaluemax_entry.place(
        x=224, y=385
    )

    pvaluemin_desc.place(
        x=144, y=334
    )

    pvaluemax_desc.place(
        x=144, y=385
    )


    # mz entires and descs
    mzmin_entry.place(
        x=583, y=320
    )

    mzmin_desc.place(
        x=458, y=320
    )

    mzmax_entry.place(
        x=583, y=371
    )

    mzmax_desc.place(
        x=458, y=371
    )


###########################################################################################


mainloop()


"""
TODO:
- make a button which opens GitHub docunentation
- create a local README file in case the device has no internet access

"""