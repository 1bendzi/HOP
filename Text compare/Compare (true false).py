from datetime import date 
import filecmp
from importlib.metadata import files

# This script will remove all new lines and whitespaces from both files (demo.txt and scheme.txt)

# Then script will compare both files if they are identical.


with open("Text compare\Files to compare\scheme.txt") as scheme_website_evidence:
    for line in scheme_website_evidence:
        line.strip()

scheme_website_evidence = open("Text compare\Files to compare\scheme.txt","w", encoding="utf-8")
scheme_website_evidence.write(line)
scheme_website_evidence.close()

with open("Text compare\Files to compare\demo.txt") as demo_website_evidence:
    for line in demo_website_evidence:
        line.strip()

demo_website_evidence = open("Text compare\Files to compare\demo.txt","w", encoding="utf-8")
demo_website_evidence.write(line)
demo_website_evidence.close()

scheme_website_evidence = open("Text compare\Files to compare\scheme.txt", "r", encoding="utf-8")  
demo_website_evidence = open("Text compare\Files to compare\demo.txt", "r", encoding="utf-8") 
  
today = str(date.today())
evidence_file = open("Text compare\Evidence\Difference line by line.txt","w", encoding="utf-8") #clearing file before saving anything in it 
evidence_file.close()
evidence_file = open("Text compare\Evidence\Difference line by line.txt","a", encoding="utf-8")
evidence_file.write(f"{today}\n")

filecmp.clear_cache()
demo = "Text compare\Files to compare\demo.txt"
scheme = "Text compare\Files to compare\scheme.txt"
result = filecmp.cmp(demo, scheme, shallow=False)

evidence_file.write(f"True - the files are the same \n")
evidence_file.write(f"False - the files are NOT the same \n")
evidence_file.write(f"\n")
evidence_file.write(f"R E S U L T:  ")
evidence_file.write(str(result))
evidence_file.close()

print(f"\n Done - evidence file was generated. \n")