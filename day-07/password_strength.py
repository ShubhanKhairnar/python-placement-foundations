def check_password(password):
    if len(password) < 8:
        return "Weak"
    elif len(password) <= 10:
        return "Moderate"
    else:
        return "Strong"

password = input("Enter your password: ")
strength = check_password(password)

print(f"Your password strength is: {strength}")

