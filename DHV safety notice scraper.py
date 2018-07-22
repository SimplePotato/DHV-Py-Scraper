# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

   #Source HTML Code
'''<tr>
	<td class="dhv_sm data datum">10.04.2018</td>
	<td class="dhv_sm data kategorie">Safety note</td>
	<td class="dhv_sm data bezug"><a href="/db1/source/technicdatareportnotes.php?lang=en&amp;item=267" class="dhv_sm bezug" target="_blank">Paraglider Harness Progress 3</a></td>
   </tr>
''' 
   #Source  
html = urlopen("https://www.dhv.de/en/safety/safety-notes/")
soup = BeautifulSoup(html, "lxml")

   #Get last released note
def getLastRelesedNotice():
    sNotice = soup.find_all("td", class_="dhv_sm data bezug")
    return sNotice[0].text
getLastRelesedNotice() 

item = getLastRelesedNotice()
print(item)
print("----------------")
    

   #Get source link and add aditional text + "item"
def sNoticeAddText():
    sNoticeLink = soup.find_all('a', {'class': 'dhv_sm bezug', 'href': True})
    for sNoticeLink in sNoticeLink:
       print('DHV releases IMPORTANT SAFETY notice about' + '  ' + item + '\n' 'To read more information about this IMPORTANT safety notice, click on the following link' + '\n' '\n' 'https://www.dhv.de/' + sNoticeLink['href'] + '\n' '\n' '\n')
sNoticeAddText()
