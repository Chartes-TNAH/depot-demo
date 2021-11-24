import sys
import os


# Récupère le chemin du dossier actuel
thisdir = os.getcwd()

errors = 0
files = 0

# r=Racine, d=Sous-dossiers, f = Fichiers
for r, d, f in os.walk(thisdir):
    # Pour chaque fichier
    for file in f:
        if file == ".gitignore" or ".git" in r:
            # On ignore les fichier dans les dossiers contenant ".git" (Donc .github et le dossier caché .git)
            continue
        elif file == "LICENSE" or file == "test_files.py":
            # On ignore le fichier LICENSE et le fichier pour faire les tests
            continue 
        elif not file.lower().endswith(".md"):
            # Si le fichier ne finit pas par l'extension .md, 
            #   C'est que c'est un mauvais fichier
            errors += 1
            files += 1
            print("Erreur: fichier " + file + " ne finit pas par MD")
        else:
            # Pour les autres fichiers
            files += 1

if files == 0:
	files = 1 # Pour éviter une division par 0

print("======")
print(str(errors/files*100)+"% des fichiers ont une mauvaise extension")

if errors > 0:
	sys.exit(1)
