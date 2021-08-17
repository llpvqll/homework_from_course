
class Reverse:
    def __init__(self, lst):
        self.lst = lst
        self.index = len(lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.lst[self.index]


rev = Reverse('Palamarchuk')

for char in rev:
    print(char)
