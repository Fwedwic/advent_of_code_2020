#!/usr/bin/env python3

#Ouverture input
with open("input","r") as f:
	my_array = f.readlines()
	
#Declaration variables

position_col = 0
liste_compteur_arbres = []
result = 1


#Code
for step in [1,3,5,7]:
	compteur_arbres = 0
	position_col = 0
	for line in my_array:
		element = line[position_col]
		if element == '#':
			compteur_arbres += 1
		position_col = (position_col + step) % 31
	liste_compteur_arbres.append(compteur_arbres)
	print(liste_compteur_arbres)
	
#Cas particulier lignes impaires
compteur_arbres = 0
position_col = 0

for line in my_array[0:len(my_array):2]:
	element = line[position_col]
	if element == '#':
		compteur_arbres += 1
	position_col = (position_col + 1) % 31

liste_compteur_arbres.append(compteur_arbres)

for nbre_arbres in liste_compteur_arbres:
	result = result * nbre_arbres
	 
	
print(result)
#1744787392 est la réponse

