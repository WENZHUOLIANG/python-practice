'''
Created on May 24, 2024
题目：暂停一秒输出。
@author: Wenzhuo Liang
'''

import time
myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)
