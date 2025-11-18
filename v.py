import pyautogui
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
import time
pyautogui.alert(
    text = (
        "Thank you! The HTML has been copied to your clipboard.\n\n"
        "You can now return to the script and continue."
        "I have so many shits to say I can't even begin to explain it all."
        "But just know that you're doing great and keep pushing forward!"
    ),
    title="Thank You!"
)
while True:
    time.sleep(1)
    pyautogui.alert(
        text=(
            "This is just to keep the script running. Close this alert to end the script"
            " at any time."
            "But know the current time is: " + time.strftime("%H:%M:%S")
        ),
        title="Script Running"
    )
        