#!/usr/bin/env python3

count=0

with open("input.txt", 'r') as f:
	my_Array = f.readlines()
	
for i in range(len(my_Array)-1):
	for j in range(i,len(my_Array)-1):
		for k in range(j,len(my_Array)-1):
			somme = int(my_Array[i].split()[0]) + int(my_Array[j].split()[0]) + int(my_Array[k].split()[0])
			if somme == 2020:
				produit = int(my_Array[i].split()[0]) * int(my_Array[j].split()[0]) * int(my_Array[k].split()[0])
				break

print(produit)

