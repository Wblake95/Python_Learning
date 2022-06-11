#! /usr/bin/env python3

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(self.age,  self.name)

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationyear = year

    def welcome(self):
        print("Welcome ", self.name, "age ", self.age, "to class of ", self.graduationyear) 

x = Student("John", 27, 2019)
x.welcome()
