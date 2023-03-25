import json
import os
import pickle



class Student:
    students = []

    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def add_student(cls, id, name):
        """
        添加学生
        :param id: 学生的id
        :param name: 学生的姓名
        """
        student = cls(id, name)
        cls.students.append(student)
        save_students(cls.students)

    @classmethod
    def delete_student(cls, id):
        """
        删除学生
        :param id: 学生的id
        :return: True表示删除成功，False表示删除失败
        """
        for student in cls.students:
            # 遍历所有学生，如果找到了对应id的学生，则删除该学生并返回True
            if student.id == id:
                cls.students.remove(student)
                save_students(cls.students)
                return True
        return False

    @classmethod
    def find_student(cls, id):
        """
        查找学生
        :param id: 学生的id
        :return: 学生对象，如果找不到则返回None
        """
        cls.students = load_students()
        for student in cls.students:
            if student.id == id:
                return student
        return None

    @classmethod
    def modify_student(cls, id, name):
        """
        修改学生信息
        :param id: 学生的id
        :param name: 学生的姓名
        :return: True表示修改成功，False表示修改失败
        """
        student = cls.find_student(id)
        if student:
            student.name = name
            save_students(cls.students)
            return True
        return False


def save_students(students):
    with open('students.txt', 'w', encoding='utf-8') as f:
        for student in students:
            f.write(f'{student.id},{student.name}\n')


def load_students():
        try:
            with open('students.txt', 'r', encoding='utf-8') as f:
                lines = f.readlines()
                students = [Student(*line.strip().split(',')) for line in lines]
        except FileNotFoundError:
            students = []
        return students