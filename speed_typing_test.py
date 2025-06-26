import random
import tkinter
from timeit import default_timer as timer

root = tkinter.Tk()
root.resizable(False, False)
root.geometry('900x200')
root.title('Speed Typing Test')

sentence_label = tkinter.Label(root,
                               font='times 15',
                               )
sentence_label.place(x=300, y=10)

start_typing_label = tkinter.Label(root,
                                   text='Start Typing:',
                                   font='times 12'
                                   )
start_typing_label.place(x=160, y=65)

entry = tkinter.Entry(root,
                      width=50,
                      bg='black',
                      fg='white',
                      font='times 12'
                      )
entry.place(x=280, y=65)

done_button = tkinter.Button(root,
                             text='Done',
                             width=12,
                             bg='black',
                             fg='white'
                             )
done_button.place(x=280, y=120)

try_again_button = tkinter.Button(root,
                                  text='Try Again',
                                  width=12,
                                  bg='black',
                                  fg='white'
                                  )
try_again_button.place(x=590, y=120)

check_result_label = tkinter.Label(root,
                                   font='times 20'
                                   )
check_result_label.place(x=160, y=120)


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

    sentence_label.config(text=sentence)
    entry.delete(0, tkinter.END)
    check_result_label.config(text='')

    def check_result():
        if entry.get() == sentence:
            end = timer()
            check_result_label.configure(text=f'Time: {round((end - start), 4)}s',
                                         font='times 12',
                                         fg='black'
                                         )
        else:
            check_result_label.configure(text='Wrong Input',
                                         font='times 12',
                                         fg='red'
                                         )

    done_button.config(command=check_result)
    try_again_button.config(command=speed_test)


if __name__ == '__main__':
    speed_test()
    root.mainloop()
