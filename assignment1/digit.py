#Q3. 3. Write a program to accept a 4 digit number and
#a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If user enters a 4 digit number 9361

num = int(input("Enter a 4-digit number: "))
num_str = str(num)

print("Face values:")
for digit in num_str:
    print(digit, end=' ')
print()
print("Place values:")
thousands = int(num_str[0]) * 1000
hundreds = int(num_str[1]) * 100
tens = int(num_str[2]) * 10
ones = int(num_str[3]) * 1
print(f"{num} = {thousands} + {hundreds} + {tens} + {ones}")

reversed_num = num_str[::-1]
print("Reversed number:", reversed_num)
