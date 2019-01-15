"""
scrape a website, gather data, and export it to csv

target page: century21.com
cached page, for practice: pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
"""

import requests
from bs4 import BeautifulSoup as BS


web_page = requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
web_page_content = web_page.content
soup = BS(web_page_content, 'html.parser')
allPropertyRow = soup.find_all("div", {"class": "propertyRow"})  # --> bs4.element.ResultSet
# Because this is a list of bs4 elements, we can apply again find or find_all methods to each elem
# extract property price from the 1st element
# we need to use find, to apply the text property. Otherwise, we need to apply it to each element in the list
# returned by find_all
propertyPrice1 = allPropertyRow[0].find("h4", {"class": "propPrice"}).text
# we have some rogue spaces and \n chars, so let's strip them
propertyPrice1 = propertyPrice1.replace("\n","").replace(" ","")
# iterate through all items
# at this stage, we need to 'inspect' each element in the website, and find where it is stored, then extract it
for item in allPropertyRow:
    price   = item.find("h4", {"class": "propPrice"}).text.replace("\n","").replace(" ", "")
    address = item.find_all("span", {"class": "propAddressCollapse"})[0].text
    city    = item.find_all("span", {"class": "propAddressCollapse"})[1].text
    # some items don't have the bed number listed, so we need to take into account that it will return None
    # and NoneType doesn't have a text attribute
    try:
        # this attribute returns the text from the <span> tag, and also the text from the <b> tag
        beds = item.find("span", {"class": "infoBed"}).text
        # if we want to get only the number of beds, we can apply the find() method again
        beds =  item.find("span", {"class": "infoBed"}).find("b").text
    except:
        beds = ""

    try:
        sqft =  item.find("span", {"class": "infoSqFt"}).find("b").text
    except:
        sqft = ""

    try:
        baths =  item.find("span", {"class": "infoValueFullBath"}).find("b").text
    except:
        baths = ""

    try:
        half_bath =  item.find("span", {"class": "infoValueHalfBath"}).find("b").text
    except:
        half_bath = ""

    for columnGroup in item.find_all("div", {"class": "columnGroup"}):
        # print(columnGroup)
        for featureGroup, featureName in zip(columnGroup.find_all("span", {"class": "featureGroup"}), columnGroup.find_all("span", {"class": "featureName"})):
            # print(featureGroup.text, featureName.text)
            if "Lot Size" in featureGroup.text:
                lotSize = featureName.text
                print(lotSize)
    print(price, beds, baths, half_bath, sqft)
    print()

# print(soup.prettify())
# print(allPropertyRow)
# print(">",propertyPrice1,"<")
