#!/usr/bin/env python3

'''
1002561
17,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,409,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,373,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,19
['17', '37', '409', '29', '13', '23', '373', '41', '19']
'''


#1-Lecture fichier et init variables
with open("input","r") as f:
	my_Array = f.read().splitlines()
	
time_Stamp = int(my_Array[0])
liste_bus = my_Array[1].split(',')

#2-Conservation bus interessants
lignes_bus = [int(bus) for bus in liste_bus if bus != 'x']

#3-Calcul des temps d'attente (pourrait etre interessant de faire une fonction)
attente_bus = []
for numero in lignes_bus:
	attente_bus.append(numero - (time_Stamp % numero))

magic_index = attente_bus.index(min(attente_bus))

result = attente_bus[magic_index] * lignes_bus[magic_index]

print(result)
