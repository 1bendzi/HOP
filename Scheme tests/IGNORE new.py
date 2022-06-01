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

for i in range(1, 14, 2):
    i = str(i)
    try:
        time.sleep(2)
        faq_header = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ui-id-'+ i +'"]')))
        time.sleep(2)
        faq_header.click()
        time.sleep(2)
        faq_header.click()
    except:
        print("N O P E ")

driver.quit()
