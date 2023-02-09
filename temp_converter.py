from tkinter import *

root = Tk()
root.title("Temp converter")
root.columnconfigure(0, minsize=200)
root.rowconfigure([0, 1], minsize=100)
root.resizable(width=False, height=False)


def celcius_to_fahrenheit():
    """Converts a value from degrees Celsius to degrees Fahrenheit"""
    celcius = entry_temperature.get()
    fahrenheit = ((9 / 5) * (float(celcius))) + 32
    label_result['text'] = f'{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}'


frame_entry = Frame(root)
entry_temperature = Entry(frame_entry, width=20)
label_temp = Label(frame_entry, text='\N{DEGREE CELSIUS}', font=50)
button_convert = Button(root, text='\N{RIGHTWARDS BLACK ARROW}',
                        command=celcius_to_fahrenheit, font=50)
label_result = Label(root, text='\N{DEGREE FAHRENHEIT}', font=50)

entry_temperature.grid(row=0, column=0, sticky='e')
label_temp.grid(row=0, column=1, sticky='w')
frame_entry.grid(row=0, column=0, padx=10, pady=10)
button_convert.grid(row=0, column=1, pady=10)
label_result.grid(row=0, column=2, padx=10)


def fahrenheit_to_celcius():
    """Converts a value from degrees Fahrenheit to degrees Celsius"""
    fahrenheit = entry_temperature2.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    label_result2["text"] = f"{round(celsius, 2)} \N{DEGREE FAHRENHEIT}"


frame_entry2 = Frame(root)
entry_temperature2 = Entry(frame_entry2, width=20)
label_temp2 = Label(frame_entry2, text='\N{DEGREE FAHRENHEIT}', font=50)
button_convert2 = Button(root, text='\N{RIGHTWARDS BLACK ARROW}',
                         font=50, command=fahrenheit_to_celcius)
label_result2 = Label(root, text='\N{DEGREE CELSIUS}', font=50)

entry_temperature2.grid(row=0, column=0, sticky='e')
label_temp2.grid(row=0, column=1, sticky='w')
frame_entry2.grid(row=0, column=0, padx=10, sticky='s')
button_convert2.grid(row=0, column=1, sticky='s')
label_result2.grid(row=0, column=2, padx=10, sticky='s')

root.mainloop()
