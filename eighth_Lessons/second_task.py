

class Books:
    def __init__(self, author, book_name, publishing_year, book_genre, comments):
        self.author = author
        self.book_name = book_name
        self.publishing_year = publishing_year
        self.book_genre = book_genre
        self.comments = comments

    def __str__(self):

        return f'\nAuthor: {self.author} \nBook name: {self.book_name} \nThe year of publishing: ' \
               f'{self.publishing_year}\nBook genre: {self.book_genre}{self.comments}'


class Comments:
    def __init__(self, comments_name, body_comments):
        self.comments_name = comments_name
        self.body_comments = body_comments

    def __str__(self):
        return f"\nAuthor comments: {self.comments_name}\nComments: {self.body_comments}"


bob_comments = Comments("Fred", "Very interesting book.")
lion_comments = Comments("Jon", "Very hard book for understanding.")

bob_Book = Books('Bob', "Bob's history", 2000, 'History', bob_comments)
lion_Book = Books('Alfred', 'Interesting history about Lion', 1992, 'Drama', lion_comments)

print(bob_Book)
print(lion_Book)


