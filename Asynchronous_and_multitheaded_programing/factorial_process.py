import concurrent.futures


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n-1)


if __name__ == '__main__':
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)

    future_one = executor.submit(factorial, 300)
    future_two = executor.submit(factorial, 500)

    result_one = None
    result_two = None

    try:
        result_one = future_one.result()
        result_two = future_two.result()
    except Exception as ex:
        print("factorial_func:: <main> :: Exception: %s" % ex)

    print("factorial_func:: <main> :: result from future_one = " + str(result_one))
    print("factorial_func:: <main> :: result from future_one = " + str(result_two))

    executor.shutdown()
