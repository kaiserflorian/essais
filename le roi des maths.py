#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Programme qui trouve des calculs a faire et qui demande a l'utillisateur de les faire
# mais avant d'afficher la réponse il demande la solution
#
__author__ = 'kaiserfl'
import random

print(">>> Le roi des maths <<<")
print("")

# Trouver un chiffre a
a = random.randint(1,100)

# Trouver une opération à faire
operations = ['plus', 'moins', 'divisé', 'fois', 'puissance', 'division entière', 'modulo']
operation = random.choice(operations)

# Trouver un chiffre b
b = random.randint(1,100)

# Afficher le calcul à faire
calcul = str(a) + " " + str(operation) + " " + str(b)
print("Trouve la réponse pour le calcul suivant: " + calcul)

# Demander la réponse
try:
    reponse = float(input("Réponse ?:"))
except ValueError:
    print("Hého - c'est pas un résultat valide")
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

# Comparer si la reponse est identique au resultat
print("")

if reponse==resultat:
    print("Bravo bonne réponse!!!!")
    exit()
else:
    print("Faux, la bonne réponse est: " + str(resultat))
    exit()
