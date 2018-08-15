# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 16:05
# @Author  : Ryu
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import time
if __name__ == '__main__':
    start_time = time.time()
    for a in range(0,1001):
        for b in range(0,1001):
            for c in range(0,1001):
                if a+b+c==1000 and a**2+b**2==c**2:
                    print(a,b,c)
    end_time = time.time()
    print(end_time-start_time)