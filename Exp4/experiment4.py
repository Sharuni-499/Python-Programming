# List for cricket scores
scores = [102, 45, 78, 12, 56]
print("Original Scores:", scores)


scores.append(89)
print("After append:", scores)


scores.insert(2, 34)
print("After insert:", scores)


scores.extend([67, 23])
print("After extend:", scores)


copy_scores = scores.copy()
print("Copied Scores:", copy_scores)


print("Scores:", scores)


scores.clear()
print("After clear:", scores)
