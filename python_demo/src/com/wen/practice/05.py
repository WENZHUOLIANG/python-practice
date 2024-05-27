'''
Created on May 24, 2024
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
@author: Wenzhuo Liang
'''
l = []
for i in range(3):
    num = int(input("enter number: "))
    l.append(num)
l.sort()
print(l)