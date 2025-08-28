# Function to filter words longer than given length
def filter_long_words(words, length):
    result = []                     
    for w in words:                 
        if len(w) > length:         
            result.append(w)      
    return result                   
words_list = ["apple", "bat", "elephant", "cat", "sunflower"]
print(filter_long_words(words_list, 3))  
