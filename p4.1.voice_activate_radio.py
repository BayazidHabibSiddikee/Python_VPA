from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from mptpkg import voice_to_text, print_say
''' Kono kamer na -_-'''
browser = None
button = None

def live_radio():
    global button
    global browser
    edge_options = Options()
    edge_options.add_argument("--headless")
    #chrome_options.add_argument("--headless")  # Fixed: use -- not -
    edge_options.add_argument("--no-sandbox")
    edge_options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Edge(options=edge_options)
    browser.implicitly_wait(10)
    button = browser.find_element(By.XPATH,'//*[@id="b_top_play"]')
    button.click()
    
while True:
    print_say("How may I help you?")
    inp = 'radio' #voice_to_text().lower()
    if 'stop' in inp or 'exit' in inp or 'close' in inp:
        print_say("Stopping the radio. Goodbye!")
        button.click()
        break
    elif 'radio' in inp:
        print_say("Radio is playing on.")
        live_radio()
        while True:
            background = voice_to_text().lower()
            if 'stop' in background or 'exit' in background or 'close' in background:
                print_say("Stopping the radio. Goodbye!")
                button.click()
                break
            else:
                continue