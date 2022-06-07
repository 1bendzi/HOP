from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from HOP_functions import *

chromedriver_autoinstaller.install()  
driver = webdriver.Chrome()
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")

driver.maximize_window()
accept_cookies(driver)
open_faq(driver)

# driver.execute_script("document.body.style.zoom='60%'")

for header in driver.find_elements(By.CLASS_NAME, "search-results-area"):
    link = header.find_element(By.CLASS_NAME, "accordion search-result")
    time.sleep(2)
    link.click()
 
driver.quit()

# $('div.search-results-area')[0].querySelectorAll('div.accordion.search-result').forEach(x => x.querySelector('h2').click())
