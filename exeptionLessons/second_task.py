def addition(first_num, second_num, action):
    result = first_num + second_num
    print(f"{first_num} {action} {second_num} = {result}")


def subtraction(first_num, second_num, action):
    result = first_num - second_num
    print(f"{first_num} {action} {second_num} = {result}")


def multiplication(first_num, second_num, action):
    result = first_num * second_num
    print(f"{first_num} {action} {second_num} = {result}")


def division(first_num, second_num, action):
    result = first_num / second_num
    print(f"{first_num} {action} {second_num} = {result}")


def power(first_num, second_num, action):
    result = first_num ** second_num
    print(f"{first_num} {action} {second_num} = {result}")


def calculator():
    print("Welcome to Calculator!")
    while True:
        try:
            first_num = int(input("Enter first num: "))
            action = input("Choose action (+, -, *, /, **): ")
            second_num = int(input("Enter second num: "))

            if action == "+":
                addition(first_num, second_num, action)
            elif action == "-":
                subtraction(first_num, second_num, action)
            elif action == "*":
                multiplication(first_num, second_num, action)
            elif action == "/":
                division(first_num, second_num, action)
            elif action == "**":
                power(first_num, second_num, action)

        except (ZeroDivisionError, ValueError):
            print(f'You enter incorrect values, try again!')
            return calculator()


calculator()
