__author__ = "tobyproctor"
import requests
from bs4 import BeautifulSoup

articleID= "32213003"
baseURL="http://www.bbc.co.uk/modules/comments/ajax/comments/?siteId=newscommentsmodule&forumId=__CPS__"+articleID+"&filter=none&sortOrder=Descending&sortBy=Created&mock=0&mockUser=&parentUri=http%3A%2F%2Fwww.bbc.co.uk%2Fnews%2F32213003%2Fcomments%2Fiframe&loc=en-GB&preset=responsive&initial_page_size=100&transTags=0&comments_page=1"
r=requests.get(baseURL)
collected = r.json()

print collected.keys()
#print collected['comments']
print collected["summary"]

soup=BeautifulSoup(collected["comments"])

#print soup.find_all('li')
print r.headers["content-type"]