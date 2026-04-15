# -------- CLASS & OBJECT --------
print("CLASS & OBJECT")

class Box:
    val = 10

    def show(self):
        print("Value:", self.val)

obj = Box()
obj.show()


# -------- SINGLE INHERITANCE --------
print("\nSINGLE INHERITANCE")

class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

obj = Dog()
obj.sound()
obj.bark()


# -------- MULTIPLE INHERITANCE --------
print("\nMULTIPLE INHERITANCE")

class A:
    def one(self):
        print("One")

class B:
    def two(self):
        print("Two")

class C(A, B):
    def three(self):
        print("Three")

obj = C()
obj.one()
obj.two()
obj.three()


# -------- MULTILEVEL INHERITANCE --------
print("\nMULTILEVEL INHERITANCE")

class X:
    def a(self):
        print("A")

class Y(X):
    def b(self):
        print("B")

class Z(Y):
    def c(self):
        print("C")

obj = Z()
obj.a()
obj.b()
obj.c()


# -------- HIERARCHICAL INHERITANCE --------
print("\nHIERARCHICAL INHERITANCE")

class P:
    def show(self):
        print("Parent")

class Q(P):
    def one(self):
        print("Child1")

class R(P):
    def two(self):
        print("Child2")

o1 = Q()
o2 = R()

o1.show()
o1.one()

o2.show()
o2.two()


# -------- POLYMORPHISM --------
print("\nPOLYMORPHISM")

class Add:
    def calc(self):
        print("Add:", 2 + 3)

class Mul:
    def calc(self):
        print("Mul:", 2 * 3)

a = Add()
b = Mul()

a.calc()
b.calc()
