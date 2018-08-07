# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError
from urllib.error import URLError
from datetime import date
from datetime import datetime


print("DHV-PY-SCRAPER \n")



    #Today Date
def todayDate():
    today = date.today()
    today = datetime.strftime(today, "%d.%m.%Y")
    return(today)
()
print("Today  " + todayDate())


    #fakeDate is for testing purposes only (when not in testing make change on row 80 at if statement)
def fakeDate():
    td = date.today()
    #print(td.strftime("%d.%m.%Y"))
    fd = td.replace(day=10, month=4, year=2018)
    return(fd.strftime("%d.%m.%Y"))
()
print("FAKE DATE  " + fakeDate() + "\n")



    #HTML Code for scraping
'''<tr>
	<td class="dhv_sm data datum">10.04.2018</td>
	<td class="dhv_sm data kategorie">Safety note</td>
	<td class="dhv_sm data bezug"><a href="/db1/source/technicdatareportnotes.php?lang=en&amp;item=267" class="dhv_sm bezug" target="_blank">Paraglider Harness Progress 3</a></td>
   </tr>
'''



try:

    #Source site for parsing
    html = urlopen("https://www.dhv.de/en/safety/safety-notes/")
    soup = BeautifulSoup(html, "lxml")

    #scraped data
    datum = soup.find_all("td", class_="datum")    #self explanatory. Datum is date
    kat = soup.find_all("td", class_="kategorie")    #a category of notice like... Warning, Airworthiness advisory, Safety note...
    productName = soup.find_all("td", "a", class_="bezug")    #the main topic of that note
    safetyNoticeLink = soup.find_all("a", {"class": "dhv_sm bezug", "href": True})    #link to the article



    # If something goes wrong with the connection on their or our side, we will be notified with following exceptions
except URLError as e:    #https://docs.python.org/3.7/library/urllib.error.html
    if hasattr(e, "reason"):
        print("Failed to reach server!")
        print("Reason:", e.reason)
    elif hasattr(e, "code"):
        print("The sever couldn\'t fulfill the request.")
           # next comment is a fix for "pylint" Error message (E1101:Instance of 'URLError' has no 'code' member) Read more... http://pylint-messages.wikidot.com/messages:e1101
           # pylint: disable=no-member
        print("Error code: ", e.code)



except AttributeError() as e:
    print("There\'s something wrong with a tag attribute")


    #Grab all the data in the tables with for loop and skip the first TR with empty TD with [1:] -means skip first element. (if we want to skip last element we chose [:-1])
else:

    for datum,kat,productName,safetyNoticeLink in zip(datum[1:],kat[1:],productName[1:],safetyNoticeLink):

    #Print out only if date is equal as todays date (Can choose betwen todayDate and fakeDate but this is for testing only)
        if str(fakeDate()) != str(datum):
            print("\n" + "\n")
            print(datum.text)
            print("\n" + "------------------------------------------")
            print("title: " + kat.text + ": " + productName.text + ".")    #title: (DHV has released )
            print("------------------------------------------" + "\n") 
            print("msg:" + "\n"+ "\n" + "https://www.dhv.de/" + safetyNoticeLink["href"])    #msg: (For more info please visit the link below)  link (https://www.dhv.de/)
            
        else:
            print("Nothing to worry about")
            break
    '''
    I'm doing something wrong with the if statement at row 82.
    A datum is a scraped date which is always now ( date when notice was released).
    I create fakeDate function just for the purpose of testing and is always set to one of the dates when the notice was released.
    
    When I set...
    if str(fakeDate()) == str(datum):
        print("Safety Note)
    else:
        print("nothing new")

    but here is the issue. The set fakeDate is always equal to datum and the output is always the opposite!
    If I set fakeDate != datum which shouldn't return issued notes it returns exactly that.

    What am I doing wrong?    

    '''