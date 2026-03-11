students = {
    "S101": 85,
    "S102": 92,
    "S103": 78,
    "S104": 88,
    "S105": 91,
    "S106": 79
}

print("\nOriginal Dictionary:", students)

print("Student IDs:", students.keys())

print("Grades:", students.values())

students_copy = students.copy()
print("Copied Dictionary:", students_copy)

students.update({"S107": 95})
print("After Update:", students)

students.pop("S105")
print("After Pop:", students)

del students["S104"]
print("After Delete:", students)

print("Final Dictionary:", students)