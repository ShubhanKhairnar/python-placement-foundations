name= input ("Enter your name: ")
print ("Hello " + name + "!")

#f allows variable to be used in the string
name= input ("Enter your name: ").strip().title()
print(f"hello {name}!")

#new way of doing it
age= int (input ("Enter your age:"))
print(f"You are {age} yrs old")

#old way of doing it
age= int (input ("Enter your age:"))
print("You are "+ str(age) + "yrs old")

#f prefix tells Python: "This string contains variables or math expressions inside curly 
# braces {} that need to be evaluated and inserted.
#The .2f is a formatting rule used inside an f-string 
# to control how floating-point numbers (decimals) are displayed.

