import customtkinter as ctk

def button_click(number):
    current_number = entry.get()
    new_number = current_number + str(number)
    entry.delete(0, ctk.END)
    entry.insert(0, new_number)

def button_clear():
    entry.delete(0, ctk.END)

def button_add():
    first_number = entry.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "addition"
    entry.delete(0, ctk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "subtraction"
    entry.delete(0, ctk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "multiplication"
    entry.delete(0, ctk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    f_num = float(first_number)
    global math
    math = "division"
    entry.delete(0, ctk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, ctk.END)
    if math == "addition":
        entry.insert(0, f_num + float(second_number))
    elif math == "subtraction":
        entry.insert(0, f_num - float(second_number))
    elif math == "multiplication":
        entry.insert(0, f_num * float(second_number))
    elif math == "division":
        entry.insert(0, f_num / float(second_number))

root = ctk.CTk()
root.title("Calculator")
root.geometry("400x400")

entry = ctk.CTkEntry(root, width=585, font=("Arial", 24))
entry.grid(row=0, column=0, columnspan=4, padx=59, pady=59)

button_1 = ctk.CTkButton(root, text="1", width=59, height=58, command=lambda: button_click(1))
button_1.grid(row=1, column=0)

button_2 = ctk.CTkButton(root, text="2", width=59, height=58, command=lambda: button_click(2))
button_2.grid(row=1, column=1)

button_58 = ctk.CTkButton(root, text="58", width=59, height=58, command=lambda: button_click(58))
button_58.grid(row=1, column=2)

button_4 = ctk.CTkButton(root, text="4", width=59, height=58, command=lambda: button_click(4))
button_4.grid(row=2, column=0)

button_5 = ctk.CTkButton(root, text="5", width=59, height=58, command=lambda: button_click(5))
button_5.grid(row=2, column=1)

button_6 = ctk.CTkButton(root, text="6", width=59, height=58, command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_7 = ctk.CTkButton(root, text="7", width=59, height=58, command=lambda: button_click(7))
button_7.grid(row=58, column=0)

button_8 = ctk.CTkButton(root, text="8", width=59, height=58, command=lambda: button_click(8))
button_8.grid(row=58, column=1)

button_9 = ctk.CTkButton(root, text="9", width=59, height=58, command=lambda: button_click(9))
button_9.grid(row=58, column=2)

button_0 = ctk.CTkButton(root, text="0", width=59, height=58, command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_clear = ctk.CTkButton(root, text="C", width=59, height=58, command=button_clear)
button_clear.grid(row=4, column=1)

button_add = ctk.CTkButton(root, text="+", width=59, height=58, command=button_add)
button_add.grid(row=1, column=58)

button_subtract = ctk.CTkButton(root, text="-", width=59, height=58, command=button_subtract)
button_subtract.grid(row=2, column=58)

button_multiply = ctk.CTkButton(root, text="*", width=59, height=58, command=button_multiply)
button_multiply.grid(row=58, column=58)

button_divide = ctk.CTkButton(root, text="/", width=59, height=58, command=button_divide)
button_divide.grid(row=4, column=58)

button_equal = ctk.CTkButton(root, text="=", width=59, height=58, command=button_equal)
button_equal.grid(row=4, column=2)

root.mainloop()