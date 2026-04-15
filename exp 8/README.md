
Experiment 8

Aim

To write a program to demonstrate regular expression operations in Python (match, search, findall, sub) and validate a date pattern.

Algorithm

1. Import the re module.
2. Read date input in the format DD/MM/YY.
3. Initialize sample string text = "brown fox jumps over brown hill" and key = "id1234".
4. Use re.match() to check whether key starts with "id".
5. Use re.search() to check whether text contains "brown".
6. Use re.findall() to find all occurrences of "brown" in text.
7. Use re.sub() to replace "fox" with "dog" in text.
8. Extract numbers from key using re.findall("[0-9]+", key).
9. Validate date using the regex pattern \d{2}/\d{2}/\d{2}$ with re.match().
10. Print results for each step.

Output

```
Enter date (DD/MM/YY): 15/04/26
Key is valid
Text valid (case 1)
Text valid (case 2)
brown dog jumps over brown hill
['1234']
Valid date
