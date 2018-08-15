# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 16:32
# @Author  : Ryu
# @Site    : 
# @File    : output.py
# @Software: PyCharm
"""
界面输入函数
"""
import numfuction

def welcome():
    """欢迎界面"""
    print("*"*50)
    print("名片管理系统 V1.0")
    print("欢迎使用名片管理系统！")
    print("")
    print("1.增加名片","2.显示所有名片","3.名片查询")
    print("")
    print("0.推出系统")
    print("*"*50)
    print("您出入的编号为：")
    return input()

def show_alldate():
    print("姓名\t\t","性别\t\t","电话\t\t")
   # print('*'*25)
    for i in numfuction.all_date:
        print(i[0]+"\t\t",i[1]+"\t\t",i[2]+"\t\t")
    #print(numfuction.all_date)
    print("按任意键返回主菜单！")
    input()