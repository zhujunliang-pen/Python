from webbrowser import get
from paramiko import Agent


class Student:
    name = 'Student'
    __age = 0
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'name=%s, score=%d, age=%d'% (self.name, self.score, self.age) 
    __repr__=__str__ #没有这句 print(repr(s1)) =  <__main__.Student object at 0x7f09b3746f70>
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if isinstance(value, int):
            self.__age = value

print(Student.name)
s = Student('Bob')
s.score = 90
s1 = Student('')
s1.score = 89
s1.age = 10
print(s1)
print(repr(s1))