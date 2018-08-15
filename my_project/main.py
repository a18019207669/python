# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 16:32
# @Author  : Ryu
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import output
import numfuction
all_date = []

def Num1():
    print("您的选择是1")

    numfuction.num_function1()


def Num2():
    print("您的选择是2")
    numfuction.Num_function2()


def Num3():
    print("您的选择是3")
    numfuction.Num_function3()


def Num0():
    print("您的选择是0")
    print("感谢您的使用，欢迎下次再来！")


if __name__ == '__main__':
    # print("hello,world!")
    getNum = output.welcome()
    while(1):
        if getNum == '1':
            Num1()
        elif getNum == '2':
            Num2()
        elif getNum == '3':
            Num3()
        else:
            Num0()
        getNum = output.welcome()
