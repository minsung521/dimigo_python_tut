f = open("../files/test.txt", 'r')  # 파일 쓰기모드로 열기

for line in f:
	print(line, end="")

f.close()

#
# f = open('test.txt', 'r')
# lines = f.readlines()
# print(lines)  # 리스트로 출력
#
# for line in lines:
#     print(line, end='')
# f.close()