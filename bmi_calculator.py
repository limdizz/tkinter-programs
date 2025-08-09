from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Body Mass Index (BMI) Calculator')
root.geometry('460x200')


def calculate_bmi():
    kg = float(weight_form.get())
    m = float(height_form.get())
    bmi = round((kg / (m**2)), 1)

    if bmi < 16.0:
        messagebox.showinfo('Severe thinness',
                            f'BMI {bmi} corresponds to severe thinness')
    elif 16.0 < bmi < 16.9:
        messagebox.showinfo('Moderate thinness',
                            f'BMI {bmi} corresponds to moderate thinness')
    elif 17.0 < bmi < 18.4:
        messagebox.showinfo('Mild thinness',
                            f'BMI {bmi} corresponds to mild thinness')
    elif 18.5 < bmi < 24.9:
        messagebox.showinfo('Normal weight',
                            f'BMI {bmi} corresponds to normal weight')
    elif 25.0 < bmi < 29.9:
        messagebox.showinfo('Overweight', f'BMI {bmi} corresponds to overweight')
    elif 30.0 < bmi < 34.9:
        messagebox.showinfo('Obese (Class I)',
                            f'BMI {bmi} corresponds to obese class I')
    elif 35.0 < bmi < 39.9:
        messagebox.showinfo('Obese (Class II)',
                            f'BMI {bmi} corresponds to obese class II')
    else:
        messagebox.showinfo('Obese (Class III)',
                            f'BMI {bmi} corresponds to obese class III')


frame = Frame(
    root,
    padx=10,
    pady=10,
    bg='grey'
)

height_lbl = Label(
    frame,
    text='Enter your height (m): ',
    font='Times 20',
    width=20,
    bg='black',
    fg='white'
)
height_lbl.grid(row=3, column=1, pady=10)

weight_lbl = Label(
    frame,
    text='Enter your weight (kg): ',
    font='Times 20',
    width=20,
    bg='black',
    fg='white'
)
weight_lbl.grid(row=4, column=1, pady=10)

height_form = Entry(
    frame,
    font='Times 20',
    width=9,
)
height_form.grid(row=3, column=2)

weight_form = Entry(
    frame,
    font='Times 20',
    width=9,
)
weight_form.grid(row=4, column=2, pady=5, padx=5)

call_button = Button(
    frame,
    text='Count BMI',
    font='Impact 20',
    command=calculate_bmi,
    bg='black',
    fg='white'
)
call_button.grid(row=5, column=2)

frame.pack(expand=True)

root.mainloop()
