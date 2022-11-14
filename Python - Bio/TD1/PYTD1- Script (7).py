#mon 7e script python
from math import *
print("Calcul des solutions d'une equation du second degre")
a = int(input("Entrez la valeur de a "))
b = int(input("Entrez la valeur de b "))
c = int(input("Entrez la valeur de c "))
delta = b**2 - 4*a*c
print("Delta est égal à" , delta)
if delta == 0:
    print("Il n'y a qu'une racine à notre polynôme qui est," , -b / (2*a) )
elif delta > 0:
    S1 = (-b - sqrt(delta)) / (2*a)
    S2 = (-b + sqrt(delta)) / (2*a)
    print("Il y a deux racines à notre polynôme qui sont," + "S1:", S1, "et S2:", S2 )
else:
    print("Il n'y a aucune racine à notre polynôme.")
    
print("Merci de votre visite, à bientôt.")


