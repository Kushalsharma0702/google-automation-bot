from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.chrome.options import Options

search_queries = [
    "Why do cats rule the internet?", "How to become a billionaire in 10 days?", 
    "Funniest memes of 2025", "Selenium vs Human - Who wins?", 
    "Secret shortcuts in Google that nobody knows"
]

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
options.add_argument("--headless=new")  
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

for i in range(3):  # Open fewer tabs (test stability first)
    driver.execute_script("window.open('');")  
    driver.switch_to.window(driver.window_handles[i])  
    driver.get("https://www.google.com")  
    time.sleep(random.uniform(2, 4))  

    search_box = driver.find_element(By.NAME, "q")
    search_text = random.choice(search_queries)
    
    for letter in search_text:
        search_box.send_keys(letter)
        time.sleep(random.uniform(0.1, 0.2))  
    search_box.send_keys(Keys.RETURN)
    
    time.sleep(random.uniform(2, 5))  
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  

for i in range(2, -1, -1):  
    driver.switch_to.window(driver.window_handles[i])  
    time.sleep(random.uniform(1, 3))  
    driver.close()

driver.quit()
