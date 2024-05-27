'''
Created on May 23, 2024
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
@author: Wenzhuo Liang
'''
for i in range(2, 85):
    if 168 % i == 0:
        j = 168 / i
        if (i + j) % 2 == 0 and (i - j) % 2 == 0 and i > j:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)