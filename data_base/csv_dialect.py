import csv

FILENAME = 'dialect_example.csv'


class TestDialect(csv.Dialect):
    # creating dialect
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "!"
    lineterminator = '\n'


csv.register_dialect('tester', TestDialect)

with open(FILENAME, 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, dialect='tester')
    writer.writerow(('a', 'b', 'c'))
    writer.writerow(('d', 'e', 'f'))
    writer.writerow(('g', 'h', 'i'))
    writer.writerow(('j', 'k', 'l'))
    writer.writerow(('m', 'n', 'o'))

