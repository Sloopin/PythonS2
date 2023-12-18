if __name__ == '__main__':

    list_example = [1,2,2,2,3,1,4,2,3,6,7,9,7,3]

    # Duplicates of a list can easily be removed by converting a list to a dictionary then back to a list
    # The reason why this works is because dictionaries can't have duplicate keys so they automatically get removed

    new_list = mylist = list(dict.fromkeys(list_example))

    print(new_list)