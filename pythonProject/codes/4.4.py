# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = int(input())
b = int(input())
c = int(input())


def my_max(a, b, c):
    return a if a > b and a > c else (b if b > c else c)


print(my_max(a, b, c))