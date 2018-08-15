# -*- coding: utf-8 -*-
# @Time    : 2018/8/14 7:59
# @Author  : Ryu
# @Site    : 
# @File    : main.py
# @Software: PyCharm

import main_tool
num_gl = []
num_glin = []

if __name__ == '__main__':
    while True:
        main_tool.welcome()
        num_glin = main_tool.Input()
        num_gl = main_tool.random_num()
        grade = main_tool.ceck(num_glin,num_gl)
        if grade != 0:
            print("恭喜你！中奖了！中奖金额为 %d" % grade)