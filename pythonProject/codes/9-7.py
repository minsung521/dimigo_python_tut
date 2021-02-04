# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

apple = int(input())  # 사과 수
banana = int(input())  # 바나나 수
kiwi = int(input())  # 키위 수

fruits = {"apple": apple, "banana": banana, "kiwi": kiwi}

total = 0

for i in fruits.values():
    total = total + i

print(total)