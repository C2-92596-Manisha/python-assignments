#1. Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube
 #function]

def cube(n):
    return n ** 3
a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))
a3 = int(input("Enter third number: "))
a4= int(input("Enter fourth number: "))
a5= int(input("Enter fifth number: "))
sum_of_cubes = cube(a1) + cube(a2) + cube(a3) + cube(a4) + cube(a5)
print("Sum of cubes:", sum_of_cubes)
