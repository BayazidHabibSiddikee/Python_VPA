# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 01:21:59 2025
@author: HP
"""
import requests
import bs4
import sys
import threading
from mptpkg import print_say, voice_to_text

# Global flag for exit
exit_flag = False

def takenap():
    """Background thread listening for 'exit' command"""
    global exit_flag
    while not exit_flag:
        inp = voice_to_text()
        if inp and 'exit' in inp.lower():
            print_say("You said to exit! Ok then, goodbye!")
            exit_flag = True
            sys.exit()

def read_news(div, news_index):
    """Read a single news item"""
    global exit_flag
    
    if exit_flag:
        return news_index
    
    # Print the news number
    print_say(f"News summary number {news_index}. The title is:")
    
    # Retrieve and print the h2 tag that has title
    h2tag = div.find('h2', class_='title')
    if not h2tag:
        return news_index + 1
    
    print_say(h2tag.text)
    print_say("Do you want to hear this one?")
    
    inp = voice_to_text()
    print(f"You said: {inp}")
    
    if inp and 'no' in inp.lower():
        print_say("You said no. Let's check the next one.")
    else:
        # Retrieve p tag that contains teaser
        ptag = div.find('p', class_='teaser')
        if ptag:
            print_say(ptag.text)
        else:
            print_say("No summary available for this news.")
    
    return news_index + 1

def main():
    global exit_flag
    
    print_say("Welcome to News Radio BD")
    print_say("Say 'exit' anytime to quit the program")
    print_say("Say 'yes' to hear the full story or 'no' to skip to the next one")
    
    # Start exit listener thread
    exit_thread = threading.Thread(target=takenap, daemon=True)
    exit_thread.start()
    
    # Fetch news from NPR
    try:
        print("Fetching news from NPR...")
        res = requests.get('https://www.npr.org/sections/news/', timeout=10)
        res.raise_for_status()
    except Exception as e:
        print_say(f"Error fetching news: {e}")
        sys.exit(1)
    
    # Parse HTML
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    
    # Find all divs that contain 'item-info' class
    div_tags = soup.find_all('div', class_='item-info')
    
    if not div_tags:
        print_say("No news items found")
        sys.exit(1)
    
    print_say(f"Found {len(div_tags)} news articles. Let's begin!")
    
    # Read news items
    news_index = 1
    for div in div_tags:
        if exit_flag or news_index > 10:
            break
        
        news_index = read_news(div, news_index)
    
    if not exit_flag:
        print_say("That's all the news for now. Goodbye!")

if __name__ == "__main__":
    main()