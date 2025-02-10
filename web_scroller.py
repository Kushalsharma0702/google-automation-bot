from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# List of crazy search queries 😜
search_queries = [
    "Why do cats rule the internet?",
    "How to become a billionaire in 10 days?",
    "Funniest memes of 2025",
    "What happens if you drink 10 cups of coffee?",
    "Selenium vs Human - Who wins?",
    "How to convince my laptop to run faster?",
    "Most ridiculous conspiracy theories",
    "Best programming language to talk to aliens",
    "Secret shortcuts in Google that nobody knows",
    "What if AI takes over my fridge?"
]

# Open browser
driver = webdriver.Chrome()

for i in range(10):  
    driver.execute_script("window.open('');")  # Open a new tab
    driver.switch_to.window(driver.window_handles[i])  # Switch to new tab
    driver.get("https://www.google.com")  

    # Find the search bar and type a random query
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(random.choice(search_queries) + Keys.RETURN)
    
    time.sleep(2)  # Wait for a bit before moving on

# Now, let’s close each tab **one by one** in **reverse order** like a boss 😎
for i in range(9, -1, -1):
    driver.switch_to.window(driver.window_handles[i])
    time.sleep(1)
    driver.close()

# Done! The chaos is complete. 🤯
