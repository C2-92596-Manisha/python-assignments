def count_non_c_lines(filename):
    count = 0
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()  
            if line and line[0].isalpha():   
                if not line.startswith("C"):
                    count += 1
    print("Number of lines not starting with 'C':", count)

count_non_c_lines("story.txt")
