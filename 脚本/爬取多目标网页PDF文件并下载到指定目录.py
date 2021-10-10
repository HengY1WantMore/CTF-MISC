import requests
import re
import os
import sys

re1 = '[a-fA-F0-9]{32,32}.pdf'
re2 = '[0-9\/]{2,2}index.html'

pdf_list = []
def get_pdf(url):
    global pdf_list 
    print(url)
    req = requests.get(url).text
    re_1 = re.findall(re1,req)
    for i in re_1:
        pdf_url = url+i
        pdf_list.append(pdf_url)
    re_2 = re.findall(re2,req)
    for j in re_2:
        new_url = url+j[0:2]
        get_pdf(new_url)
    return pdf_list
    # return re_2

pdf_list = get_pdf('http://111.200.241.244:63164/')
print(pdf_list)
for i in pdf_list:
    os.system('wget '+i)
