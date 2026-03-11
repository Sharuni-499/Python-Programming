def calc(a, b):
    return a + b, a - b, a * b, a / b

a = int(input("Enter a: "))
b = int(input("Enter b: "))

add, sub, mul, div = calc(a, b)

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)