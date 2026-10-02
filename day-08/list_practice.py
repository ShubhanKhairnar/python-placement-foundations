age = int (input("Enter your age: "))
if age >= 18:
    print("You are eligible.")
else:
    print("You are not eligible.")


#Marksheet

marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
#No need to write the upper limit in the elif stmts cus python checks  the conditions from top to bottom and executes the first true condition it encounters. So if the marks are 85, it will check the first condition (marks >= 90) which is false, then it will check the second condition (marks >= 80) which is true, and it will print "Grade: B" without checking the remaining conditions.


#Login check
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Login failed. Please check your username and password.")
