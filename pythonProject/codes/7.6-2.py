# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

s = input()

l = ["c", "c++", "java", "python", "c#", "javascript"]

for lang in l:
	if lang.count(s):
		print(lang)