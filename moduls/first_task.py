
from url_cut import LinksDB


def add_links(links):
    while True:
        original_links = input("Enter url: ")
        short_name = input("Enter name: ")

        try:
            links.set_link(short_name, original_links)
        except(KeyError, ValueError) as error:
            print(error.args[0])
        else:
            break


def get_links(links):

    name = input("Enter name of link: ")

    try:
        url = links.get_link(name)
    except KeyError:
        print("Link does not exists!")
    else:
        print(url)


def main():

    links = LinksDB()

    while True:
        print("1. Add links")
        print("2. Get links")
        print("3. Exit")

        confirm = input('> ')
        if confirm == '1':
            add_links(links)
        elif confirm == '2':
            get_links(links)
        elif confirm == '3':
            break
        else:
            print('Incorrect Input')


if __name__ == '__main__':
    main()

