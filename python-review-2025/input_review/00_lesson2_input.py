# Goal: show how input works, type conversion, and basic math output.

name = input("Whats your name? ")
print(f"Hi {name}! Lets do some math.\n")

# Get two numbers from the user and ask for their name to personalize the experience

nameF = input("Whats your name? ")
food = input("What is your favorite food?")
print(f" Hi {name} lets starting making {food} for later.")
















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings