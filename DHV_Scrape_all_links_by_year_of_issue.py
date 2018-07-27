# Just playing around and practicing with this one and right now isn't a part of the original project.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.dhv.de/en/safety/safety-notes/")
soup = BeautifulSoup(html, "lxml")


'''
--- With this block of code we get all the links from wanted domain ---
for link in soup.findAll("a"):
	if "href" in link.attrs:
		print(link.attrs["href"])
''' 

#   With for loop we scraped all the links, sorted by year of issues.

for link in soup.find("div", {"id":"c14421"}).findAll("a", href=re.compile("^(en/safety/safety-notes/jahr/)([0-9]{4})/$")):
	if "href" in link.attrs:
		print("https://www.dhv.de/"+link.attrs["href"])
	else:
		pass