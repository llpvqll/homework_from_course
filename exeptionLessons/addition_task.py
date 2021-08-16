
class Main:
    @staticmethod
    def type_exception():
        try:
            enter = int(input('Enter your age: '))
            return f"You are {enter} years old!"
        except ValueError:
            return f"You entered not a number! "


res = Main.type_exception()
print(res)
