"""
scrape a website, gather data, and export it to csv

target page: century21.com
cached page, for practice: pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/
"""

import requests
from bs4 import BeautifulSoup as BS
import pandas

list_of_elements = []
web_page = requests.get('http://pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
web_page_content = web_page.content
soup = BS(web_page_content, 'html.parser')
allPropertyRow = soup.find_all("div", {"class": "propertyRow"})  # --> bs4.element.ResultSet
for item in allPropertyRow:
    # temporary_dict which will be stored in a list
    d = {}
    d["Address"] = item.find_all("span", {"class": "propAddressCollapse"})[0].text
    d["City"] = item.find_all("span", {"class": "propAddressCollapse"})[1].text
    d["Price"] = item.find("h4", {"class": "propPrice"}).text.replace("\n","").replace(" ", "")
    try:
        d["Beds"] =  item.find("span", {"class": "infoBed"}).find("b").text
    except:
        d["Beds"] = None
    try:
        d["Area"] = item.find("span", {"class": "infoSqFt"}).find("b").text
    except:
        d["Area"] = None
    try:
        d["Full Baths"] = item.find("span", {"class": "infoValueFullBath"}).find("b").text
    except:
        d["Full Baths"] = None
    try:
        d["Half Baths"] = item.find("span", {"class": "infoValueHalfBath"}).find("b").text
    except:
        d["Half Baths"] = None

    for columnGroup in item.find_all("div", {"class": "columnGroup"}):
        for featureGroup, featureName in zip(columnGroup.find_all("span", {"class": "featureGroup"}), columnGroup.find_all("span", {"class": "featureName"})):
            if "Lot Size" in featureGroup.text:
                d["Lot Size"] = featureName.text

    list_of_elements.append(d)


# print(list_of_elements)

data_frame = pandas.DataFrame(list_of_elements)
data_frame.to_csv("output.csv")
print(data_frame)
