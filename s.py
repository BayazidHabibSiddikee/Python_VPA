url = "https://classroom.google.com/u/1/c/NzM5MTQ1NjgyNTkx"
try:
    import requests
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    print("Webpage fetched successfully.")
except Exception as e:
    print(f"Error {e} occurred while fetching the webpage.")
    exit()
import bs4
soup = bs4.BeautifulSoup(res.text, 'html.parser')
print("Webpage parsed successfully.")
#print(soup.text[:500])  # Print first 500 characters of the text content

import re #https://[^"\s]+\.mp4
# Find all links in the page https://drive.google.com/file/d/1lvEs8ag4FuwqOpR3bGE1Ds9u8XK9G4Uo/view
links = re.findall(r'https://drive.google.com/[^"\s]/view', res.text)
print(f"Possible video links found: {links}")