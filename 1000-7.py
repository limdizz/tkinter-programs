import tkinter as tk
import pygame as pg
from PIL import ImageTk, Image

pg.mixer.init()
pg.mixer.music.load('1000-7/unravel.mp3')
pg.mixer.music.play()

root = tk.Tk()
root['bg'] = 'black'
root.title('1000-7.exe')
root.rowconfigure(0, minsize=250)
root.columnconfigure(1, minsize=250)
root.resizable(width=False, height=False)

img = ImageTk.PhotoImage(Image.open('1000-7/Kaneki.png'))


def decrease():
    value = int(label_value['text'])
    label_value['text'] = f'{value - 7}'
    if value < 7:
        root.destroy()


button_decrease = tk.Button(
    root,
    font='Times 60',
    command=decrease,
    image=img
)
button_decrease.grid(row=0, column=0, sticky='nsew')

text = tk.Label(text='Click Kaneki', bg='black', fg='white', font='Intro')
text.grid(sticky='s')

label_value = tk.Label(root, text='1000', font='Intro 50', bg='black', fg='white')
label_value.grid(row=0, column=1)

root.mainloop()
