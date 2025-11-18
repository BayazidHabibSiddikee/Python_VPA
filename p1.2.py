# -*- coding: utf-8 -*-
"""
Created on Wed Oct 29 23:35:58 2025

@author: HP
"""

import requests, bs4, os, webbrowser


url = "https://www.npr.org/podcasts/500005/npr-news-now/"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.text,'html.parser')
print(soup)

#a class="audio-module-listen
atag = soup.find_all('a',class_='audio-module-listen')
for a in atag:
    b = a['href']
    print(b)
    '''
    #webbrowser.open(b)
    b = os.path.join(os.getcwd(),b)
    
    os.system(f"curl -O {b}")
    #from playsound import playsound
    #playsound(f"{b}")
    os.system(f"explorer {b}")'''
    
    #remove unwanted components
    pos = b.find('?')
    print(b[0:pos])
    mymp3 = b[0:pos]
    webbrowser.open(mymp3)