# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


def century():
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    current_year = 2025
    year_at_100_y_o = current_year + 100 - user_age

    print(f"Hello {user_name}, you will be 100 years old in the year {year_at_100_y_o}")


century()


# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Add a response, when the number is divisible by 4


def odd_even():
    user_input = input("Please, input a number: ")
    user_input = int(user_input)

    if user_input % 2 == 0 and user_input % 4 != 0:
        print(f"The number {user_input} is even.")
    elif user_input % 2 == 0 and user_input % 4 == 0:
        print(f"The number {user_input} is even and is divisible by 4.")
    else:
        print(f"The number {user_input} is odd.")


odd_even()
