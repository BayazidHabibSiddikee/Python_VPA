# -*- coding: utf-8 -*-
"""
Find and play NBC Nightly News videos
"""
import requests
import bs4
import re
import webbrowser

url = 'https://www.nbcnews.com/nightly-news-full-episodes'

try:
    res = requests.get(url, timeout=10)
    res.raise_for_status()
except Exception as e:
    print(f"Error {e} occurred while fetching the webpage.")
    exit()

soup = bs4.BeautifulSoup(res.text, 'html.parser')

# Find MP4 video links
link = re.findall(r'https://[^"\s]+\.mp4', res.text)

if not link:
    print("No video links found")
    exit()

print(f"Found {len(link)} video link(s):")
for i, l in enumerate(link, 1):
    print(f"{i}. {l}")

# Choose which method to use
print("\nSelect method:")
print("1. Open in browser (simplest)")
print("2. Download and play with default player")
print("3. Play with VLC")

choice = input("Enter choice (1-3): ").strip()

video_url = link[0]  # Use first video found

# Method 1: Open in browser (RECOMMENDED - simplest)
if choice == "1":
    print(f"Opening {video_url} in browser...")
    webbrowser.open(video_url)

# Method 2: Download and play with default player
elif choice == "2":
    print("Downloading video...")
    video_data = requests.get(video_url, timeout=20)
    
    with open('nbc_news.mp4', 'wb') as f:
        f.write(video_data.content)
    
    print("Playing with default video player...")
    import os
    os.startfile('nbc_news.mp4')  # Windows
    # os.system('open nbc_news.mp4')  # Mac
    # os.system('xdg-open nbc_news.mp4')  # Linux
    import time
    time.sleep(100)  # Wait for a while to let the player start
    os.system('del nbc_news.mp4')  # Clean up after playing

# Method 3: Play with VLC
elif choice == "3":
    try:
        import vlc
        import time
        
        print(f"Playing {video_url} with VLC...")
        
        # VLC needs URL or file path, not BytesIO
        player = vlc.MediaPlayer(video_url)
        player.play()
        
        # Wait for video to load
        time.sleep(2)
        
        print("Playing... Press Ctrl+C to stop")
        input("Press Enter to stop...")
        player.stop()
    
    except ImportError:
        print("VLC not installed. Install with: pip install python-vlc")
    except Exception as e:
        print(f"Error playing video: {e}")

else:
    print("Invalid choice. Opening in browser...")
    webbrowser.open(video_url)