# TSV Filter

This script was created for filtering XCMS output files in **scpecific format** and cannot be used for other files. Before using, confirm that the file has all of the columns listed below.

#### Required column names:
* fold
* updown
* pvalue
* mzmed
* rtmed


## Download

Above the file list, click ***Code*** → ***Download ZIP***. After downloading, extract the contents wherever you wish. **Do not remove the underlined files/folders showed below**, they are necessary for the script to run correctly.

<!--TODO Pridej obrazek souboru ktere musi zustat -->

The script may be executed by clicking ***<span>run.exe</span>*** if Python is not installed on your device. If you have Python installed, you could use ***<span>gui.py</span>*** to run.


## Usage 

If you've done everything right, after running the script this menu should be displayed.

<!--TODO Obrazek prvni stranky -->

> At the bottom of the window is a tooltip screen with basic information about certain elements. You can find all the information shown there in this documentation with more details.

Begin with giving the script a source file. Click ***Open file*** and then choose the desired TSV file. The file will be displayed in the outlined window for you to check if it's the correct one.

The ***Next*** button should be unlocked now. After clicking you will be taken to configuration menu. Here you can choose different methods of filtering based on a column.

Each column has its own small menu with a check box and two entry boxes. In those you may insert the desired tolerances.

> If you do not want to use a tolerance, leave the entry empty. You can unecheck the box but keep the text in the entries - the script will ignore them.

After setting everything up, click ***Process*** and let the sript run. After it's finished, a pop-up message will be shown and output saved in ***<span>out.tsv</span>***. This file will be overwritten with new information each time ***Process*** is clicked, so make sure to rename or move the file to another directory.