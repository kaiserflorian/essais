__author__ = 'kaiserfl'

from datetime import datetime

# Récuperer la date/heure système
maintenant = datetime.now()

# Demander année de naissance
annee_courante = maintenant.year
reponse = input("Quelle est votre année de naissance ?")

# Calculer la différence entre année courante et année de naissance
calcul = annee_courante - int(reponse)

if calcul >= 0:
    print("Vous avez environ " + str(calcul) + " ans")
    if calcul > 105:
        print("Ouhlala, vous êtes en très bonne santé...")
    if calcul > 200:
        print("Euh tu n'est pas en train de tricher???????")
else:
    print("Tu rigoles, t'es même pas encore né!")

