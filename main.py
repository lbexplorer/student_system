# coding=utf-8
# !/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
student = {'name': '', 'number': ''}
students = []
find_student = []


# 用students表示有多个学生，每个学生的信息用一个字典表示，student中包含一个学生的姓名和学号（暂时）

def add_student():
    i = 1
    while True:
        try:
            student['name'] = input("Please enter the student name")
            student['number'] = input("Please enter number")

            students.append(student.copy())  # 再次输入是会将已经传入列表的第一个学生信息覆盖
            another = input("Whether to continue input y/n")
            if another.lower() == 'n':
                break
        except ValueError:
            print("输入错误，请输入数字！")
            continue


def search_student():
    # 按名字搜索和按学号搜索，先确定选取哪种方法
    while True:
        try:
            another = input("how to search number/name")
            if another.lower() == 'name':
                need_to_find = input(
                    "please input need to find {}".format(another))  # another可以是名字或者学号,将another与字典中所有属性相匹配若符合则返回
            temp=search(need_to_find)
            if temp!=0:
                find_student.append(temp.copy())

            elif another.lower() == 'number':
                need_to_find = int(input("please input need to find {}".format(another)))
            temp = search(need_to_find)
            if temp != 0:
                find_student.append(temp.copy())

            another = input("Whether to continue find (y/n)")
            if another.lower() == 'n':
                break
        except ValueError:
            print("输入错误，请重新输入！")
            continue


def search(need_to_find):
    flag = 1  # flag为1时表示没有找到目标学生
    for student in students:
        if student['name'] == need_to_find or student['number'] == need_to_find:
            print("name: ", student['name'])
            print("number: ", student['number'])
            print("\n")
            flag = 0
            return student

    if flag:
        print("no find ")
        return 0


def delete_student():
    temp = input("Please tell me the student information you want to delete-number/name")
    if temp.lower() == 'name':
        need_to_find = input("please input need to find {}".format(temp))
        delete(need_to_find)
    elif temp.lower() == 'number':
        need_to_find = int(input("please input need to find {}".format(temp)))  # 与查找信息原理相同，先找到再删除
        delete(need_to_find)


def delete(need_to_find):
    for student in students:
        if student['name'] == need_to_find or student['number'] == need_to_find:
            students.remove(student)
            print("have been delete")
            break


def show_student():
    aim_student = {}
    search_student()
    print("name: ", student['name'])
    print("number: ", student['number'])
    pass


def main():
    while True:
        print("1. add message")
        print("2. check message")
        print("3. remove information")
        print("4.Display student information")
        print("5. exit")
        choice = input("Please enter the action to be performed:")
        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            show_student()
        elif choice == '5':
            print("Program has exited!")
            break
        else:
            print("Input error, please re-enter!")
    pass


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
