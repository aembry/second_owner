import PyPDF2
import os

#The working file is on the Desktop
print(os.getcwd())
os.chdir("C:\\users\\"+os.getlogin()+"\\Desktop")
print(os.getcwd())

with open("ISO9001-2015.pdf","rb") as f:
    input_file = PyPDF2.PdfFileReader(f)
    print(input_file.getNumPages())

output_file = open("target.txt","wb")
PyPDF2.PdfFileWriter().write(output_file)