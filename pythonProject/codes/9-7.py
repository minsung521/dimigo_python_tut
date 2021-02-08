# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

apple = int(input())  # 사과 수
apple_price = int(input())  # 사과 단가
banana = int(input())  # 바나나 수
banana_price = int(input())  # 바나나 단가
kiwi = int(input())  # 키위 수
kiwi_price = int(input())  # 키위 단가

dic = {"apple": (apple, apple_price), "banana": (banana, banana_price), "kiwi": (kiwi, kiwi_price)}

total = 0

for i in dic.keys():
    total = total + dic[i][0] * dic[i][1]

print(total)