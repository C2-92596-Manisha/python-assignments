# 9. write a function to return simple interest.
 
def simple_interest(P, R, T):
    SI = (P * R * T) / 100
    return SI
principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter annual interest rate (R): "))
time = float(input("Enter time in years (T): "))
interest = simple_interest(principal, rate, time)

print("Simple Interest is: Rs.", round(interest, 2))
