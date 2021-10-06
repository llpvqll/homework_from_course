

def main():
    first_str = input("Enter first word: ")
    second_str = input("Enter second word: ")
    print(''.join(set(first_str) & set(second_str)))


if __name__ == '__main__':
    main()
