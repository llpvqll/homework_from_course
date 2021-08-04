bob_lst = []
lion_lst = []


class Books:
    def __init__(self, author, book_name, publishing_year, book_genre, comments):
        self.author = author
        self.book_name = book_name
        self.publishing_year = publishing_year
        self.book_genre = book_genre
        self.comments = comments

    def __str__(self):

        comments_list = ["History about Lion very hard for reading", "Bob's history, very interesting book",
                         "Bob is my favourite author", "History about Lion thousands book in my collection"]
        for item in comments_list:
            if "Bob" in item:
                bob_lst.append(item)

        if "Lion" in item:
            lion_lst.append(item)

        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: ' \
               f'{self.publishing_year}\nBook genre: {self.book_genre}\nComments: {self.comments}'


bob_Book = Books('Bob', "Bob's history", 2000, 'History', bob_lst)
lion_Book = Books('Alfred', 'Interesting history about Lion', 1992, 'Drama', lion_lst)

print(bob_Book)
print(lion_Book)


