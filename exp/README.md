Experiment 7

Aim

To write a program to demonstrate Object-Oriented Programming concepts in Python including Class & Object, Single Inheritance, Multiple Inheritance, Multilevel Inheritance, Hierarchical Inheritance, and Polymorphism.

Algorithm

1. Class & Object: Define a class Box with a class variable val = 10 and method show(). Create an object and call the method.
2. Single Inheritance: Define parent class Animal with method sound() and child class Dog inheriting Animal with method bark(). Create object and call both methods.
3. Multiple Inheritance: Define classes A and B with methods one() and two(). Define class C(A, B) with method three(). Create object and call all methods.
4. Multilevel Inheritance: Define classes X → Y → Z where each inherits from the previous. Create object of Z and call all methods.
5. Hierarchical Inheritance: Define parent class P and two child classes Q and R inheriting from P. Create objects of both children and call parent and respective child methods.
6. Polymorphism: Define two classes Add and Mul each with a method calc() performing different operations. Create objects and call the method to demonstrate method overriding.
7. Print results for each concept.

Output

```
CLASS & OBJECT
Value: 10

SINGLE INHERITANCE
Sound
Bark

MULTIPLE INHERITANCE
One
Two
Three

MULTILEVEL INHERITANCE
A
B
C

HIERARCHICAL INHERITANCE
Parent
Child1
Parent
Child2

POLYMORPHISM
Add: 5
Mul: 6

