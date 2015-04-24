__author__ = 'tobyproctor'

import json
from bs4 import BeautifulSoup

f=open('examplecommentsfile')
#
# print f.read()

soup=BeautifulSoup(f.read())
print soup.find_all('li')



#print soup
