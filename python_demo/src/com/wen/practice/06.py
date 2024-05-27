'''
Created on May 24, 2024
题目：斐波那契数列。
@author: Wenzhuo Liang
'''

def feb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return feb(n-1) + feb(n-2)
print(feb(3))
print(feb(4))
print(feb(5))
print(feb(6))
