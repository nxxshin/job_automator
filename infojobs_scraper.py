import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# Create Chromeoptions instance 
options = webdriver.ChromeOptions() 
 
# Adding argument to disable the AutomationControlled flag 
options.add_argument("--disable-blink-features=AutomationControlled") 
 
# Exclude the collection of enable-automation switches 
options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
 
# Turn-off userAutomationExtension 
options.add_experimental_option("useAutomationExtension", False) 
 
# Setting the driver path and requesting a page 
DRIVER_PATH = '/selenium/chromedriver'
driver = webdriver.Chrome(options=options) 
 
# Changing the property of the navigator value for webdriver to undefined 
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# keyword in search: developer
driver.get('https://www.infojobs.net/trabajos.rss/kw_desarrollador/p_51/')

job_item_class = "ij-List-item"

print(driver.page_source)

df = pd.DataFrame(data = driver.page_source)

driver.quit()



