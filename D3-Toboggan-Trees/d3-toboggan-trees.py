#!/usr/bin/env python3

#Ouverture input
with open("input","r") as f:
	my_array = f.readlines()
	
#Declaration variables
compteur_arbres = 0
position_col = 0

#Code
	
for line in my_array:
	element = line[position_col]
	if element == '#':
		compteur_arbres += 1
	position_col = (position_col + 3) % 31 
	
print(compteur_arbres)
#affiche : 257
