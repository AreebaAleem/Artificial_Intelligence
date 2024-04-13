marks = int(input("Enter marks: "))

if marks < 50:
    grade = "F"
elif marks <= 60:
    grade = "E"
elif marks <= 70:
    grade = "D"
elif marks <= 80:
    grade = "C"
elif marks <= 90:
    grade = "B"
else:
    grade = "A"

print(f"Grade is: {grade}")
