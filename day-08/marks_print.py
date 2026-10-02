marks = int(input("Enter your marks out of 100: "))

if marks < 0 or marks > 100:
    print("Invalid marks entered. Please enter a value between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

else:
    print("Grade: F")