
def value_changer(int_list: list[int]) -> list[str]:
    str_list = []
    for item in int_list:
        item = str(item)
        str_list.append(item)
    print(str_list)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List before function: \n{lst}")
print()
print(f"List after function: ")
value_changer(lst)


