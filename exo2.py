import sys
fichier= sys.argv[1]

with open(fichier, "a") as f:
    f.write("Hello world\n")
