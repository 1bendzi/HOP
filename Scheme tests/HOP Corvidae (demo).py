from selenium import webdriver 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from datetime import date
import time
from HOP_functions import *
# import requests
# import time
# from urllib import request 

today = str(date.today())
evidence_file = open("Scheme tests\Generated Evidence\HOP_Corvidae_Evidence.txt","w")
evidence_file.close()
evidence_file = open("Scheme tests\Generated Evidence\HOP_Corvidae_Evidence.txt","a", encoding="utf-8")
evidence_file.write(f"{today}\n")

chromedriver_autoinstaller.install()  
driver = webdriver.Chrome()
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")

driver.maximize_window()
accept_cookies(driver)
open_menu(driver)

# M E N U  H E A D E R S

evidence_file.write(f"*MENU HEADERS: *\n")
menu_items = driver.find_elements(By.XPATH, '//*[@id="globalTopMenu"]/div')
for x in range(len(menu_items)):
    evidence_file.write(menu_items[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# H E A D E R  R I G H T  S I D E 

header_right_scrape(driver, evidence_file)
return_to_home(driver)

# A A A  C H E C K 

smallest_a = driver.find_element(By.XPATH, '//*[@id="textSmall"]')
middle_a = driver.find_element(By.XPATH, '//*[@id="textMedium"]')
biggest_a = driver.find_element(By.XPATH, '//*[@id="textLarge"]')
contac_us_button = driver.find_element(By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[1]/a')

biggest_a.click()
time.sleep(1)
evidence_file.write("Contact Us font-size when biggest A is selected (correct value is: 26px): ")
evidence_file.write(contac_us_button.value_of_css_property("font-size"))
evidence_file.write("\n")

middle_a.click()
time.sleep(1)
evidence_file.write("Contact Us font-size when middle A is selected (correct value is: 23px): ")
evidence_file.write(contac_us_button.value_of_css_property("font-size"))
evidence_file.write("\n")

smallest_a.click()
time.sleep(1)
evidence_file.write("Contact Us font-size when smallest A is selected (correct value is: 20px): ")
evidence_file.write(contac_us_button.value_of_css_property("font-size"))
evidence_file.write("\n")
evidence_file.write("\n")

# P A G E  B O D Y  E L E M E N T S

evidence_file.write(f"*Page Body ELEMENTS: *\n")
homepage_general_elements = driver.find_elements(By.ID, "tilePageTiles")
for x in range(len(homepage_general_elements)):
    evidence_file.write(homepage_general_elements[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# F O O T E R

evidence_file.write(f"*Footer ELEMENTS: *\n")
footer_elements = driver.find_elements(By.CLASS_NAME, "hop-footer")
for x in range(len(footer_elements)):
    evidence_file.write(footer_elements[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# C O N T A C T  U S

open_contact_us_demo(driver)

evidence_file.write(f"*Contact Us WORDING: *\n")
contact_us_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(contact_us_wording)):
    evidence_file.write(contact_us_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# L O G I N (ACCESSED FROM HEADER BUTTON)

open_login_header(driver)

evidence_file.write(f"*LOGIN WORDING (from header button): *\n")
login_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(login_wording)):
    evidence_file.write(login_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# R E G I S T E R (ACCESSED FROM HEADER BUTTON)

open_register_header(driver)

evidence_file.write(f"*REGISTER WORDING (from header button): *\n")
register_wording = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]')
for x in range(len(register_wording)):
    evidence_file.write(register_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# L O G I N  N A M E  R E M I N D E R 

open_login_name_reminder(driver)

evidence_file.write(f"*LOGIN NAME REMINDER WORDING: *\n")
login_name_reminder_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/main/form')
for x in range(len(login_name_reminder_wording)):
    evidence_file.write(login_name_reminder_wording[x].text)
    evidence_file.write("\n")

evidence_file.write("\n")

# R E S E T  P A S S W O R D

open_reset_password(driver)

evidence_file.write(f"*RESET PASSWORD WORDING: *\n")
reset_password_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/main/form')
for x in range(len(reset_password_wording)):
    evidence_file.write(reset_password_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# R E S E T  P I N

open_reset_pin(driver)

evidence_file.write(f"*RESET PIN WORDING: *\n")
reset_pin_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/main/form')
for x in range(len(reset_pin_wording)):
    evidence_file.write(reset_pin_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# A P P L I C A T I O N  O P T I O N S

open_application_options(driver)

evidence_file.write(f"*Application Options page WORDING: *\n")
app_options_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(app_options_wording)):
    evidence_file.write(app_options_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# P E N S I O N  C O M M U N I C A T I O N (LINK CHECK, EXTERNAL PAGE)

# S C H E M E  I N F O R M A T I O N 

open_scheme_info(driver)
evidence_file.write(f"*Scheme Information WORDING: *\n")
scheme_information_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(scheme_information_wording)):
    evidence_file.write(scheme_information_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# I N V E S T M E N T  O P T I O N S

open_inv_options(driver)
evidence_file.write(f"*Investment Options WORDING: *\n")
inv_options_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(inv_options_wording)):
    evidence_file.write(inv_options_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# C O N T A C T  U S (ACCESSED FROM MENU)

open_contact_us_menu(driver)


# U S E F U L  A D D R E S S E S

open_useful_addresses(driver)
evidence_file.write(f"*Useful Addresses WORDING: *\n")
inv_options_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(inv_options_wording)):
    evidence_file.write(inv_options_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# U S E F U L  T E R M S 

open_useful_terms(driver)
evidence_file.write(f"*Useful Terms WORDING: *\n")
useful_terms_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]/div/main')
for x in range(len(useful_terms_wording)):
    evidence_file.write(useful_terms_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# L O G I N (ACCESSED FROM PAGE BODY BUTTON)

open_login_main(driver)

evidence_file.write(f"*LOGIN WORDING (from main page button): *\n")
login_wording = driver.find_elements(By.XPATH, '/html/body/div/div[2]/div[2]')
for x in range(len(login_wording)):
    evidence_file.write(login_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# R E G I S T E R (ACCESSED FROM PAGE BODY BUTTON)

open_register_main(driver)

evidence_file.write(f"*REGISTER WORDING (from main page button): *\n")
register_wording = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[2]')
for x in range(len(register_wording)):
    evidence_file.write(register_wording[x].text)
    evidence_file.write("\n")
evidence_file.write("\n")

# C A P I T A  P L C  (LINK CHECK, EXTERNAL PAGE)

# C A P I T A (LINK CHECK, EXTERNAL PAGE)

# A C C E S S I B I L I T Y 

open_accessibility(driver)

evidence_file.write(f"*Accessibility WORDING: *\n")
accessibility_wording = driver.find_elements(By.XPATH, '//*[@id="accessibility"]')
for x in range(len(accessibility_wording)):
    evidence_file.write(accessibility_wording[x].text)
    evidence_file.write("\n")

evidence_file.write("\n")

# P R I V A C Y  &  C O O K I E  P O L I C Y 

open_privacy(driver)

evidence_file.write(f"*Privacy & Cookie Policy WORDING: *\n")
privacy_wording = driver.find_elements(By.XPATH, '//*[@id="privacyPolicy"]')
for x in range(len(privacy_wording)):
    evidence_file.write(privacy_wording[x].text)
    evidence_file.write("\n")

evidence_file.write("\n")

# F A Q 

open_faq(driver)

evidence_file.write(f"*FAQ WORDING: *\n")
faq_wording = driver.find_elements(By.XPATH, '//*[@id="faq"]/section[2]/div')
for x in range(len(faq_wording)):
    evidence_file.write(faq_wording[x].text)
    evidence_file.write("\n")
    # print(faq_wording[x].text)
evidence_file.write("\n")

# T E R M S  &  C O N D I T I O N S

open_terms(driver)

evidence_file.write(f"*Terms & Conditions WORDING: *\n")
terms_wording = driver.find_elements(By.XPATH, '//*[@id="tncPage"]')
for x in range(len(terms_wording)):
    evidence_file.write(terms_wording[x].text)
    evidence_file.write("\n")

evidence_file.write("\n")
evidence_file.close()
driver.quit()