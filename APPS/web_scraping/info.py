"""
library used:
requests - to access a website and load the content to a python data structure
pip install requests

beautifulsoup - to analyze and extract needed data
pip install bs4


basic website: example.com
- written in html
- elements as components, defined by tags

https://pythonhow.com/example.html

check specific site for scraping policy
"""

import requests
from bs4 import BeautifulSoup as BS

# load the web page
web_page = requests.get('https://pythonhow.com/example.html')
# get the content
web_page_content = web_page.content
# parse content with BS
soup = BS(web_page_content, 'html.parser')
all_cities = soup.find_all('div', {'class': 'cities'})
first_city = soup.find('div', {'class': 'cities'})   # alternative all_cities[0]
sub_tag = first_city.find_all('h2')
for elem in all_cities:
    print(elem.find_all('h2'))
    print(elem.find('h2').text) #apply the text method to get the text out of the tag (works only on 1 elem, not on a list, which is returned by find_all() !!!

# print(web_page_content)
# print(soup)
# print(soup.prettify())
# print(all_cities[0])
# print(first_city)
print(sub_tag)