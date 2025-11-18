import requests, bs4, webbrowser
with open("example.html") as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')
    print(soup.text)
    #Select elements
    elem = soup.select('#author') #Through ID
    print(type(elem[0]))
    
    pelem = soup.select('a') #Through tag
    print(pelem[0])
    print(pelem[0]['href'])
    
    link = pelem[0]['href']
    try:
        res = requests.get(link)
        webbrowser.open(link)
        print(res.text[:250])
    except Exception as e:
        print(f"Could not retrieve link: {e}")