#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Programme qui permet de faire des calculs et qui affiche les résultats
#
# TODO: Encoder les accents car sur la Tab il n'affiche pas les "divisé"...
#
__author__ = 'kaiserfl'

print("La calculette")

# Saisir le chiffre a
try:
    a = float(input("Entrez le chiffre a:"))
except ValueError:
    print("Hého - c'est pas un chiffre")
    exit()

# Saisir l'opération et convertir en minuscules
try:
    operation = input("Entrez l'opération:")
    operation = str.lower(operation)
except ValueError:
    print("Hého - c'est pas une opération")
    exit()

# Saisir le chiffre b
try:
    b = float(input("Entrez b:"))
except ValueError:
    print("Hého - c'est pas un chiffre")
    exit()

# Calcul en fonction de l'opération
if operation=="+" or operation=="plus":
    resultat = a + b
elif operation=="-" or operation=="moins":
    resultat = a - b
elif operation=="*" or operation=="fois":
    resultat = a * b
elif operation=="/" or operation=="divisé":
    resultat = a / b
elif operation=="**" or operation=="puissance":
    resultat = a ** b
elif operation=="//" or operation=="division entière":
    resultat= a//b
elif operation=="%" or operation=="modulo":
    resultat= a%b
else:
    print(str(operation) + "?????")
    print("Désolé mais je ne sais pas encore faire ceci... faut demander à Mr. Florian de me l'apprendre")
    print("Par contre je suis malin et je sais déjà faire:")
    print(" +, plus, -, moins, *, fois, /, divisé")
    print(" **, puissance, //, division entière, %, modulo ")
    exit()

# Afficher les valeurs et le résultat de l'opération
print("a=" + str(a))
print("b=" + str(b))
print("Le résultat de a " + str(operation) + " b = " + str(resultat))
    exit()
