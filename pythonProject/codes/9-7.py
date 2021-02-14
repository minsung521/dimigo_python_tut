
file = open('../files/score.txt','w')
file.write("kor 100\n")
file.write("eng 95\n")
file.write("mat 90\n")
file.close()

file = open('../files/score.txt','r')
for line in file.readlines():
	print(line,end="")
file.close()