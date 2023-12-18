if __name__ == "__main__":
    num = int(input("enter num: ",))

    if num > 0:
        print(f'The number {num} is positive')
    elif num < 0:
        print(f'The number {num} is negative')
    else:
        print(f'The number {num} is zero')