
def average(*numbers):
    res = 0
    for element in numbers:
        res += element
    result = res / len(numbers)
    print(float(result))


def average_v2(*num):
    res_v2 = 0
    for item in range(num[0], num[-1] + 1):
        res_v2 += item
    result_v2 = res_v2 / num[-1]
    print(result_v2)


average_v2(1, 5)
average(1, 2, 3, 4, 5)
