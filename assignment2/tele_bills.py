#5. Write a program that prompts the user to input number of calls and calculate the monthly telephone.

calls = int(input("Enter number of calls made: "))
bill = 200
if calls <= 100:
    bill = 200
elif calls <= 150:
    bill += (calls - 100) * 0.60
elif calls <= 200:
    bill += (50 * 0.60) + (calls - 150) * 0.50
else:
    bill += (50 * 0.60) + (50 * 0.50) + (calls - 200) * 0.40
print("Monthly telephone bill: Rs.", round(bill, 2))
