# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:27:21 2025

@author: HP
"""

# -*- coding: utf-8 -*-
"""
Simple web scraping example using BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup

# Fetch the webpage
url = 'https://www.booking.com/index.html?aid=1670475&label=enxl-edge-ntp-topsites-curate-ana'
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all <p> tags
    ptags = soup.find_all("p")

    for p in ptags:
        print(p.get_text(strip=True))  # print text inside <p> tags

        # Find all <a> tags inside this <p>
        atags = p.find_all('a')
        for a in atags:
            print("Link text:", a.get_text(strip=True))
            print("URL:", a.get('href'))
            print('-' * 50)

else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
