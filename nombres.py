__author__ = 'kaiserfl'
total =0
for i in range(1,100,1):
    print("J'ajoute " + str(i) + " au total de " + str(total))
    total = total + i
    if total>100:
        print("J'en ai marre...")
        break

print(total)