from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk()
root.title('Calculator')

button_list = [
    '1', '2', '3', '+', '-',
    '4', '5', '6', '*', '/',
    '7', '8', '9', '√', 'xⁿ',
    '.', '0', '=', 'π', 'C',
    'Exit'
]

rows = 1
columns = 0
for i in button_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=rows, column=columns)
    columns += 1
    if columns > 4:
        columns = 0
        rows += 1


def calc(key):
    if key == '=':
        str1 = '+-0123456789.*/)('
        if calc_entry.get()[0] not in str1:
            messagebox.showerror("Error!", "You didn't enter the number")
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, '=' + str(result))
        except:
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

    elif key == 'Exit':
        root.after(1, root.destroy)
        sys.exit()


calc_entry = Entry(root, width=75)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
