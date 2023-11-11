class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_mark(self, mark):
        self.mark = mark

    def get_student(self, mark, age, name):
        return name, age, mark

