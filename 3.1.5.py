if __name__ == '__main__':
    num_list = []
    while True:
        num = int(input("Insert number then press enter: "))
        if num == 0:
            break
        else:
            num_list.append(num)

    print(f"The sum of the values are {sum(num_list)}")
    print(f"The average value is {sum(num_list)/len(num_list)}") # sum of values / number of values
    print(f"The minimum value is {min(num_list)}")
    print(f"The maximum value is {max(num_list)}")