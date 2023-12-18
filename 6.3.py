class ToDo:

    def __init__(self, initial_todo_list = []):
        self.todo_list = initial_todo_list

    def add_to_list(self, todo):
        self.todo_list.append(todo)

    def item_in_list(self, item):
        if item not in self.todo_list:
            print("Item not in list!")
        else:
            print("Item exists in list!")

    def remove_element(self, thing_to_remove):
        if thing_to_remove not in self.todo_list:
            print("Item not in list!")
        else:
            self.todo_list.remove(thing_to_remove)

    def print_elements(self):
        for item in self.todo_list:
            print(item)

    def return_list(self):
        return self.todo_list


if __name__ == '__main__':
    todo_list = ToDo(["test","test1"])

    todo_list.add_to_list("test2")
    todo_list.print_elements()
    todo_list.item_in_list("test")
    todo_list.remove_element("test")
    todo_list.item_in_list("test")
    print(todo_list.return_list())