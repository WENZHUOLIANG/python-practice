'''
Created on May 24, 2024
题目：暂停一秒输出，并格式化当前时间。

print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
 
# 暂停一秒
time.sleep(1)
 
print (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
@author: Wenzhuo Liang
'''
import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())));

time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())));