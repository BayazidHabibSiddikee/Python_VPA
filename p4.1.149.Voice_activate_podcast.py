from io import BytesIO
import requests
import bs4
from pygame import mixer
# Import functions from the local package
from mptpkg import voice_to_text, print_say
def news_brief():
    # Locate the website for the NPR news brief
    url = 'https://www.npr.org/podcasts/500005/npr-news-now'
    # Convert the source code to a soup string
    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # Locate the tag that contains the mp3 files
    casts = soup.find_all('a', {'class': 'audio-module-listen'})
    # Obtain the web link for the mp3 file
    cast = casts[0]['href']
    # Remove the unwanted components in the link
    mp3 = cast.find("?")
    mymp3 = cast[0:mp3]
    # Play the mp3 using the pygame module
    mymp3 = requests.get(mymp3)
    voice = BytesIO()
    voice.write(mymp3.content)
    voice.seek(0)
    mixer.init()
    mixer.music.load(voice)
    mixer.music.play()
while True:
    print_say('Python is listening…')
    inp = "news" #voice_to_text().lower()
    print_say(f'you just said: {inp}')
    if inp == "stop listening":
        print_say('Goodbye!')
        break
    # If "news" in your voice command, play news brief
    elif "news" in inp: 
        news_brief()
        # Python listens in the background
        while mixer.music.get_busy():
            background = voice_to_text().lower()
            # Stops playing if you say "stop playing"
            if "stop playing" in background:
                mixer.music.stop()
                break
        continue