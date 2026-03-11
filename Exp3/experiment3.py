line = "I'm sharuni, I like to sing"

print("Lowercase:", line.lower())
print("Uppercase:", line.upper())
print("Title Case:", line.title())
print("Swapcase:", line.swapcase())
print("Capitalize:", line.capitalize())
print("Length:", len(line))

words = line.split(" ")
print("Split:", words)
new_line = line.replace("sing", "draw")
print("Replace:", new_line)
position = line.index("like")
print("Index of 'like':", position)