Python OOP Concepts – Beginner Friendly README

📌 Overview

This program demonstrates basic Object-Oriented Programming (OOP) concepts in Python. It is written in a simple and beginner-friendly way to help understand how classes, objects, inheritance, and polymorphism work.

---

🧱 1. Class & Object

What is a Class?

A class is like a blueprint for creating objects.

What is an Object?

An object is an instance of a class.

Code Explanation:

class Box:
    val = 10

    def show(self):
        print("Value:", self.val)

- "Box" is a class
- "val" is a variable inside the class
- "show()" is a method (function inside class)

obj = Box()
obj.show()

- "obj" is an object of class "Box"
- It calls the "show()" method

---

🐶 2. Single Inheritance

Definition:

One child class inherits from one parent class.

Code:

class Animal:
    def sound(self):
        print("Sound")

class Dog(Animal):
    def bark(self):
        print("Bark")

- "Dog" inherits from "Animal"
- So it can use both "sound()" and "bark()"

---

🔗 3. Multiple Inheritance

Definition:

One child class inherits from multiple parent classes.

Code:

class A:
    def one(self):
        print("One")

class B:
    def two(self):
        print("Two")

class C(A, B):
    def three(self):
        print("Three")

- Class "C" inherits from both "A" and "B"
- It can access methods from both classes

---

🪜 4. Multilevel Inheritance

Definition:

A class inherits from a class, which itself inherits from another class.

Code:

class X:
    def a(self):
        print("A")

class Y(X):
    def b(self):
        print("B")

class Z(Y):
    def c(self):
        print("C")

- "Z" → "Y" → "X"
- Object of "Z" can access all methods

---

🌳 5. Hierarchical Inheritance

Definition:

Multiple child classes inherit from the same parent class.

Code:

class P:
    def show(self):
        print("Parent")

class Q(P):
    def one(self):
        print("Child1")

class R(P):
    def two(self):
        print("Child2")

- Both "Q" and "R" inherit from "P"

---

🔄 6. Polymorphism

Definition:

Same method name behaves differently for different classes.

Code:

class Add:
    def calc(self):
        print("Add:", 2 + 3)

class Mul:
    def calc(self):
        print("Mul:", 2 * 3)

- Both classes have "calc()" method
- But they perform different operations

---

▶️ How to Run the Program

1. Install Python (if not already installed)
2. Save the code in a file (e.g., "oop_program.py")
3. Run using:

python oop_program.py

---

🎯 Output

The program will print outputs for each concept like:

- Value display
- Animal sounds
- Numbers from inheritance examples
- Addition and multiplication results

---

📚 Conclusion

This program helps beginners understand:

- Classes and Objects
- Types of Inheritance
- Polymorphism

It is a good starting point for learning OOP in Python.

---
