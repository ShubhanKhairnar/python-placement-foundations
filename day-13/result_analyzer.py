name = input("Enter student's name: ")
subjects = int(input("Enter no of subjects: "))

total = 0

for i in range(subjects):
    while True:
        marks = float(input(f"Enter marks for subject {i + 1}: "))

        if 0 <= marks <= 100:
            break

        print("Invalid marks. Enter a value between 0 and 100.")

    total += marks

percentage = (total / (subjects * 100)) * 100


def calculate_grade(percentage):
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade


grade = calculate_grade(percentage)

if percentage >= 40:
    result = "Pass"
else:
    result = "Fail"

print()
print("========================")
print("     STUDENT RESULT")
print("========================")
print(f"Name: {name}")
print(f"Subjects: {subjects}")
print(f"Total: {total} / {subjects * 100}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Result: {result}")
print("========================")