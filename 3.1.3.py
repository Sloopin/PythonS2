if __name__ == '__main__':
    while True:
        value = input("Insert value: ")
        if value == "Q" or value == "q":
            break
        num = int(value)

        if num > 0:
            print(f'The number {num} is positive')
        elif num < 0:
            print(f'The number {num} is negative')
        else:
            print(f'The number {num} is zero')