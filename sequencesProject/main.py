
# 31 28 31 30 31 30 31
# 31 30 31 30 31

def get_month_day(month_index: int) -> int:
    return 30 + int(month_index % 7 % 2 == 0) - int(month_index == 1) * 2


for index in range(12):
    print(f"{index + 1} : {get_month_day(index)}")