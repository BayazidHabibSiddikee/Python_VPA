from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from mptpkg import print_say, voice_to_text

button = None  # Initialize global variable

def live_radio():
    global button 
    edge_options = Options()  
    edge_options.add_argument("--headless")  # Fixed: -- instead of —
    browser = webdriver.Edge()  # Fixed: removed executable_path and edge_options parameter
    browser.get("https://www.nbcnews.com/nightly-news-full-episodes")
    
    # Fixed: use new syntax
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="content"]/div[6]/div/div[3]/div/section[2]/div[2]/div/div[1]/article/div[1]/h2/a[2]/span')))
    button.click()

while True:
    print_say("how may I help you?")
    inp = 'video' #voice_to_text().lower() 
    print_say(f'you just said {inp}')
    if inp == "stop listening": 
        print_say('Goodbye!')
        break
    elif "radio" in inp: 
        print_say('OK, play live radio online for you!')
        live_radio()
        while True:
            background = voice_to_text().lower()
            if "stop playing" in background:
                button.click()
                break
            else:
                continue