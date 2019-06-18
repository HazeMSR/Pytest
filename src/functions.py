
n = 1


def obtenerNumerico():
    return n 


def asignarNumerico(valor):
    n = valor 
    print(str(n))


def func(x):
    return x


def f():
    raise SystemExit(1)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
