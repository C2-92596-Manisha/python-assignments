# Q15: Count occurrences of alphabets
text = input("Enter a string: ").lower()
count = {}

for c in text:
    if c.isalpha():
        count[c.upper()] = count.get(c.upper(), 0) + 1

print("Occurrences:")
for k, v in sorted(count.items()):
    print(k, ":", v)
