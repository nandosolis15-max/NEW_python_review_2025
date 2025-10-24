#Part one: For each line of code below, write what type of variable is being stored (string, integer, or float). Write your answer as a comment next to each line of code.

first_name = "Bro" # for example: this is a string
food = "pizza" #string
email = "Bro123@fake.com" #string
age = 25 ##string
quantity = 3 ##string
price = 10.99 #float
gpa = 3.2 #float
distance = 5.5 #float

#Part 2 – Predict the Output

#Without running the code, predict what each line will print:
print(f"Hello {first_name}") # for example: Hello Bro
print(f"You like {food}") # for example: You like pizza
print(f"Your email is: {email}")
print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"The price is ${price}")
print(f"Your GPA is {gpa}")
print(f"You ran {distance} km")


# Part 3 – Fix the Errors

# The following code has two mistakes.
# Find and fix them so it runs correctly.

name = "Bro"
food = "pizza"
print(f"Hello {name}")
print (f"You like {food}")

# Missing quotes and wrong variable name
favorite_food = "pizza"
print(f"You like {favorite_food}")

# Wrong f-string format
age = 17
print(f"You are {age} years old")

# Mismatched parentheses
price = 12.99
print(f"The total price is ${price}")
      

# Variable name spelled incorrectly
name = "Bro"
print(f"Hello {name}")

# Using + instead of commas
name = "Bro"
print(f"Hello {name} ")

# Mixing single and double quotes incorrectly
email = "Bro123@fake.com"
print(f"Your email is: {email}")

# Forgot to include the f before the string
age = 21
print(f"You are {age} years old")

# Trying to use a number as a variable
cool = "yes"
print(f"Am I cool? {cool}")

#rules for variable names state that they
#cannot be numbers
#another rule is that variable names cannot have spaces
#another rule is that variable names
#cannot have special characters like @!$ etc.
#cannot use reserved key words like class, def, etc.

# Missing curly braces
quantity = 3
print(f"You are buying {quantity} items")

# Using a reserved keyword
class_4 = "ECS"
print(f"You are in {class_4}")


# Part 4 – Create Your Own

# Write a short Python program that:

# Creates at least three variables (a string, an integer, and a float)

# Prints a formatted message using f-strings that combines all three.
#  Example:
movie = "Inception"
rating = 9.5
year = 2010
print(f"My favorite movie is {movie}, released in {year}, rated {rating}/10!")


pet = "coco"
paws = 4
food= "treats"
print(f"My dog's name is {pet} and she has {paws} paws. Her favorite food are {food}")