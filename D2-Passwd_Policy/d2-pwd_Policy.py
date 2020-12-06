#!/usr/bin/env python3

'''
6-7 z: dqzzzjbzz
13-16 j: jjjvjmjjkjjjjjjj
5-6 m: mmbmmlvmbmmgmmf
'''



compteur_Faux = 0

with open("input","r") as f:
	my_Array = f.readlines()
	
for i in range(len(my_Array)):
	mini = int(my_Array[i].split('-')[0])
	maxi = int(my_Array[i].split('-')[1].split(' ')[0])
	token = my_Array[i].split(' ')[1][0]
	password = my_Array[i].split(':')[1]
	
	liste_Token = []
	liste_Token = [ letter for letter in password if letter == token ]
	
	if len(liste_Token) < mini:
		compteur_Faux += 1
	elif len(liste_Token) > maxi:
		compteur_Faux +=1
	
	#print(liste_Token)
	#print(token)
	#print(len(liste_Token))
	#print(mini)
	#print(maxi)
	#print(compteur_Faux)
	#input("?")
		
print(compteur_Faux)

