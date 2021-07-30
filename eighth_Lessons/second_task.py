

class Books:
    def __init__(self, author, book_name, publishing_year, book_genre, comments_list):
        self.author = author
        self.book_name = book_name
        self.publishing_year = publishing_year
        self.book_genre = book_genre
        self.comments_list = comments_list

    def __repr__(self):
        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: {self.publishing_year} \nBook genre: {self.book_genre}\nComments: {self.comments_list}'

    def __str__(self):
        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: {self.publishing_year} \nBook genre: {self.book_genre}\nComments: {self.comments_list}'

    def __eq__(self, other):
        return self.author == other.author and \
               self.book_name == other.book_name and \
               self.publishing_year == other.publishing_year and \
               self.book_genre == other.book_genre

first_Book = Books('Bob', "Bob's history", 2000, 'History', comments_list=["So it's book very interesting but from other hand very difficult"])
second_Book = Books('Alfred', 'Interesting history about Lion', 1992, 'Drama', comments_list=['Very interesting book'])

print(first_Book)
print(second_Book, f"\n")
print(first_Book == second_Book)


