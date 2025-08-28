#6. The marks obtained by a student in 3 different subjects are input by the user. Your program should calc
# ulate the average of subjects and display the grade. 


mark1 = float(input("Enter marks for subject 1: "))
mark2 = float(input("Enter marks for subject 2: "))
mark3 = float(input("Enter marks for subject 3: "))

average = (mark1 + mark2 + mark3) / 3
if average >= 90 and average <= 100:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'
print("Average marks:", round(average, 2))
print("Grade:", grade)
