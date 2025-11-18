import requests, bs4, sys, webbrowser

'''Get command line argument for search term'''

if len(sys.argv)>1:
    term = '+'.join(sys.argv[1:])
else:
    print("What's the search term?")
    term = input(">>>")
    
print(f"Googling...{term}")
try:
    res = requests.get(f"https://www.google.com/search?q={term}")
    res.raise_for_status()
    
    #webbrowser.open(f"http://www.google.com/search?q={term}")
    
    soup = bs4.BeautifulSoup(res.text,'html.parser')
    # Find other links so to open all links in the first page
    link_elems = soup.select('.yuRUbf a') # Find all anchor tags
    print(link_elems)
    #num_open = min(5,len(link_elems)) # Open only first 5 links or less if not enough links
    links = []
    for i in link_elems:
        if 'href' in i.attrs:
            url = i['href']
            links.append(url)
            print(f"Opening URL: {url}")
            webbrowser.open(url)
    # Alternative method to extract URLs from Google search results
        '''
        if 'href' in i.attrs and i['href'].startswith('/url?q='):
            url = i['href'][7:]  # Remove the '/url?q=' part
            if '&' in url:
                url = url.split('&')[0]  # Remove any additional parameters after the actual URL
            if url.startswith('http'):
                links.append(url)
                print(f"Opening URL: {url}")
                webbrowser.open(url)'''

except Exception as e:
    print(f"Could not complete search: {e}")
# print(links)