from tkinter import *

# Setting up a new font and it's size
large_font = ('Verdana', 20)

root = Tk()

# Title and Icon...put the path of your icon in place of (...)
# Always use .ico format of image. PNG format is not supported by Tkinter!
root.title("Calculator")
# root.iconbitmap("(...).ico")

e = Entry(root, width = 30, borderwidth = 5, relief = "solid", font = large_font) 
e.grid(row = 0, column = 0, columnspan = 10, padx = 20, pady = 20)

#e.insert(0, "") ... Used to insert any sentence. The sentence is erasable.
#e.delete(0, END) ... Used for deleting any value recieved by the program.
# relief is a property which is used for giving a texture to the box as well as to the buttons.

# Defining Click button
def button_click(number):
	current = e.get()
	e.delete(0, END)
	e.insert(0, str(current) + str(number))

# Defining Clear button
def button_clear():
	e.delete(0, END)

# Defining (+) button
def button_add():
	first_number = e.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	e.delete(0, END)

# Defining (-) button
def button_subtract():
	first_number = e.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	e.delete(0, END)

# Defining (*) button
def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	e.delete(0, END)

# Defining (/) button
def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	e.delete(0, END)

# Defining functions for (=) button
def button_equal():
	second_number = e.get()
	e.delete(0, END)

	if math == "addition":
		e.insert(0, f_num + int(second_number))

	if math == "subtraction":
		e.insert(0, f_num - int(second_number))

	if math == "multiplication":
		e.insert(0, f_num * int(second_number))

	if math == "division":
		e.insert(0, f_num / int(second_number))

# Defining Buttons

button_1 = Button(root, text = "1", padx = 60, pady = 40, command = lambda: button_click(1), relief = "raised")
button_2 = Button(root, text = "2", padx = 60, pady = 40, command = lambda: button_click(2), relief = "raised")
button_3 = Button(root, text = "3", padx = 60, pady = 40, command = lambda: button_click(3), relief = "raised")
button_4 = Button(root, text = "4", padx = 60, pady = 40, command = lambda: button_click(4), relief = "raised")
button_5 = Button(root, text = "5", padx = 60, pady = 40, command = lambda: button_click(5), relief = "raised")
button_6 = Button(root, text = "6", padx = 60, pady = 40, command = lambda: button_click(6), relief = "raised")
button_7 = Button(root, text = "7", padx = 60, pady = 40, command = lambda: button_click(7), relief = "raised")
button_8 = Button(root, text = "8", padx = 60, pady = 40, command = lambda: button_click(8), relief = "raised")
button_9 = Button(root, text = "9", padx = 60, pady = 40, command = lambda: button_click(9), relief = "raised")
button_0 = Button(root, text = "0", padx = 60, pady = 40, command = lambda: button_click(0), relief = "raised")
button_add = Button(root, text = "+", padx = 60, pady = 40, command = button_add, relief = "flat")
button_equal = Button(root, text = "=", padx = 60, pady = 40, command = button_equal, relief = "flat")
button_clear = Button(root, text = "Clear", padx = 60, pady = 40, command = button_clear, relief = "flat")

button_subtract = Button(root, text = "-", padx = 60, pady = 40, command = button_subtract, relief = "flat")
button_multiply = Button(root, text = "*", padx = 60, pady = 40, command = button_multiply, relief = "flat")
button_divide = Button(root, text = "/", padx = 60, pady = 40, command = button_divide, relief = "flat")

# Put the buttons on the screen

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_add.grid(row = 4, column = 2)
button_clear.grid(row = 1, column = 4, columnspan = 4)
button_equal.grid(row = 4, column = 1)

button_subtract.grid(row = 2, column = 4)
button_multiply.grid(row = 3, column = 4)
button_divide.grid(row = 4, column = 4)

root.mainloop()
