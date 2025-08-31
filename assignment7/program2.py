import string

def is_palindrome(phrase):
    phrase = phrase.lower()
    
    cleaned = "".join(char for char in phrase if char.isalnum())
    
    return cleaned == cleaned[::-1]

phrases = [
    "Go hang a salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!"
]

for p in phrases:
    print(f"'{p}' ->", is_palindrome(p))
