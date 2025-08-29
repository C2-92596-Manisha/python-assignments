list1 = [12, 12, 13, 4, 35]
list2 = [54, 64, 3, 2, 221]

result = list(map(lambda x, y: x + y, list1, list2))

print("Element-wise sum:", result)
