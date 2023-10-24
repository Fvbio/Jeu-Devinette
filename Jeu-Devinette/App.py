import random

def jouer_au_niveau(niveau):
    if niveau == "facile":
        min_num, max_num, max_essais = 1, 50, 10
    elif niveau == "moyen":
        min_num, max_num, max_essais = 1, 100, 7
    elif niveau == "difficile":
        min_num, max_num, max_essais = 1, 200, 5
    else:
        print("Niveau non valide.")
        return

    nombre_a_deviner = random.randint(min_num, max_num)
    nombre_d_essais = 0

    print(f"Bienvenue dans le jeu de devinette ({niveau}) !")
    print(f"Je vais choisir un nombre entre {min_num} et {max_num}, et vous devez deviner ce nombre en {max_essais} essais maximum.")

    while nombre_d_essais < max_essais:
        essai = int(input("Entrez votre devinette : "))
        nombre_d_essais += 1

        if essai < nombre_a_deviner:
            print("Le nombre à deviner est plus grand.")
        elif essai > nombre_a_deviner:
            print("Le nombre à deviner est plus petit.")
        else:
            print(f"Bravo ! Vous avez deviné le nombre en {nombre_d_essais} essais.")
            break

    if nombre_d_essais == max_essais:
        print(f"Désolé, vous avez atteint le nombre maximal d'essais. Le nombre à deviner était {nombre_a_deviner}.")

    rejouer = input("Voulez-vous rejouer ? (Oui/Non) : ").lower()
    if rejouer == "oui":
        choisir_niveau()
    else:
        print("Merci d'avoir joué !")

def choisir_niveau():
    print("Choisissez un niveau :")
    print("1. Facile")
    print("2. Moyen")
    print("3. Difficile")
    niveau = input("Entrez le numéro du niveau (1/2/3) : ")
    
    if niveau == "1":
        jouer_au_niveau("facile")
    elif niveau == "2":
        jouer_au_niveau("moyen")
    elif niveau == "3":
        jouer_au_niveau("difficile")
    else:
        print("Choix non valide. Veuillez entrer 1, 2 ou 3.")
        choisir_niveau()

if __name__ == "__main__":
    choisir_niveau()
