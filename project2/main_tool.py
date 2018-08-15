# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 7:59
# @Author  : Ryu
# @Site    : 
# @File    : main_tool.py
# @Software: PyCharm
import random

def welcome():
    """定义欢迎界面"""
    print('*' * 50)
    print('*' * 50)
    print("欢迎使用彩票模拟系统！ V1.0")



def Input():
    """定义输入函数"""
    my_num = []
    my_numlist = []
    my_num = input("请输入您的彩票号码：")
    my_num = my_num.split(" ")
    for i in my_num:
        my_numlist.append(int(i))
    print("您输入彩票号码为：",my_numlist)
    return my_numlist



def random_num():
    """生成中奖号码"""
    num_gl = range(1,34)
    num_gl = random.sample(num_gl,6)
    num_gl.sort()
    #num_base2 = random.randint(1,17)
    num_gl.append(random.randint(1,17))
    print("中奖号码为：",num_gl)
    return num_gl


def ceck(num_glin,num_gl):
    """中奖比对"""
    #蓝号比对
   # print(num_glin)
   # print(num_gl)
    if num_gl.pop() == num_glin.pop():
        blue_num = 1
    else:
        blue_num = 0
    #红号比对
    red_num = 0
    for i in num_glin:
        if i in num_gl:
            red_num = red_num + 1
    #兑奖

    if red_num == 6 and blue_num == 1:
        return 5000000
    elif red_num == 6:
        return 150000
    elif red_num == 5 and blue_num == 1:
        return 3000
    elif (red_num == 5) or (red_num == 4 and blue_num == 1):
        return 200
    elif (red_num == 4) or (red_num == 3 and blue_num == 1):
        return 10
    elif (red_num == 2 and blue_num == 1) or (red_num == 1 and blue_num == 1) or (blue_num == 1):
        return 5
    else:
        print("很遗憾，未中奖！")
        return 0
    #print("中奖结果")
