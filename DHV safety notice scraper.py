# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import datetime as dt

    #Now Date
today = dt.now()
date_string = dt.strftime(today, '%m.%d.%Y') #the date is in the same format as the date in a ckass="dhv_sm data datum"
print('\n' + date_string + '\n') 
print('\n'+"----------------"+'\n')

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

    #get category of a notice
kat = soup.find_all("td", class_="kategorie")
for kategorie in kat:
    print(kategorie.text)

    #I get a list of category successfully, but I don't know how to implement them into final print???

print('\n'+"----------------"+'\n')

    #Get product name
productName = soup.find_all("td", "a", class_="bezug")
for product in productName:
    print(product.text)

    #I get a list of items successfully, but I don't know how to implement them into final print???

print('\n'+"----------------"+'\n')

    #Get source link and add aditional text + "item"
safetyNoticeLink = soup.find_all('a', {'class': 'dhv_sm bezug', 'href': True})
for link in safetyNoticeLink:
    #print('DHV releases IMPORTANT SAFETY notice about' + '  ' + item + '\n' 'To read more information about this IMPORTANT safety notice, click on the following link' + '\n' '\n' 'https://www.dhv.de/' + sNoticeLink['href'] + '\n' '\n' '\n')
    print('https://www.dhv.de/' + link['href'])
    