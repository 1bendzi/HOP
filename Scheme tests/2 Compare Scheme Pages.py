from datetime import date, datetime
from HOP_functions import *
import difflib

scheme_name = input("Please enter scheme name that you want to test (don't use '&' and seperate words with '_'\n(for example AT&T should be written as ATT):\n")

with open(f"Scheme tests\Generated Evidence\HOP_{scheme_name}_Evidence.txt", encoding='utf8') as scheme_page_evidence:
    scheme_wording = scheme_page_evidence.read()

    
with open("Scheme tests\Generated Evidence\HOP_Corvidae_Evidence.txt", encoding='utf8') as demo_page_evidence:
    demo_wording = demo_page_evidence.read()

evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","w") 
evidence_file_diff.close()
evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file_diff.write(f"{today}\n{current_time}\n")
evidence_file_diff.close()

evidence_file_diff = open(f"Scheme tests\Compare Scheme Pages - evidence\HOP_{scheme_name}_compared_to_demo.txt","a", encoding="utf-8")
evidence_file_diff.write(f"Lines starting with - are from {scheme_name} scheme\nLines starting with + are from demo\n\n")
scheme_wording_list = scheme_wording.split("\n")
demo_wording_list = demo_wording.split("\n")
d = difflib.Differ()
diff = d.compare(scheme_wording_list, demo_wording_list)
evidence_file_diff.write('\n'.join(diff))
evidence_file_diff.close()
