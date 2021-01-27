# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

month = 8
date = 30
day = "금요일"
city = "서울"
temperature = 26.5

s = "%d월 %d일 %s 현재 %s 기온은 %.1f도입니다."

print(s % (month,date,day,city,temperature))
