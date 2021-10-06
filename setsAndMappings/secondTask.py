
def add_links(links):
    original_links = input("Enter url: ")
    short_name = None
    while not short_name or short_name in links:
        short_name = input("Enter short name: ")
        if short_name in links:
            print(f"Short name already exist (url: {links[short_name]})")
    links[short_name] = original_links


def get_links(links):

    name = input("Enter name of link: ")
    url = links.get(name, None)

    if url:
        print(url)
    else:
        print('Link dose not exist!')


def main():

    links = {}

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