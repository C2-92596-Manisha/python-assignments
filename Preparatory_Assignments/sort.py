# Q10: Sorting student names
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

names.sort()
print("Sorted names:")
for n in names:
    print(n)
