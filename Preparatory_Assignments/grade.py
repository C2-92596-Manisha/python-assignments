# Q4: Grade calculation
marks = [int(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
total = sum(marks) / 5

if total >= 90:
    grade = "Ex"
elif total >= 80:
    grade = "A"
elif total >= 70:
    grade = "B"
elif total >= 60:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)
