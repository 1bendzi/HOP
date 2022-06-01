import subprocess

program_list = ['Scheme tests\HOP Corvidae (demo).py', 'Scheme tests\HOP Anglian Water.py', 'Scheme tests\HOP Heinz.py', 'Scheme tests\HOP Lloyds.py', 'Scheme tests\HOP MS.py', 'Scheme tests\HOP Pfizer.py', 'Scheme tests\HOP PG.py', 'Scheme tests\HOP Severn Trent.py', 'Scheme tests\HOP_ATT.py']
# program_list = ['Scheme tests\HOP Severn Trent.py', 'Scheme tests\HOP_ATT.py'] 

for program in program_list:
    subprocess.call(['python', program])
    print("Finished: " + program)