if __name__ == '__main__':
    letter = input("Insert character: ")
    if letter.isupper():
        print(letter.lower())
    else:
        print(letter.upper())