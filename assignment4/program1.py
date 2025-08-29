words = ["python", "functional", "programming", "is", "powerful"]

lengths = list(map(len, words))
max_len = max(lengths)

longest_words = list(filter(lambda word: len(word) == max_len, words))

print("Longest word is = ", longest_words)
