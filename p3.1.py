from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.edge.service import Service

# This is often needed if automatic detection fails
# You would replace the path with the location of your msedgedriver.exe
# service = Service(executable_path="/path/to/msedgedriver.exe") 
# browser = webdriver.Edge(service=service)

# Or, just try the simple call with the latest Selenium:
browser = webdriver.Edge()
browser.get("https://onlineradiobox.com/us/")
browser.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear
try:
    button = browser.find_element(By.XPATH, '//*[@id="b_top_play"]')
    button.click()  # Removed due to missing import
except Exception as e:
    print(f"An error occurred: {e}")
import time
time.sleep(100)  # Let the music play for 10 seconds
browser.quit()