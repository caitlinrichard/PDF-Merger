import PyPDF2
import os
import sys

class Main:
    # Gather PDF files
    pdf_files = []
    for file_name in os.listdir('.'):
        if file_name.endswith('.pdf'):
            pdf_files.append(file_name)
    pdf_files.sort(key = str.lower)
    pdf_writer = PyPDF2.PdfFileWriter()

    # Add each page of each PDF to new file
    try:
        for file_name in pdf_files:
            with open(file_name, 'rb') as pdf_file_obj:
                pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj, strict=False)
                for page_num in range(0, pdf_reader.numPages): # Here you can adjust the pages numbers you want to merge
                    page_obj = pdf_reader.getPage(page_num)
                    pdf_writer.addPage(page_obj)

                    # Save as new PDF file
                    new_file = 'combined-pdf.pdf'
                    with open(new_file, 'wb') as pdf_output:
                        pdf_writer.write(pdf_output)
    except EnvironmentError:
        print('Could not merge PDF files.')
        sys.exit()

    # Print success message
    print(f'Success! Your PDF files have been merged and are saved in {new_file}')
