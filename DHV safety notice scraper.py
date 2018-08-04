# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import datetime as dt
'''
    #Now Date
today = dt.now()
date_string = dt.strftime(today, '%m.%d.%Y') #the date is in the same format as the date in a class="dhv_sm data datum"
print(date_string) 
'''

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

    #scraped data
datum = soup.find_all("td", class_="datum")
kat = soup.find_all("td", class_="kategorie")
productName = soup.find_all("td", "a", class_="bezug")
safetyNoticeLink = soup.find_all('a', {'class': 'dhv_sm bezug', 'href': True})

    #going trough all the data in the tables with for loop and skip the first TR with empty TD with [1:] -means skip first element. (if we want to skip last element we chose [:-1])
for datum,kat,productName,safetyNoticeLink in zip(datum[1:],kat[1:],productName[1:],safetyNoticeLink):
    print('\n'+'\n')
    print('\n')
    print(datum.text)
    print('\n' + '------------------------------------------')
    print('DHV has released ' + kat.text + ' about ' + productName.text + '.')
    print('------------------------------------------' + '\n') 
    print('For more information about this notice please visit link below' + '\n'+ '\n' + 'https://www.dhv.de/' + safetyNoticeLink['href'])
