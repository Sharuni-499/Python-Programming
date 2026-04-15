🔥 REGULAR EXPRESSIONS (REGEX) IN PYTHON – BEGINNER README 🔥

📌 Overview

This program demonstrates basic usage of Regular Expressions (regex) in Python using the "re" module. It covers pattern matching, searching, extracting, replacing, and validating data like dates.

---

🔤 1. Importing Regex Module

import re

- "re" is Python’s built-in module for working with regular expressions.

---

⌨️ 2. User Input

date = input("Enter date (DD/MM/YY): ")

- Takes a date input from the user in "DD/MM/YY" format.

---

🧾 3. Sample Data

text = "brown fox jumps over brown hill"
key = "id1234"
word = "brown"

- "text": Sample sentence
- "key": Used for validation
- "word": Word to search in text

---

✅ 4. Match Function

res = re.match("id", key)

- Checks if the string starts with "id"
- If yes → Valid key

---

🔍 5. Search Function

res = re.search(word, text)

- Searches for ""brown"" anywhere in the text
- Returns first occurrence

---

📋 6. Find All

res = re.findall(word, text)

- Finds all occurrences of ""brown""
- Returns a list

---

🔄 7. Replace (Substitution)

new = re.sub("fox", "dog", text)

- Replaces ""fox"" with ""dog""

---

🔢 8. Extract Numbers

nums = re.findall("[0-9]+", key)

- "[0-9]+" → finds one or more digits
- Extracts numbers from ""id1234""

---

📅 9. Date Validation

pattern = r"\d{2}/\d{2}/\d{2}$"
check = re.match(pattern, date)

Pattern Explanation:

- "\d{2}" → exactly 2 digits
- "/" → slash
- "$" → end of string

✔ Valid Example: "12/05/24"
❌ Invalid Example: "123/5/2024"

---

▶️ How to Run

1. Save file as "regex_program.py"
2. Run using:

python regex_program.py

---

🎯 Output Includes:

- Key validation result
- Word search results
- List of matches
- Modified string
- Extracted numbers
- Date validation

---

📚 Conclusion

This program helps you understand:

- Pattern matching ("match")
- Searching ("search")
- Extracting ("findall")
- Replacing ("sub")
- Input validation using regex

A great beginner step into text processing in Python 🚀

---
