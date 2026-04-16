import re

date = input("Enter date (DD/MM/YY): ")

text = "brown fox jumps over brown hill"
key = "id1234"

word = "brown"

# match
res = re.match("id", key)
if res:
    print("Key is valid")
else:
    print("Invalid key")

# search
res = re.search(word, text)
if res:
    print("Text valid (case 1)")
else:
    print("Text invalid")

# findall
res = re.findall(word, text)
if res:
    print("Text valid (case 2)")
else:
    print("Invalid text")

# replace
new = re.sub("fox", "dog", text)
print(new)

# extract numbers
nums = re.findall("[0-9]+", key)
print(nums)

# date validation
pattern = r"\d{2}/\d{2}/\d{2}$"
check = re.match(pattern, date)

if check:
    print("Valid date")
else:
    print("Invalid date")

