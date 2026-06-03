# Create a roller coaster access screener (determine if the user is allowed to ride)
# Rules:    They must be over 150cm and over 10 years old
#           They must not have a heart condition
#           OR they can ride if they have a VIP pass

# Get input

"""
tall = input('How tall are you? ')
age = input('How old are you? ')
role = input('What is your level? ')
heart = input('Do you have heart disease? ')
if tall > 150 and age > 10 or role == "VIP":
    print("Welcome!")
else:
    print("Sorry, you cannot ride.")
"""
tall = int(input('How tall are you? '))
age = int(input('How old are you? '))
role = input('What is your level? ').upper()
heart = input('Do you have heart disease? ').lower()

if (tall > 150 and age > 10 and heart == "no") or role == "VIP":
    print("Welcome!")
else:
    print("Sorry, you cannot ride.")


# Check conditions and output verdict




# ------------------------------
# EXTENSION
# Change your screener to work for 3 different rides (ask user which ride at the beginning) with different rules

# ------------------------------
# EXPERT
# Follow the same task (with extension), but use dictionaries to make the code more efficient   