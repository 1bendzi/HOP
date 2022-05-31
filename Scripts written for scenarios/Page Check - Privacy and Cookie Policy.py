from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from datetime import date, datetime
from HOP_functions import *
import difflib

url_list = print('''
Anglian Water: https://qaportal.hartlinkonline.co.uk/myawgpension
Heinz: https://qaportal.hartlinkonline.co.uk/heinzpensions
Lloyds: https://qaportal.hartlinkonline.co.uk/lloydspensionscheme
M&S: https://qaportal.hartlinkonline.co.uk/mandspensionscheme
Pfizer: https://qaportal.hartlinkonline.co.uk/pfizer
P&G: https://qaportal.hartlinkonline.co.uk/procterandgamble
Severn Trent: https://qaportal.hartlinkonline.co.uk/severntrent
AT&T: https://qaportal.hartlinkonline.co.uk/attpensionscheme
''')
url = input('Paste scheme website you want to test (you can paste link here by using right click):\n')
scheme_name = input("Please enter scheme name that you want to test (don't use '&' and seperate words with '_'\n")

evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy.txt","w") 
evidence_file.close()
evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy.txt","a", encoding="utf-8")
now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file.write(f"{today}\n{current_time}\n")
evidence_file.close()

chromedriver_autoinstaller.install()  
driver = webdriver.Chrome()
driver.get(f"{url}")
driver.maximize_window()

accept_cookies(driver)
open_privacy(driver)
privacy_wording = driver.find_elements(By.XPATH, '//*[@id="privacyPolicy"]')
for x in range(len(privacy_wording)):
    scheme_wording = privacy_wording[x].text

scheme_wording = scheme_wording + "\n" + "\n"
driver.quit()

driver = webdriver.Chrome()
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")
driver.maximize_window()
accept_cookies(driver)
open_privacy(driver)
privacy_wording = driver.find_elements(By.XPATH, '//*[@id="privacyPolicy"]')
for x in range(len(privacy_wording)):
    demo_wording = privacy_wording[x].text

demo_wording = demo_wording + "\n" + "\n"
driver.quit()

if demo_wording == scheme_wording:
    print(f"\n\033[1mPrivacy and Cookie Policy page wording is the same for both demo and scheme page!\033[0m\n")
    evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy.txt","a", encoding="utf-8")
    evidence_file.write(f"R E S U L T S  O F  T H E  T E S T: Privacy and Cookie Policy page wording is the same for both demo and scheme page!\n\n")
    evidence_file.write(f"\nWording pulled from {scheme_name} page:\n\n{scheme_wording}")
    evidence_file.write(f"\nWording pulled from Corvidae page:\n\n{demo_wording}")
    evidence_file.close()

else:
    print (f"\n\033[1mPrivacy and Cookie Policy page wording is NOT the same for demo and scheme page!\033[0m\n")
    evidence_file = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy.txt","a", encoding="utf-8")
    evidence_file.write(f"R E S U L T S  O F  T H E  T E S T: Privacy and Cookie Policy page wording is NOT the same for demo and scheme page!\n\n")
    evidence_file.write(f"\nWording pulled from {scheme_name} page:\n\n{scheme_wording}")
    evidence_file.write(f"\nWording pulled from Corvidae page:\n\n{demo_wording}")
    evidence_file.close()
    evidence_file_diff = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy_differences.txt","w", encoding="utf-8")
    evidence_file_diff.close()
    evidence_file_diff = open(f"Scripts written for scenarios\Evidence\HOP_{scheme_name}_Privacy_And_Cookie_Policy_differences.txt","a", encoding="utf-8")
    evidence_file_diff.write(f"Lines starting with - are from {scheme_name} scheme\nLines starting with + are from demo\n\n")
    scheme_wording_list = scheme_wording.split("\n")
    demo_wording_list = demo_wording.split("\n")
    d = difflib.Differ()
    diff = d.compare(scheme_wording_list, demo_wording_list)
    evidence_file_diff.write('\n'.join(diff))
    evidence_file_diff.close()
