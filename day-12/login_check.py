login = "admin"
password = 1234
user_login = input("Enter your login: ")
user_password = int(input("Enter your password: "))

if user_login == login and user_password == password:
    print("Login successful!")
else:
    print("Invalid login or password. Please try again.")

