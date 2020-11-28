from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json

# Change DRIVER_PATH appropriately
DRIVER_PATH = '/PATH/TO/DRIVER/chromedriver'
ENGADGET_URL = 'https://www.engadget.com/gaming/'

# Start the driver
driver = webdriver.Chrome(executable_path=DRIVER_PATH)

# Fetch the URL
driver.get(ENGADGET_URL)

# Let's scroll the page for ten times, and Click on LoadMore button
for i in range(1, 10):
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight-75);")
  load_more_button = driver.find_element_by_xpath('//*[@id="LoadMore"]')
  driver.execute_script("arguments[0].click();", load_more_button)
  time.sleep(10)

# Get all posts
posts = driver.find_elements_by_xpath('//div[@class="D(f) Fld(c) Ai(fs)"]')

# Let's filter posts to have PS5 in their title
list_of_posts = []

for post in posts:
  title = post.find_element_by_xpath(".//a").text
  link = post.find_element_by_xpath(".//a").get_attribute('href')
  description = post.find_element_by_xpath(".//div").text
  date_posted = [a.text for a in posts[0].find_elements_by_xpath(".//span")][-1].split(',')[-1].strip()
  
  if 'PS5' in title or 'PlayStation 5' in title:
    list_of_posts.append({
      'title': title,
      'link': link,
      'description': description,
      'date_posted': date_posted
    })

# Dismiss the Browser
driver.quit()

# Dump the results as json file

with open('engadget.json', 'w') as f:
  json.dump(list_of_posts , f)