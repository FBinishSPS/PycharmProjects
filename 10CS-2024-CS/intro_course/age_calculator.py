    # Get the user to input their name
    # Get the user to input their birth year
    # Calculate the user's age
    # Expected output: "Hi NAME, you are 15 years old." as an F-string
    # Test the program with your own name and birth year

import os
repeat = "yes"
while repeat == "yes":
    name = input("Enter your name: ").strip()
    birth_year = int(input("Enter your birth year: ").strip())
    birthday = input("Have you had your birthday this year? (Yes/No): ").lower().strip()

    age = 2024 - birth_year

    if birthday == "no":
        age -= 1

    print(f"Hi {name}, you are {age} years old.")

    repeat = input("Would you like to run the program again? (Yes/No): ").lower().strip()
    os.system('cls||clear')

print("Thank you for using the age calculator.")
