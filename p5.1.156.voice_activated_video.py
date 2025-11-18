import requests, bs4, re, webbrowser

url ='https://www.nbcnews.com/nightly-news-full-episodes'
try:
    res = requests.get(url)
    res.raise_for_status()
except Exception as e:
    print(f"Error {e} occurred while fetching the webpage.")

soup = bs4.BeautifulSoup(res.text, 'html.parser')
episode = soup.find_all('script',{"type":"application/json"})
#episode = res.json()
#print(episode)

link = re.findall(r'https://[^"\s]+\.mp4',res.text)
#print(f"Possible video links found: {link}")

for l in link:
    #webbrowser.open(l)
    #from moviepy.editor import VideoFileClip
    #import pygame
    #clip = VideoFileClip(l)
    #clip.preview()  # This will open a window to play the video clip
    import vlc
    #from io import BytesIO
    #mp4 = requests.get(l)
    '''file = BytesIO()
    file.write(mp4.content)
    file.seek(0)
    import os
    os.system(f'start {file}')'''
    p = vlc.MediaPlayer(l)
    p.play()
    print("Playing... Press Ctrl+C to stop")
    input("Press Enter to stop...")
    p.stop()
    break  # Remove this break if you want to open all found links