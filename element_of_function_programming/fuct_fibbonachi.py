
def even_numbers(function):
    def decorator(*args):
        seq = function(*args)
        return filter(lambda x: x % 2 == 0, seq)
    return decorator


@even_numbers
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


print(list(fib(50)))
