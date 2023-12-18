from tkinter import *
from calc_62 import Calculator

if __name__ == '__main__':
    root = Tk()
    root.title("Mihai's Calculator + Codemy GUI")
    text_box = Entry(root, width=35, borderwidth=5)
    text_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

    calc = Calculator()

    def clear_text_box():
        text_box.delete(0, END)

    def add_number(number):
        current_text = text_box.get()
        clear_text_box()
        text_box.insert(0, str(current_text) + str(number))

    # This function will store the symbol for the calculation corresponding to the button pressed (+, -, *, /)
    def button_calculation(symbol):
        global f_num
        f_num = int(text_box.get())
        global calculation
        calculation = symbol
        clear_text_box()

    # When the equal btn is pressed, the calculator will use the imported "Calculator" class to make the calculation based on the symbol stored
    # by the button_calculation(symbol) function
    def button_equal():
        s_num = int(text_box.get())
        clear_text_box()

        if calculation == "+":
            text_box.insert(0, calc.sum(f_num, s_num))

        if calculation == "-":
            text_box.insert(0, calc.sub(f_num, s_num))

        if calculation == "*":
            text_box.insert(0, calc.multi(f_num, s_num))

        if calculation == "/":
            text_box.insert(0, calc.divide(f_num, s_num))

    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: add_number(1))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: add_number(2))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: add_number(3))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: add_number(4))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: add_number(5))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: add_number(6))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: add_number(7))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: add_number(8))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: add_number(9))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: add_number(0))
    button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_calculation("+"))
    button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
    button_clear = Button(root, text="Clear", padx=79, pady=20, command=clear_text_box)
    button_subtract = Button(root, text="-", padx=41, pady=20, command=lambda: button_calculation("-"))
    button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_calculation("*"))
    button_divide = Button(root, text="/", padx=41, pady=20, command=lambda: button_calculation("/"))

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)

    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)

    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)

    button_0.grid(row=4, column=0)
    button_clear.grid(row=4, column=1, columnspan=2)
    button_add.grid(row=5, column=0)
    button_equal.grid(row=5, column=1, columnspan=2)

    button_subtract.grid(row=6, column=0)
    button_multiply.grid(row=6, column=1)
    button_divide.grid(row=6, column=2)

    root.mainloop()