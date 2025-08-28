#8. Write a program that prompts the user to input a character and determine the character is vowel or
#consonant.

char = input("Enter a single alphabet character: ").lower()

if char in ['a', 'e', 'i', 'o', 'u']:
    print(char, "is a Vowel")
elif char.isalpha():
    print(char, "is a Consonant")
else:
    print("Invalid input. Please enter an alphabet letter.")
