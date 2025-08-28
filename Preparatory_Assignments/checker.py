# Q5: Character type checker
text = input("Enter text: ")

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())
digits = sum(1 for c in text if c.isdigit())
others = len(text) - (upper+lower+digits)

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digits)
print("Others:", others)
