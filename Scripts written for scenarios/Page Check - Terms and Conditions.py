from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, datetime
from HOP_functions import *
import difflib
import logging
import os

logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = "false"

print('-' * 120)
url = input('Paste scheme website you want to test (you can paste link here by using right click):\n')
scheme_name = input("\nPlease enter evidence file name (file name will look like this: HOP_<\033[1mtext that you're going to type below\033[0m>_<name of the subpage>.txt):\n")

evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions.txt","w") 
evidence_file.close()
evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions.txt","a", encoding="utf-8")
now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file.write(f"{today}\n{current_time}\n")
evidence_file.close()

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) 
driver.get(f"{url}")
driver.maximize_window()
accept_cookies(driver)

open_terms(driver)
terms_wording = driver.find_elements(By.XPATH, '//*[@id="tncPage"]')
scheme_wording = ""
for terms_text in terms_wording:
    scheme_wording += terms_text.text

scheme_wording = scheme_wording + "\n" + "\n"
driver.quit()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")
driver.maximize_window()
accept_cookies(driver)

open_terms(driver)
terms_wording = driver.find_elements(By.XPATH, '//*[@id="tncPage"]')
demo_wording = ""
for terms_text in terms_wording:
    demo_wording += terms_text.text

demo_wording = demo_wording + "\n" + "\n"
driver.quit()

if demo_wording == scheme_wording:
    print('-' * 120)
    print(f"\n\033[1mTerms and Conditions page wording the same for both demo and scheme page!\033[0m\n")
    evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions.txt","a", encoding="utf-8")
    evidence_file.write(f"R E S U L T S  O F  T H E  T E S T: Terms and Conditions page wording the same for both demo and scheme page!\n\n")
    evidence_file.write(f"\nWording pulled from {scheme_name} page:\n\n{scheme_wording}")
    evidence_file.write(f"\nWording pulled from Corvidae page:\n\n{demo_wording}")
    evidence_file.close()

else:
    print('-' * 120)
    print (f"\n\033[1mTerms and Conditions page wording NOT the same for demo and scheme page!\033[0m\n")
    evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions.txt","a", encoding="utf-8")
    evidence_file.write(f"R E S U L T S  O F  T H E  T E S T: Terms and Conditions page wording NOT the same for demo and scheme page!\n\n")
    evidence_file.write(f"\nWording pulled from {scheme_name} page:\n\n{scheme_wording}")
    evidence_file.write(f"\nWording pulled from Corvidae page:\n\n{demo_wording}")
    evidence_file.close()
    evidence_file_diff = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions_differences.txt","w", encoding="utf-8")
    evidence_file_diff.close()
    evidence_file_diff = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Terms_And_Conditions_differences.txt","a", encoding="utf-8")
    evidence_file_diff.write(f"Lines starting with - are from {scheme_name} scheme\nLines starting with + are from demo\n\n")
    scheme_wording_list = scheme_wording.split("\n")
    demo_wording_list = demo_wording.split("\n")
    d = difflib.Differ()
    diff = d.compare(scheme_wording_list, demo_wording_list)
    evidence_file_diff.write('\n'.join(diff))
    evidence_file_diff.close()

print('-' * 120)
print("\n\033[1mEvidence file was successfully generated!\033[0m\n")