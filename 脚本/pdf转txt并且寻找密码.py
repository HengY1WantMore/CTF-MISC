from io import StringIO

#python3
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter


import sys
import string
import os
import hashlib
import importlib
import random
from urllib.request import urlopen
from urllib.request import Request


def get_pdf():
    return [i for i in os.listdir("./") if i.endswith("pdf")]
 
 
def convert_pdf_to_txt(path_to_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path_to_file, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text
 
 
def find_password():
    pdf_path = get_pdf()
    for i in pdf_path:
        print ("Searching word in " + i)
        pdf_text = convert_pdf_to_txt("./"+i).split(" ")
        for word in pdf_text:
            sha1_password = hashlib.sha1(word.encode('utf-8')+'Salz!'.encode('utf-8')).hexdigest()
            if (sha1_password == '3fab54a50e770d830c0416df817567662a9dc85c'):
                print ("Find the password :" + word)
                exit()
            
 
if __name__ == "__main__":
    find_password()
