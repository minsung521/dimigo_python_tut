# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

fruits = ["banana", "apple", "kiwi", "grape"]

fruits.sort()

file = open('sort.txt','w')

for fruit in fruits:
	file.write(fruit+"\n")

file.close()

file = open('sort.txt','r')

for line in file.readlines():
	print(line,end='')

file.close()