class ToDo:

    # We initialise the instanced variable, by default if no list is provided, the list will be empty
    def __init__(self, initial_todo_list):
        self.todo_list = initial_todo_list
    # Add element to the end of the list
    def add_to_list(self, todo):
        self.todo_list.append(todo)
    # Check if item is in list
    def item_in_list(self, item):
        if item not in self.todo_list:
            print("Item not in list!")
        else:
            print("Item exists in list!")
    # Check if item is in list, if not then we print a message, if yes then we remove the element using .remove()
    def remove_element(self, thing_to_remove):
        if thing_to_remove not in self.todo_list:
            print("Item not in list!")
        else:
            self.todo_list.remove(thing_to_remove)
    # We go through every element in the list and print each one
    def print_elements(self):
        for item in self.todo_list:
            print(item)
    # We return the list
    def return_list(self):
        return self.todo_list

class Person:

    def __init__(self, name, initial_todo_list = []):
        self.name = name
        self.myToDoList = ToDo(initial_todo_list)

    def getName(self):
        return self.name

    def setName(self, new_name):
        self.name = new_name

if __name__ == '__main__':
    pers = Person("Vasile",["test","test1"])

    print(pers.getName())
    pers.setName("Vasile Glodici")
    print(pers.getName())
    pers.myToDoList.add_to_list("test2")
    pers.myToDoList.print_elements()
    pers.myToDoList.item_in_list("test")
    pers.myToDoList.remove_element("test")
    pers.myToDoList.item_in_list("test")
    print(pers.myToDoList.return_list())