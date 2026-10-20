# Keep words longer than 5 characters and convert them to uppercase.

words = ["apple", "banana", "cat", "orange", "elephant"]

result = [word.upper() for word in words if len(word) > 5]
print ("Original Words: ", words)
print ("Result: ", result)

