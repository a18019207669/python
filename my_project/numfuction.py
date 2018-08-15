# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 16:58
# @Author  : Ryu
# @Site    : 
# @File    : numfuction.py
# @Software: PyCharm
import output
all_date = []



def num_function1():
    """增加名片功能"""
    stu_date = []
    print("")
    print('*'*50)
    print("请输入姓名：")
    stu_date.append(input())
    print("请输入性别：")
    stu_date.append(input())
    print("请输入电话：")
    stu_date.append(input())
   # all_date.append(stu_date)
   # print(all_date)
    print("名片添加成功！返回主菜单")
    print('*' * 50)
    all_date.append(stu_date)
    print(all_date)
    return stu_date
   # output.welcome()

def Num_function2():
    """显示所有名片"""
    print("")
    if len(all_date) == 0:
        print("当前没有名片资料！")
       # output.welcome()
    else:
        output.show_alldate()


def Num_function3():
    """名片查询"""
    print("")
    print(all_date[1][0])
    name = input("请输入需要查询的姓名：")

    for i in all_date:
        if name == i[0]:
            print("查询到了")
            return
        else:
            print("没有此人")



