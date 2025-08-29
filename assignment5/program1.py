people = {'Arham': 'Blue', 'Lisa': 'Yellow', 'Vinod': 'Purple', 'Jenny': 'Pink'}
print("Total students:", len(people))
people['Lisa'] = 'Green'
del people['Jenny']
for name in sorted(people):
    print(name, ":", people[name])
