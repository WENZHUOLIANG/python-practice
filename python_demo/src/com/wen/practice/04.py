'''
Created on May 24, 2024
题目：输入某年某月某日，判断这一天是这一年的第几天？
@author: Wenzhuo Liang
'''

year = int(input("Year: \n"))
month = int(input("Month: \n"))
day = int(input("Day: \n"))

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 343)

if 1 < month < 13:
    sum = months[month-1]
else:
    print("invalid month")

sum += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum += 1
    
print ('it is the %dth day.' % sum)

