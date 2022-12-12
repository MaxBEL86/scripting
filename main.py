import sys
import os

directory_input = sys.argv[1]

a = os.listdir(directory_input)

for number,directory in enumerate(a) : 
    print(f"{number} . {directory}")
print(f"Le contenu de mon répertoire : {a}")