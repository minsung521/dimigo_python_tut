# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

d = {"apple": 1, "kiwi": 2, "banana": 3, "mango": 4, "melon": 5}

d2 = {}

for i in d.items():
    d2[i[1]] = i[0]

print(d2)
