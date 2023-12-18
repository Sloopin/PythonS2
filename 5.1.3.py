if __name__ == '__main__':

    list_of_names = []

    while True:
        name = input()
        if name == "":
            break
        else:
            list_of_names.append(name)

    print("List of names unsorted:")
    for element in list_of_names:
        print(element)

    print("List of names sorted in descending order:")
    list_of_names = sorted(list_of_names, reverse=True)
    for element in list_of_names:
        print(element)