import sys

current_word = None
current_count = 0

# Lecture de l'entrée standard
for line in sys.stdin:
    word, count = line.strip().split('\t')
    count = int(count)

    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"{current_word}\t{current_count}")  # Résultat final pour chaque mot
        current_word = word
        current_count = count

# Dernière ligne
if current_word:
    print(f"{current_word}\t{current_count}")