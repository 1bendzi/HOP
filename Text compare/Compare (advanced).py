import difflib

scheme_website_evidence = open("Text compare\Files to compare\scheme.txt","r", encoding="utf-8")
demo_website_evidence = open("Text compare\Files to compare\demo.txt","r", encoding="utf-8")

scheme_wording = scheme_website_evidence.read()
demo_wording = demo_website_evidence.read()

scheme_website_evidence.close()
demo_website_evidence.close()

evidence_file_diff = open("Text compare\Evidence\Difference advanced.txt","w", encoding="utf-8")
evidence_file_diff.close()
evidence_file_diff = open("Text compare\Evidence\Difference advanced.txt","a", encoding="utf-8")
scheme_wording_list = scheme_wording.split("\n")
demo_wording_list = demo_wording.split("\n")
d = difflib.Differ()
diff = d.compare(scheme_wording_list, demo_wording_list)
evidence_file_diff.write('\n'.join(diff))
evidence_file_diff.close()