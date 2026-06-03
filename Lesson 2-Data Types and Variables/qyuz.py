grade = input("What grade are you in? 10, 11, or 12?").upper()

if grade == "10":
    print("You are in Grade 10.")
elif grade == "11":
    print("You are in Grade 11.")
elif grade == "12":
    print("You are in Grade 12.")
else:
    print("Please enter 10, 11, or 12.")

age = input("How old are you?").upper()

animal = input("What is your favourite animal?").upper()

earth = input("Do you think the Earth is square? YES or NO?").upper()

if earth == "YES":
    print("That's wrong. The Earth is not square.")
elif earth == "NO":
    print("Good job!")
else:
    print("Please answer YES or NO.")

print("----- Summary -----")
print("You are in Grade " + grade + ".")
print("Your age is " + age + ".")
print("Your favourite animal is " + animal + ".")
print("Your answer about the Earth is " + earth + ".")