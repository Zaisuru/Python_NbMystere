#Decouverte du nombre myst-re#
#creation d'un nombre aleatoire entre 0 et 100
#Le joueur dispose de 5 essais
#Si il ne trouve pas fin du jeu et affichage du nombre mystère
#Si il trouve félications et fin du jeu#

import random

nb_myster = random.randint(0,100)
nb_essai = 5

print("Le jeu du nombre mystère ***")
while nb_essai > 0:
    print(f"Il te reste {nb_essai} essai{'s' if nb_essai > 1 else ''}")

    user_choice = input("Devine le nombre :")
    if not user_choice.isdigit():
        print("Veuillez rentrer un nombre")
        continue

    user_choice = int(user_choice)

    if nb_myster > user_choice:
        print(f"le nombre mystère est plus grand que {user_choice}")
    elif nb_myster < user_choice:
        print(f"le nombre mystère est plus petit que {user_choice}")
    else:
        break
    nb_essai -= 1

if nb_essai == +0:
    print("Fin du jeu, plus d'essai")
else :
    print("Bravo tu as trouvé le nombre mystère !")
    print(f"Tu as trouvé en {nb_essai} d'essai")

print("Fin du jeu")

