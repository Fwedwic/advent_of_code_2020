#!/usr/bin/env python3
import numpy

#1-Lecture fichier et init variables
with open("input","r") as f:
	my_Array = f.read().splitlines()
	
liste_bus = my_Array[1].split(',')

#2-Conservation bus interessants
lignes_bus = [bus for bus in liste_bus if bus != 'x']

#3-Détermination des latences
latences = []
for element in lignes_bus:
	latences.append(liste_bus.index(element))
	
#3bis-On n'oublie de passer les bus en entiers dans une array qu'on appelle modulos et on stocke les restes plutôt que les latences
modulos = [int(entier) for entier in lignes_bus]
restes = []
for latence,modulo in zip(latences,modulos):
	restes.append(modulo-latence)

#4a-TC-calcul du produit des modulos n
produit = numpy.prod(modulos)

#4b-TC-recup des nouveaux modulaires (n_i)
produit_array = [produit] * len(modulos)
nouveaux_modulaires = numpy.divide(produit, modulos)
entiers_modulaires = [int(entier) for entier in nouveaux_modulaires]
print(entiers_modulaires)

#4c-TC-Theoreme de Bezout indique qu'existent x et y tels que x*modulo + y*entier_modulaire = 1 % modulo (car les bus sont tous des nombres premiers, a fortiori des nombres premiers entre eux
inverses_modulaires = []
for modulo,entier_modulaire in zip(modulos,entiers_modulaires):
	inverse_modulaire = pow(entier_modulaire, -1, modulo)
	inverses_modulaires.append(inverse_modulaire)

#4d-TC-Calcul du t
# On a les inverses_modulaires / les entiers_modulaires / les restes
t = 0
for i,j,k in zip(restes, entiers_modulaires, inverses_modulaires):
	t += i*j*k
	
temps_optimal = t % produit

print(temps_optimal)
