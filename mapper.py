import sys

# Lecture de l'entrée standard ligne par ligne
for line in sys.stdin:
    # Suppression des espaces blancs et conversion en minuscules
    line = line.strip().lower()
    words = line.split()  # Division en mots

    for word in words:
        print(f"{word}\t1")  # Format de sortie : mot et occurrence "1"
        
        