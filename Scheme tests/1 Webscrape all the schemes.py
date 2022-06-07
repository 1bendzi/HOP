import subprocess

# list of scripts that are going to be executed 

program_list = ['Scheme tests\HOP Corvidae (demo).py', 'Scheme tests\HOP Anglian Water.py', 'Scheme tests\HOP Heinz.py', 'Scheme tests\HOP Lloyds.py', 'Scheme tests\HOP MS.py', 'Scheme tests\HOP Pfizer.py', 'Scheme tests\HOP PG.py', 'Scheme tests\HOP Severn Trent.py', 'Scheme tests\HOP ATT.py']

# below is the "for" loop that will run scirpt one by one 

for program in program_list:
    subprocess.call(['python', program])
    print("Finished: " + program)