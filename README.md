![alt text](https://www.dhv.de/fileadmin/templates/dhv2011/img/pagelayout/dhv_logo_print.jpg "DHV logo")
## Safety Notice Scraper

+ **The idea** is, to build a scraper which will scrape every new safety note links from [DHV website](https://www.dhv.de/en/safety/safety-notes/ "DHV's Safety Notices").

_This site publishes every new known safety issue about paragliding and hangliding equipment._
***
+ The scraper will run every 4h or 12h and will not show already scraped results. _That means none of the new safety notes shouldn't be shown twice in the output._
 
+ In the output, I want to get the *date* of the released note, some *text* + name of the *equipment* that is issued and *link* to the page where the issue is described.

###### HTML example code where our wanted data is:

<tr>
	<td class="dhv_sm data datum">10.04.2018</td>
	<td class="dhv_sm data kategorie">Safety note</td>
	<td class="dhv_sm data bezug"><a href="/db1/source/technicdatareportnotes.php?                    lang=en&amp;item=267" class="dhv_sm bezug" target="_blank">
           Paraglider Harness Progress 3</a></td>
</tr>

```html
<tr>
	<td class="dhv_sm data datum">10.04.2018</td>
	<td class="dhv_sm data kategorie">Safety note</td>
	<td class="dhv_sm data bezug"><a href="/db1/source/technicdatareportnotes.php?                             lang=en&amp;item=267" class="dhv_sm bezug" target="_blank">
           Paraglider Harness Progress 3</a></td>
</tr>
```
___

+ For *older* notes I'll code a dictionary where all the released notes will be stored and then if needed, also be recalled like in a search option. The dictionary will also be necessary for the scraper to know which links were already been stored so they won't appear over and over again.

This shouldn't be a problem because for every new release the link to it is numbered like the number at the end of the link.
```html
~~<a href="/db1/source/technicdatareportnotes.php?lang=en&amp;item=~~267~~"</a>~~
```








