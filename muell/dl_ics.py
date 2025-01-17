
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as fOptions
from selenium.webdriver.chrome.options import Options as cOptions
import os
import time

download_path=""
file="tonnenlerung.ics"

chrome_options = cOptions()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('prefs', {
    'download.default_directory': download_path,
    'download.prompt_for_download': False,
    'download.directory_upgrade': True,
    'safebrowsing.enabled': True
})

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tonnenleerung.de/nd-sob/schrobenhausen/hafnerweg/")

#fc-button fc-cta-consent fc-primary-button

driver.find_element(By.CLASS_NAME, "fc-button").click()
details=driver.find_element(By.TAG_NAME, "details")
driver.execute_script("arguments[0].setAttribute('open', 'open')", details);
element = driver.find_element(By.ID, "btn")

# click the element
element.click() 

#wait for file
while file not in os.listdir(download_path):
    time.sleep(1)
