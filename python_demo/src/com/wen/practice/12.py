'''
Created on May 24, 2024
题目：判断101-200之间有多少个素数，并输出所有素数。

程序分析：
1. 
判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 
@author: Wenzhuo Liang
'''
import math

def isPrime(n):
    if(n <= 3):
        return n > 1
    else:
        end = int(math.sqrt(n))
        for i in range(2, end+1):
            if(n % i == 0):
                return False
        return True
count = 0
for k in range(101, 201):
    if(isPrime(k)):
        print(k, end=" ")
        count+=1
print("")
print("Total is %d" % count)
