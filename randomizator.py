import random
# listes classes
classes = ["Guerrier", "Sorcière", "Archère", "Arbalétrier", "Magicienne", "Moine"]
disciplines = ["Bâton", "Masse", "Arc", "Magie", "Nécromancie", "Arbalète"]
while True:
    # Générer une combinaison aléatoire
    classe_choisie = random.choice(classes)
    discipline_choisie = random.choice(disciplines)

    # Afficher le résultat
    print("\n Génération d'une classe aléatoire... ")
    print(f" {classe_choisie} - {discipline_choisie} ")

    # Demander à l'utilisateur s'il veut recommencer
    rejouer = input("\nVoulez-vous générer une autre classe ? (o/n) : ").strip().lower()
    if rejouer != 'o':
        print("\nMerci d'avoir utilisé le générateur ! À bientôt. ")
        break
