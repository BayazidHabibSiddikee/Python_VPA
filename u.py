import pyautogui
import time, webbrowser

print("Script starting...")
print("Please switch to your browser window in the next 3 seconds...")

# Give yourself time to switch windows
url = "https://classroom.google.com/u/1/c/NzM5MTQ1NjgyNTkx"
webbrowser.open(url)
time.sleep(10)

# 1. Press a hotkey to open a new tab (Ctrl+T or Command+T)
#    PyAutoGUI is smart and will use 'command' on macOS and 'ctrl' on Windows/Linux.
print("Opening source-code...")
pyautogui.hotkey('ctrl', 'u')
# control + a and then control + c to copy all
time.sleep(3)  # Wait a second for the new tab to open
print("Selecting all...")
pyautogui.hotkey('ctrl', 'a')
time.sleep(1)  # Wait a second for the new tab to open
print("Copying...")
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)  # Wait a second for the new tab to open
import pyperclip
text = pyperclip.paste()[100:]  # get from clipboard
time.sleep(1)  # Wait a second for the new tab to open
pyautogui.hotkey('ctrl', 'w')
pyautogui.hotkey('ctrl','w')# close the tab of browser source code
# On Windows, you can use 'win' key to minimize window
pyautogui.hotkey('win', 'down')  # close the window of browser source code
#print(f"Text copied to clipboard.{text[:1000]}...")
with open("source_code.txt", "w", encoding="utf-8") as f:
    f.write(text)

# Wait a second for the new tab to open
time.sleep(1)
'''
# 2. Type out a string.
#    Adding a small interval makes the typing look more human and is more reliable.
print("Typing message...")
pyautogui.write('Hello, PyAutoGUI is typing this!', interval=0.08)

# 3. Press the Enter key
print("Pressing Enter...")
pyautogui.press('enter')
'''
print("Script finished!\nTime to webscrape!")

import re
with open("source_code.txt", "r", encoding="utf-8") as f:
    text = f.read()
    links = re.findall(r'https://drive.google.com/file/d/[^"\s]+/view', text)
    print(f"Possible video links found: {links}")
    for link in links:
        webbrowser.open(link)
        # https://drive.google.com/file/d/1I9eIYHttDa6jdfFMI-HUHdbovlsKifbS/view?usp=classroom_web&authuser=1