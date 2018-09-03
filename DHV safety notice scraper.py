# -*- coding: utf-8 -*-
from urllib.request import urlopen
import urllib.request
from bs4 import BeautifulSoup
import re
from urllib.error import HTTPError, URLError
from datetime import date, datetime
import time
import pprint as pp
import logging
import json


    # The site we are scraping data from... https://www.dhv.de/en/safety/safety-notes/


    # HTML Code for scraping
''' <tr>
        <td class="dhv_sm data datum">10.04.2018</td>
        <td class="dhv_sm data kategorie">Safety note</td>
        <td class="dhv_sm data bezug"><a href="/db1/source/technicdatareportnotes.php?lang=en&amp;item=267" class="dhv_sm bezug" target="_blank">Paraglider Harness Progress 3</a></td>
    </tr>
'''



# Will create --logs.log-- file for logging and debuging. Here we also configure logger settings.
logging.basicConfig(filename="logs.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s %(message)s", datefmt="%d.%m.%y %I:%M:%S %p")    # LEVEL set to DEBUG will log all messages to the log file. If we don't want to log DEBUG logs set level to --INFO--.Choosing --filemode="w"-- argument, will always rewrite old messages in the logs.log file SO, CHOSE THIS ARGUMENT ONLY IF YOU'RE SURE YOU DON'T NEED OLD LOGS!!! 


logging.debug("START script")

    # Today Date
def todayDate():
    today = date.today()
    today = datetime.strftime(today, "%d.%m.%Y")
    return(today)
()
logging.info("Today  " + todayDate())


    # fakeDate is for testing purposes only (when not in testing make changes on line 80 at if statement - Replace --todayDate()-- with --fakeDate()--)
def fakeDate():
    td = date.today()
    fd = td.replace(day=10, month=4, year=2018) # when testing this script, set --fd-- to 10.4.2018 (Two safety notices that day).
    return(fd.strftime("%d.%m.%Y"))
()
logging.debug("FAKE DATE is set to  " + fakeDate() + "\n")



    # While loop will executing code every n seconds as it is set in line 123
while True:
    logging.debug("In the WHILE loop")


    try:
        logging.debug("Entering TRY")
        # Source site for parsing
        html = urlopen("https://www.dhv.de/en/safety/safety-notes/")
        soup = BeautifulSoup(html, "lxml")


        # scraping data from HTML tags/classes
        datum = soup.find_all("td", class_="datum")    # self explanatory. Datum is date
        kat = soup.find_all("td", class_="kategorie")    # a category of notice like... Warning, Airworthiness advisory, Safety note...
        productName = soup.find_all("td", "a", class_="bezug")    #the main topic of that note
        safetyNoticeLink = soup.find_all("a", {"class": "dhv_sm bezug", "href": True})    # link to the article


        # All scraped data lists ... ( Got idea from this video and his git repo https://www.youtube.com/watch?v=R3XJZAldhYQ )
        allData = []


        # Grab all the data from tables with for loop and skip the first TR with empty TD with [1:] which means skip first element. (if we want to skip last element we chose [:-1])
        for datum,kat,productName,safetyNoticeLink in zip(datum[1:],kat[1:],productName[1:],safetyNoticeLink):
            logging.debug("In the FOR loop X number of articles")

        # Print out only if date is equal as todays date (Can choose betwen todayDate and fakeDate but this is for testing only)
            if (datum.text) == (todayDate()):

                print("\n" + "\n")
                print(datum.text)
                print("\n" + "------------------------------------------")
                print("title: " + kat.text + ": " + productName.text + ".")    # Example... title: (DHV has released something something )
                print("------------------------------------------" + "\n")
                print("msg:" + "\n"+ "\n" + "https://www.dhv.de" + safetyNoticeLink["href"])    # example... msg: (For more info please visit the link below)  link (https://www.dhv.de)
                print("\n" + "...................." + "\n")

                logging.info("The following data has been successfully scraped: ")
                logging.info(kat.text + " for/about " + productName.text)

                allData.append(datum.text)    # Appending datum to allData list
                allData.append(kat.text)    # Appending kat to allData list
                allData.append(productName.text)    # Appending productName to allData list
                allData.append( "https://www.dhv.de" + safetyNoticeLink["href"] )    # Appending safetyNoticeLink to allData list
                
                logging.debug("data appended to allData list")
                continue
            else:
                pass


        # If something goes wrong, we will be notified with the exception ( e == error)
        # All wrongish behaviours will be logged into --logs.log-- file

    except Exception as e:
        logging.warning("Woops! Something went wrong!")
        logging.error("Reason: " + str(e))
        time.sleep(300)    # If e then wait 5 min
        continue
    else:
        pass

    print("\n" + "......PRITTY PRINT....." + "\n")
    pp.pprint(allData)    # Pretty Print 
    print("\n" + "......PYTHON LIST....." + "\n")
    print(allData)
    print("\n" + ".....JSON ARRAY......" + "\n")
    print(json.dumps(allData))    # Printing JSON

    logging.debug("WHILE loop ended. Now sleep for n hours and repeat the WHILE loop")
    time.sleep(14400) # (300 sec == 5 min), (3600 sec == 1h), (14400 sec == 4h), (28800 == 8h), (43200 == 12h)
