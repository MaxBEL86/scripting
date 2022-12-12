import sys 

try:
    fichier, contenu, fin = sys.argv[1], sys.argv[2], sys.argv[3]
except IndexError:
    print("il vous manque des arguments")

if len(sys.argv) == 5:
    num = sys.argv[4]
else:
    num = 1

try:
    with open(fichier, "a") as f:
        for i in range(int(num)):
            f.write(f"{contenu}\n")
        f.write(f"\n{fin}")
except NameError:
    print("impossible de trouver le fichier avec nom")

