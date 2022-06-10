from datetime import date, datetime
from HOP_functions import *
import difflib

# scheme name is very imporatant below - if you type it wrong script won't find correct evidence file :) 
# so the code below is opening correct evidence file and loads it to the variable "scheme_wording"

scheme_name = input("\n\033[1mPlease enter scheme name that you want to test\033[0m\n(don't use '&' and seperate words with '_' ===> for example AT&T should be written as ATT and Anglian Water as Anglian_Water):\n")
with open(f"Scheme tests\Generated Evidence\HOP_{scheme_name}_Evidence.txt", encoding='utf8') as scheme_page_evidence:
    scheme_wording = scheme_page_evidence.read()

# code below is opening evidence file of demo website and loads it to the variable "demo_wording"
    
with open("Scheme tests\Generated Evidence\HOP_Corvidae_Evidence.txt", encoding='utf8') as demo_page_evidence:
    demo_wording = demo_page_evidence.read()

# here evidence file that will be generated from this script is prepared with date and time 

evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","w") 
evidence_file_diff.close()
evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file_diff.write(f"{today}\n{current_time}\n")
evidence_file_diff.close()

#below is the part where wording from both pages will be compared and saved into evidence file

evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
evidence_file_diff.write(f"Lines starting with - are from {scheme_name} scheme\nLines starting with + are from demo\n\n")
scheme_wording_list = scheme_wording.split("\n")
demo_wording_list = demo_wording.split("\n")
d = difflib.Differ()
diff = d.compare(scheme_wording_list, demo_wording_list)
evidence_file_diff.write('\n'.join(diff))
evidence_file_diff.close()

print('-' * 120)
print("\n\033[1mEvidence file was successfully generated!\033[0m\n")
