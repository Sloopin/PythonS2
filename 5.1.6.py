if __name__ == '__main__':

    original_list = []
    does_it_contain_odd_numbers = True

    values = input("Insert the list of numbers with spaces between them (Ex. 1 2 3): ")
    # We split the elements between spaces in a list and then convert all from string to integer
    original_list = list(map(int, values.split(" ")))

    print("Original list:", original_list)
    
    modified_list = [value for value in original_list if value % 2 == 0]

    print("Modified list:", modified_list)