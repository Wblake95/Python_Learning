#! /usr/bin/env python3

class MyCounter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 30:
            x = self.a
            self.a += self.a
            return x
        else:
            raise StopIteration

myclass = MyCounter()
MyForLoop = iter(myclass)

for x in MyForLoop:
    print(x)
