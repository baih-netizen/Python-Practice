"""
print("hello")
print(5 == 5.0)
print('hello' != 'hi')
print('hello' == 'hi')
print(5 == '5')
print(5 + 5 >= 10)
print(5 + 5 >= 8)
"""

guess = input('What’s the password?')
print('Checking password is a match…')
while guess != 'secret':
    guess = input('Try again')
    print('Checking password is a match…')
input('Welcome!')

