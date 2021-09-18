# TSVFilter

This script was created for filtering XCMS output files in **scpecific format** and cannot be used for other files. Before using, confirm that the file has all of the columns listed below.

This repository only contains the source code and necesarry resources. You can download and change the code however you wish for your needs.

#### Required column names:
* fold
* updown
* pvalue
* mzmed
* rtmed

If a chosen column for filtering would be missing, the script will show you an error message.

## Download

Above the file list, click this [link]() to download the setup file. After downloading, install the program. **Do not remove any of the files, otherwise the script won't work correctly.**



## Usage 

After running, this window should appear on your screen.

<!-- Obrazek prvni stranky -->
![First page screenshot](https://imgur.com/0ynJCvZ.png)

> At the bottom of the window is a tooltip screen with basic information about certain elements when you hover your cursor over them.

Begin with giving the script a source file. Click ***Open file*** and then choose the desired TSV file. The file will be displayed in the outlined window for you to check if it's the correct one.

The ***Next*** button should be unlocked now. After clicking it you will be taken to configuration menu. Here you can choose different methods of filtering based on a column in the data table.

Each column has its own small menu with a check box and two entry boxes (except for UPDOWN menu - it has a dropdown menu with two options). In those you may insert the desired tolerances.

![Config menu screenshot](https://imgur.com/wAAMACj.png)

> If you do not want to use a tolerance, leave the entry empty. You can unecheck the box and keep the text in the entries - the script will ignore them.
If you do not want to specify a tolerance, leave the entry empty. You can unecheck the box but keep the text in the entries - the script will ignore them.


After setting everything up, click ***Process*** and let the sript run. After it's finished, a pop-up message will be shown and output saved in ***<span>out.tsv</span>***. This file will be overwritten with new information each time ***Process*** is clicked, so make sure to rename or move the file to another directory.

This is all necessary information for you to use the script. If any problem occurs, post an issue on [GitHub](https://github.com/xdNecron/TSVFilter/issues) (account required) or contact me directly via email **venomdushii<span>@gmail.com</span>**.
