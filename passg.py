import random
import string

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

print("=====================================")
print("Welcome to the password Generator!")
print("=====================================")

length_password = int(input(f"Set length for password:\n"))

nr_letters = int(input(f"How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

checkLong = nr_letters + nr_numbers + nr_symbols

if checkLong > length_password:
    print("ERROR")
    print("Amount of letters, numbers, and symbols is not equal for password length please Try again!")
else:
    allAscii = [letters, numbers, symbols]
    password = ''

    for n in range(0, nr_letters):
        randPositionLetters = random.randint(0, len(allAscii[0]) -1)
        password += allAscii[0][randPositionLetters]

    for n in range(0, nr_numbers):
        randPositionNumbers = random.randint(0, len(allAscii[1]) -1)
        password += allAscii[1][randPositionNumbers]

    for n in range(0, nr_symbols):
        randPositionSymbols = random.randint(0, len(allAscii[2]) -1)
        password += allAscii[2][randPositionSymbols]

    print("Your passwords:")
    print("=====================================")
    print(f"Password before shaked: {password}")
    
    shakedPassword = ''
    password = list(password)
    actual = len(password)
    
    for strpass in range(0, actual):
        randpos = random.randint(0, actual -1)
        shakedPassword += password[randpos]
        password.remove(password[ randpos ])
        actual = len(password)
    
    print(f"Password after shaked: { shakedPassword }")
    print("=====================================")