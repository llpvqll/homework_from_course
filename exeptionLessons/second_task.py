
class Calculator:
    def __init__(self):
        while True:
            print("Welcome to Calculator!")
            try:
                first_num = int(input("Enter first num: "))
                action = input("Choose action (+, -, *, /, **): ")
                second_num = int(input("Enter second num: "))

                def condition(a):
                    if a == "+":
                        return addition()
                    elif a == "-":
                        return subtraction()
                    elif a == "*":
                        return multiplication()
                    elif a == "/":
                        return division()
                    elif a == "**":
                        return power()

                def addition():
                    result = first_num + second_num
                    print(f"{first_num} {action} {second_num} = {result}")

                def subtraction():
                    result = first_num - second_num
                    print(f"{first_num} {action} {second_num} = {result}")

                def multiplication():
                    result = first_num * second_num
                    print(f"{first_num} {action} {second_num} = {result}")

                def division():
                    result = first_num / second_num
                    print(f"{first_num} {action} {second_num} = {result}")

                def power():
                    result = first_num ** second_num
                    print(f"{first_num} {action} {second_num} = {result}")

                condition(action)

            except (ZeroDivisionError, ValueError, UnboundLocalError):
                print(f'You enter incorrect values, try again!')
                return Calculator()


calc = Calculator()
print(calc)

