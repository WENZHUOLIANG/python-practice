'''
Created on May 20, 2024
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
@author: Wenzhuo Liang
'''
input = [1,2,3,4]
result = 0
for i in input:
    for j in input:
        for k in input:
            if i != j and i !=k and j != k:
                result += 1
                print(i*100+j*10+k)
print(result)
