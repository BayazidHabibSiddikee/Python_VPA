import pyautogui
import time, webbrowser
import pyperclip
import re
import os

print("Script starting...")

# 1. Open the URL
url = "https://classroom.google.com/u/1/c/NzM5MTQ1NjgyNTkx"
webbrowser.open(url)

print("Waiting 15 seconds for the page to load...")
print("Please make sure you are logged in and the page is visible.")
time.sleep(15) # Increased wait time for this heavy page

# --- THIS IS THE NEW, IMPORTANT PART ---
#
# We MUST get the *final* HTML, not the 'view-source' HTML.
# 'pyautogui' is blind and can't find the 'Elements' tab.
# So, we will prompt YOU to do the one step it can't.
#
print("ACTION REQUIRED: Please follow the popup instructions.")

pyautogui.alert(
    text=(
        "The script is paused.\n\n"
        "PLEASE DO THESE STEPS IN YOUR BROWSER:\n\n"
        "1. Right-click on your Classroom page.\n"
        "2. Click 'Inspect'.\n"
        "3. In the new panel, find the 'Elements' tab.\n"
        "4. Right-click the VERY FIRST line (it starts with '<html...')\n"
        "5. Go to 'Copy' -> 'Copy outerHTML'.\n\n"
        "Once the HTML is on your clipboard, click 'OK' on this box."
    ),
    title="Script Paused - Action Required"
)

# --- SCRIPT RESUMES ---
print("Script resuming...")
print("Getting HTML from clipboard...")
try:
    text = pyperclip.paste()
    if not text.startswith("<html"):
        print("ERROR: You did not copy the HTML correctly.")
        print("Please re-run the script and follow the steps.")
        exit()
        
except Exception as e:
    print(f"Failed to get text from clipboard: {e}")
    exit()

print("Successfully got HTML. Saving to file...")

# Save the *correct* source code
file_name = "source_code.txt"
with open(file_name, "w", encoding="utf-8") as f:
    f.write(text)

print(f"File '{file_name}' saved.")

# We don't need to close tabs, we can just minimize
try:
    pyautogui.hotkey('win', 'down') # Minimize the browser
except:
    pass # Ignore if this fails on non-Windows

# --- YOUR REGEX SCRIPT (Unchanged) ---
print("\nTime to webscrape!")

try:
    with open(file_name, "r", encoding="utf-8") as f:
        text = f.read()
        
        # This is your exact regex. It will work now.
        links = re.findall(r'https://drive.google.com/file/d/[^"\s]+/view', text)
        
        if not links:
            print("No matching Google Drive links were found in the final HTML.")
        else:
            print(f"--- SUCCESS! Found {len(links)} links: ---")
            for link in links:
                print(link)
                # Open all found links
                webbrowser.open_new_tab(link)
            print("\nAll links opened in new tabs.")

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found for reading.")
except Exception as e:
    print(f"An error occurred during regex search: {e}")

print("Script finished!")