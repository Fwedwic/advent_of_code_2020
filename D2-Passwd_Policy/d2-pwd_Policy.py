#!/usr/bin/env python3

'''
6-7 z: dqzzzjbzz
13-16 j: jjjvjmjjkjjjjjjj
5-6 m: mmbmmlvmbmmgmmf
'''



compteur_vrai = 0

with open("input","r") as f:
	my_array = f.readlines()
	
for line in my_array:
	mini = int(line.split('-')[0])
	maxi = int(line.split('-')[1].split(' ')[0])
	token = line.split(' ')[1][0]
	password = line.split(':')[1]
	
	if (password.count(token) >= mini and password.count(token) <= maxi):
		compteur_vrai +=1
	
print(compteur_vrai)

