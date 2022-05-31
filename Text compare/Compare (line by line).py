from datetime import date

# This script will compare files line by line 
# 
# ---> so when files are missalinged it will show all the fallowing lines as not matching

string_without_empty_lines=""
with open("Text compare\Files to compare\scheme.txt") as scheme_website_evidence:
    for line in scheme_website_evidence:
        if not line.isspace():
            string_without_empty_lines+=line
            
scheme_website_evidence = open("Text compare\Files to compare\scheme.txt","w", encoding="utf-8")
scheme_website_evidence.write(string_without_empty_lines)
scheme_website_evidence.close()

string_without_empty_lines=""
with open("Text compare\Files to compare\demo.txt") as demo_website_evidence:
    for line in demo_website_evidence:
        if not line.isspace():
            string_without_empty_lines+=line        
            
demo_website_evidence = open("Text compare\Files to compare\demo.txt","w", encoding="utf-8")
demo_website_evidence.write(string_without_empty_lines)
demo_website_evidence.close()

scheme_website_evidence = open("Text compare\Files to compare\scheme.txt", "r", encoding="utf-8")  
demo_website_evidence = open("Text compare\Files to compare\demo.txt", "r", encoding="utf-8") 
  
today = str(date.today())
evidence_file = open("Text compare\Evidence\Difference line by line.txt","w", encoding="utf-8") #clearing file before saving anything in it 
evidence_file.close()
evidence_file = open("Text compare\Evidence\Difference line by line.txt","a", encoding="utf-8")
evidence_file.write(f"{today}\n")


i = 0
for line1 in scheme_website_evidence:
    i += 1
      
    for line2 in demo_website_evidence:
          
        # matching line1 from both files
        if line1 == line2:    
            evidence_file.write(f"line {i}: IDENTICAL \n")
        else:
            # else print that line from both files
            evidence_file.write(f"Line {i}: \n")
            evidence_file.write(f"Scheme website: {line1} \n")
            evidence_file.write(f"Demo website:   {line2} \n")
        break
  
print(f"\n Done - evidence file was generated. \n")
# closing files
scheme_website_evidence.close()                                       
demo_website_evidence.close()
evidence_file.close()