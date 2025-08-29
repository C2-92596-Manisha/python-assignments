
words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
long_words = list(filter(lambda word: len(word) > 5, words))

print("Words with more than 5 characters  = ", long_words)
