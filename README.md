# PDF-Merger

Are you tired of using unsecured, ad-ridden online PDF merging sites? Then this is for you! This PDF Merger is a simple tool that quickly combines multiple PDF files, and you can do it all on your local computer without having to upload your files to some random website. 

## How to use PDF Merger
1. Make sure Python is installed on your PC. You can check this by typing `python` in your command line and seeing if a version pops up. If Python is not installed on your PC, you can download the latest version here: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Install PyPDF 2 version 1.26.0 by typing `pip install --user PyPDF2==1.26.0` in your command line (note: you may need to add this to your interpreter as well if you choose to run the program in an IDE)
3. Add the **main.py** file and the PDFs you would like to merge to one folder
4. Run **main.py** 
5. Enjoy your freshly merged PDF!


## Additional Notes 
- If you need to rerun the program within the same folder to recombine the files, be sure to delete the previous output file first, or go into the program and change the name of the new_file variable. 
- The files will merge in alphanumeric order, so I suggest numbering your files in the order you want them to be combined. 
