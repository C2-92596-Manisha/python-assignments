# replace single element ‘b’ with [1,2,3].
list = ['a','b','c','d','e']
list.pop(1)
print(list)
list[1:1] = [[1,2,3]]
print(list)


list = ['a','b','c','d']
print(list)
list.pop(1)
print(list)
list[1:1] = [1,2,3]
print(list)