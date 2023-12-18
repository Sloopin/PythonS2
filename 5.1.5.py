if __name__ == '__main__':

    nr = int(input("Insert number: "))
    i = 0

    while True:
        square_value = i ** 2
        if square_value > nr:
            break
        else:
            print(square_value)
        i += 1