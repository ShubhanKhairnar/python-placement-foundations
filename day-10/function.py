def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"
result = check_age(23)
print(result)
