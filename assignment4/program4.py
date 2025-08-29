numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

square_odds = list(map(lambda x: x ** 2, odd_numbers))

result = sum(square_odds)
print("Sum of squares of odd numbers:", result)
