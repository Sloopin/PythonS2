def is_list_empty(list_data):
    # Note: An empty list will be false and a list with stuff in it will be true if checked in an if
    if list_data:
        print("List has stuff in it")
    else:
        print("List is empty")


if __name__ == '__main__':
    empty_list = []
    list_with_stuff = [1,2,3]

    is_list_empty(empty_list)
    is_list_empty(list_with_stuff)