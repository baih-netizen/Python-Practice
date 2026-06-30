# Set the score to 0
score = 0

# Ask the user for their grade and clean the input
year = input("What year are you in? 10, 11, or 12? ").strip()

# Ask the user's grade
while year != "10" and year != "11" and year != "12":
    year = input("Please enter 10, 11, or 12: ").strip()

print("You are in Year " + year + ".")

# Ask for their age
while True:
    age = input("How old are you? ").strip()

    if age.isdigit():
        age = int(age)
        break
    else:
        print("Please enter numbers only.")
# Ask the for their favourite animal
animal = input("What is your favourite animal? ").strip()

print("\nNow starting the quiz!")
print("----------------------------- <^> -----------------------------")


# Question 1
# Ask a YES or NO question
answer = input("|1. Is the Earth square? YES or NO?                           |").strip().upper()

# Asking until the user enters YES or NO
while answer != "YES" and answer != "NO":
    answer = input("|Please answer YES or NO:                                     |").strip().upper()

# Check the answer and give feedback
if answer == "NO":
    print("|Correct! The Earth is not square.                            |")
    score = score + 1
else:
    print("|Incorrect. The Earth is not square.                          |")


# Question 2
answer = input("|2. Is Python a programming language? YES or NO?              |").strip().upper()

while answer != "YES" and answer != "NO":
    answer = input("|Please answer YES or NO:                                     |").strip().upper()

if answer == "YES":
    print("|Correct! Python is a programming language.                   |")
    score = score + 1
else:
    print("|Incorrect. Python is a programming language.                 |")


# Question 3
answer = input("|3. Do humans need oxygen to live? YES or NO?                 |").strip().upper()

while answer != "YES" and answer != "NO":
    answer = input("|Please answer YES or NO:                                     |").strip().upper()

if answer == "YES":
    print("|Correct! Humans need oxygen to live.                         |")
    score = score + 1
else:
    print("|Incorrect. Humans need oxygen to live.                       |")


# Question 4
answer = input("|4. Is 10 greater than 20? YES or NO?                         |").strip().upper()

while answer != "YES" and answer != "NO":
    answer = input("|Please answer YES or NO:                                     |").strip().upper()

if answer == "NO":
    print("|Correct! 10 is not greater than 20.                          |")
    score = score + 1
else:
    print("|Incorrect. 10 is not greater than 20.                        |")


# Question 5
answer = input("|5. Is water usually a liquid at room temperature? YES or NO? |").strip().upper()

while answer != "YES" and answer != "NO":
    answer = input("|Please answer YES or NO:                                     |").strip().upper()

if answer == "YES":
    print("|Correct! Water is usually a liquid at room temperature.      |")
    score = score + 1
else:
    print("|Incorrect. Water is usually a liquid at room temperature.    |")

print("----------------------------- <V> -----------------------------")
# Display information and score
print("You are in Grade " + year + ".")
print("Your age is " + age + ".")
print("Your favourite animal is " + animal + ".")
print("Your final score is " + str(score) + " out of 5.")