import tkinter
from timeit import default_timer as timer
import random


def speed_test():
    speed_test_sentences = [
        "So am I still waiting for this world to stop hating",
        "Your tears don't fall, they crash around me",
        "My shadow's the only one that walks beside me",
        "I don't think you trust in my self-righteous suicide",
        "I tear my heart open, I sew myself shut",
        "I've said it once, I've said it twice, I've said it 1000 fucking times",
        "I'm waking up, I feel it in my bones",
        "I should've known the tides were getting higher",
        "Answer me it's all that I'm asking",
        "Trapped in a world where money controls you",
        "I hate that it seemed you were never enough",
        "I had you in my grip, but you're starting to slip",
        "I think I'm gonna let you break me down",
        "Release your grip and face the tide, accepting this damnation",
        "I can see that we may be running out of time",
        "We made our mistakes, it's not too late"
    ]

    sentence = random.choice(speed_test_sentences)
    start = timer()
    root = tkinter.Tk()
    root.configure()
    root.geometry('900x200')
    root.title = 'Speed Typing Test'

    label_1 = tkinter.Label(root, text=sentence, font='times 20', bg='black',
                            fg='white')
    label_1.place(x=180, y=10)

    label_2 = tkinter.Label(root, text='Start Typing:', font='times 10',
                            bg='black', fg='white')
    label_2.place(x=160, y=65)

    entry = tkinter.Entry(root, width=50, bg='black', fg='white', font='times 12')
    entry.place(x=280, y=65)

    def check_result():
        if entry.get() == sentence:
            end = timer()
            label_3.configure(text=f'Time: {round((end - start), 4)}s')
        else:
            label_3.configure(text='Wrong Input')

    button_1 = tkinter.Button(root, text='Done',
                              command=check_result, width=12, bg='black',
                              fg='white')
    button_1.place(x=300, y=120)

    button_2 = tkinter.Button(root, text='Try Again',
                              command=speed_test, width=12, bg='black',
                              fg='white')
    button_2.place(x=470, y=120)

    label_3 = tkinter.Label(root, text='', font='times 20')
    label_3.place(x=100, y=100)

    root.mainloop()


if __name__ == '__main__':
    speed_test()
