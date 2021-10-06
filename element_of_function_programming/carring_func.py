
def outer_multiply(x):
    def inner_multiply(y):
        return x * y

    return inner_multiply


def currying_multiply(function, num1, num2):
    def inner_currying_multiply(num2):
        return function(num1 * num2)

    return inner_currying_multiply(num2)


def outer_currying_multiply_function(function, num1):
    def inner_currying_multiply_num2(num2):
        return function(num1 * num2)

    return inner_currying_multiply_num2

# Вызов outer_multiply


first = outer_multiply(2)
print(first(3))

# Вызов currying_multiply

my_multiply = currying_multiply(print, 2, 2)

# Вывод outer_currying_multiply_function

my_multiply1 = outer_currying_multiply_function(print, 2)
my_multiply1(2)

