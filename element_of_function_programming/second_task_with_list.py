
def squares_of_odd_numbers(list_of_num):
    filtered_list = []
    for item in list_of_num:
        if item % 2 != 0:
            item *= item
            filtered_list.append(item)
    return filtered_list


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = squares_of_odd_numbers(some_list)
print(res)
