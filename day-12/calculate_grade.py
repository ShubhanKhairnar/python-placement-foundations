def calculate_grade(marks):
    if marks > 100 or marks < 0:
        return "Invalid marks. Please enter a value between 0 and 100."
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"
marks = int(input("Enter your marks (0-100): "))
result = calculate_grade(marks)
print(f"Your grade is: {result}")