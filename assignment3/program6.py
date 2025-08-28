num = input("Enter numbers separated by space: ")

numbers = [int(x) for x in num.split()]

largest = numbers[0]

for n in numbers:
    if n > largest:       
        largest = n       
print("Largest number is:", largest)
