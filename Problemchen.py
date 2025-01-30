# def sum():
#     user_input = int(input(f"Input the first number: "))
#     user_input_2 = int(input(f"Input the second number: "))
#     result = user_input + user_input_2

#     print(f"The result is {result}")


# sum()

# number1 = 12
# number2 = 34

# print(f"Die Summe beider Zahlen ist = {number1 + number2}")


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mult(x, y):
    return x * y


def div(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"


def calculator():
    userinput = input("Was möchtest du ausrechnen (add/sub/mult/div):")
    x = float(input("Zahl Nummer 1: "))
    y = float(input("Zahl Nummer 2: "))

    if userinput == "add":
        result = add(x, y)

    elif userinput == "sub":
        result = sub(x, y)

    elif userinput == "mult":
        result = mult(x, y)

    elif userinput == "div":
        result = div(x, y)
    else:
        result = "Ungueltige Eingabe ERROR"

        print(f"Das Ergebnis ist {result}")

    calculator()
