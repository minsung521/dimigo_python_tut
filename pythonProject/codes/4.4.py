# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a = int(input())  # 숫자1
b = int(input())  # 숫자2


def swap(a, b):
    return b, a
# def swap(a,b):
#     t = a
#     a = b
#     b = t


a, b = swap(a, b)

print(a, b)  # 실행 전에 미리 값을 예상해 보세요.
