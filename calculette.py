#! /usr/bin/env python
# -*- coding: utf-8 -*-

print("La calculette")
try:
    a = int(input("Entrez le chiffre a:"))
except ValueError:
    print("Hého - c'est pas un chiffre")
    exit()

operation = input("Entrez l'opération:")
b = input("Entrez b:")

print("a=" + str(a))
print("b=" + str(b))

# A faire:
# 1) Simplifier les tests
# 2) Ignorer majuscules / minuscules de l'opération
# 3) Vérifier division avec restes...
# 4) Vérifier les saisies b et operation comme pour le a

if operation=="+":
    resultat = a + b
elif operation=="-":
    resultat = a - b
elif operation=="*":
    resultat = a * b
elif operation=="/":
    resultat = a / b
elif operation=="fois":
    resultat = a * b
elif operation=="divisé":
    resultat = a / b
elif operation=="plus":
    resultat = a + b
elif operation=="moins":
    resultat = a - b
else:
    print(str(operation) + "?????")
    print("Désolé mais je ne sais pas encore faire ceci... faut demander à Doughy de me l'apprendre")
    print("Par contre je suis malin et je sais déjà faire: + - * / plus moins fois divisé")
    exit()

print("Le résultat de a " + str(operation) + " b = " + str(resultat))
