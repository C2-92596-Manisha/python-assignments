# 10. write a function to return compound interest
def compound_interest(P, r, n, t):
    amount = P * (1 + r / n) ** (n * t)
    CI = amount - P
    return CI
principal = float(input("Enter principal amount (P): "))
rate = float(input("Enter annual interest rate (r) in decimal (e.g., 0.05 for 5%): "))
compounds_per_year = int(input("Enter number of times interest compounds per year (n): "))
years = float(input("Enter number of years (t): "))

interest = compound_interest(principal, rate, compounds_per_year, years)

print("Compound Interest is: Rs.", round(interest, 2))
