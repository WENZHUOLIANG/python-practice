'''
Created on May 24, 2024
题目：打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，
其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

程序分析：利用for循环控制100-999个数，每个数分解出个位，十位，百位。
@author: Wenzhuo Liang
'''
def analyze(i):
    l = []
    l.append(int(i/100))
    l.append(int(i%100/10))
    l.append(int(i%100%10))
    return l

for i in range(100, 1000):
    arr = analyze(i)
    if(arr[0]**3 + arr[1]**3 + arr[2]**3 == i):
        print(i)

