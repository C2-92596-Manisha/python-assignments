# Q13: Duplicate strings
arr = ["apple", "banana", "apple", "cherry", "banana", "grapes"]

print("Duplicate strings are:")
seen = set()
for word in arr:
    if arr.count(word) > 1 and word not in seen:
        print(word)
        seen.add(word)
