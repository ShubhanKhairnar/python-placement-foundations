#It should:

#Take a string as a parameter.
#Loop through each character.
#Check whether the character is a vowel (a, e, i, o, u).
#Count the vowels.
#Return the count.
#Take the text input outside the function.
#Print the result outside the function.

def count_vowels(text):
 count = 0
 for character in text:
  
  if character.lower() in "aeiou":
   count += 1

 return count

text = input("Enter a word or sentence: ")
result = count_vowels(text)
print(f"The number of vowels is {result}.")
    