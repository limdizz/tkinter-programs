import math
import sys
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Calculator')

all_buttons = []
all_labels = []

button_list_numbers = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '.', '0', '=',
    'π', 'e', 'n!',
    'EXIT', 'BLACK', 'WHITE'
]

button_list_ops = [
    'C', '⌫', '±',
    '(', ')',
    '*', '+',
    '-', '/', '√',
    'sin', 'cos', 'xⁿ',
    'tg', 'ctg', '1/x', 'log₂', 'lg'
]

calc_entry = Entry(root, width=75)
calc_entry.grid(row=0, column=0, columnspan=5)
all_labels.append(calc_entry)


def make_cmd(key):
    def command(): calc(key)
    return command


rows = 1
columns = 0
for i in button_list_numbers:
    cmd = make_cmd(i)
    btn = Button(text=i, bg='#FFF', command=cmd, width=12, font='Times 12')
    btn.grid(row=rows, column=columns)
    all_buttons.append(btn)
    columns += 1
    if columns > 2:
        columns = 0
        rows += 1

rows = 1
columns = 3
for i in button_list_ops:
    cmd = make_cmd(i)
    btn = Button(text=i, bg='#FFF', command=cmd, width=12, font='Rockwell 12')
    btn.grid(row=rows, column=columns)
    all_buttons.append(btn)
    columns += 1
    if columns > 5:
        columns = 3
        rows += 1


def change_theme(bg_color, fg_color):
    root.configure(bg=bg_color)
    for btn in all_buttons:
        btn.config(bg=bg_color, fg=fg_color)
    for label in all_labels:
        label.config(bg=bg_color, fg=fg_color)


def calc(key):
    if key == '=':
        str1 = '+-0123456789.*/)('
        if calc_entry.get()[0] not in str1:
            messagebox.showerror("Error!", "You didn't enter the number")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except IndexError:
            messagebox.showerror('Error!', 'Check the correctness of data.')

    for n in '1234567890':
        if key == n:
            calc_entry.insert(END, n)

    if key == 'C':
        calc_entry.delete(0, END)
    elif key == '+':
        calc_entry.insert(END, '+')
    elif key == '-':
        calc_entry.insert(END, '-')
    elif key == '*':
        calc_entry.insert(END, '*')
    elif key == '/':
        calc_entry.insert(END, '/')
    elif key == '(':
        calc_entry.insert(END, '(')
    elif key == ')':
        calc_entry.insert(END, ')')
    elif key == '.':
        calc_entry.insert(END, '.')

    elif key == '√':
        calc_entry.insert(END, '=' + str(math.sqrt(int(calc_entry.get()))))
    elif key == 'xⁿ':
        calc_entry.insert(END, '**')
    elif key == 'π':
        calc_entry.insert(END, str(math.pi))

    elif key == 'BLACK':
        change_theme('black', 'white')
    elif key == 'WHITE':
        change_theme('white', 'black')

    elif key == 'Exit':
        root.after(1, root.destroy)
        sys.exit()


root.mainloop()
