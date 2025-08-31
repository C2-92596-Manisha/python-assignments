def count_words_in_file(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            words = line.split()   
            count += len(words)
    print("Total number of words:", count)


count_words_in_file("story.txt")
