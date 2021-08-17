
def reverse(lst):
    for index in range(len(lst)-1, -1, -1):
        yield lst[index]


for char in reverse('Palamarchuk'):
    print(char)



