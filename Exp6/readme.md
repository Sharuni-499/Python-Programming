## Experiment Title

Experiment 6

## Aim

To write a program to demonstrate dictionary and related functions in Python.

## Algorithm

1. Initialize a dictionary `students` with student IDs as keys and grades as values.
2. Print the original dictionary.
3. Display all the keys of the dictionary using `keys()`.
4. Display all the values of the dictionary using `values()`.
5. Create a copy of the dictionary using `copy()` and print it.
6. Add a new entry `"S107": 95` to the dictionary using `update()` and display the updated dictionary.
7. Remove the entry with key `"S105"` using `pop()` and print the dictionary.
8. Delete the entry with key `"S104"` using `del` and display the dictionary.
9. Print the final dictionary.

## Output

```text
Original Dictionary: {'S101': 85, 'S102': 92, 'S103': 78, 'S104': 88, 'S105': 91, 'S106': 79}
Student IDs: dict_keys(['S101', 'S102', 'S103', 'S104', 'S105', 'S106'])
Grades: dict_values([85, 92, 78, 88, 91, 79])
Copied Dictionary: {'S101': 85, 'S102': 92, 'S103': 78, 'S104': 88, 'S105': 91, 'S106': 79}
After Update: {'S101': 85, 'S102': 92, 'S103': 78, 'S104': 88, 'S105': 91, 'S106': 79, 'S107': 95}
After Pop: {'S101': 85, 'S102': 92, 'S103': 78, 'S104': 88, 'S106': 79, 'S107': 95}
After Delete: {'S101': 85, 'S102': 92, 'S103': 78, 'S106': 79, 'S107': 95}
Final Dictionary: {'S101': 85, 'S102': 92, 'S103': 78, 'S106': 79, 'S107': 95}
```