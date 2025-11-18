# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 01:21:59 2025

@author: HP
"""

import requests, bs4, sys
from mptpkg import print_say
from mptpkg import voice_to_text
   
#Obtain data from https://www.npr.org/sections/news/' get news and then read out loud
def define(div,news_index):
    #Print the separate news
    print_say(f"\nNews summary number {news_index} and it's title is:") 
    
    #Retrive and print the h2 tag that has title
    #find because not all but single one
    h2tag = div.find('h2',class_='title')
    print_say(h2tag.text)
    print_say("do you want it!!!")
    inp = voice_to_text() 
    print(inp)
    takenap()
    if 'no' in inp:
        print_say("You said no")
        news_index+=1
        print_say("Check this one then")
    else:
        #retrive p tag that contains teaser
        ptag = div.find('p',class_='teaser')
        print_say(ptag.text)
        #LEt's limit it to 10 news
        news_index+=1
    return news_index

def takenap():
    inp = voice_to_text()
    if 'exit' in inp:
        print_say("You said to exit!!!\nOk!! then Good bye!!")
        sys.exit()


try:
    res = requests.get('https://www.npr.org/sections/news/')
    res.raise_for_status()
    #print(res.text)
except Exception as e:
    print(f"Error {e}")

#Using bs4 to get source code
soup = bs4.BeautifulSoup(res.text,'html.parser')  
  
'''It says title and teaser information are encapsulated in a 
parent <div> tag with a class attribute of item-info'''
#find_all divs that contains 'item-info' class
div_tags = soup.find_all('div',class_='item-info')
#print(div_tags)
news_index = 1

print_say("Welcome to news radio BD")
print_say("Say exit to exit the program")
print_say('Say yes if you want to hear it or no for not listening it')


for div in div_tags:
    define(div,news_index)
    if news_index==10: 
        break

    