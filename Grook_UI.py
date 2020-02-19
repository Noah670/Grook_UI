# some basic UI demo using Tkinter

from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to Grook\'s epic house")

# You have to meet Grook first


my_label = Label(window, text='Yo what\'s up?', padx=5,
                 pady=5, font=("Helvetica", 25))

my_label.grid(column=0, row=0)

# set window size
window.geometry('640x360')


def get_clicked():
    my_label.configure(text="Bruh what are you doing??")


def click_again():
    my_label.configure(fg='red', text="Bro I told to you to stop cut it out")

# modify the label to the text entered by the user


def enter_text():
    display_text = enter_text.get()
    my_label.configure(text=display_text)

    messagebox.showinfo('Warning', 'Why did you do that?')


# buttons
my_button = Button(window, text="Poke", bg='pink',
                   fg='red', command=get_clicked)
my_button.grid(column=1, row=1)
second_button = Button(window, text="Tap", bg='green',
                       fg='black', command=click_again)
second_button.grid(column=2, row=1)

enter_button = Button(window, text="Enter", command=enter_text)
enter_button.grid(column=4, row=1)


# text box

enter_text = Entry(window, width=10)
enter_text.grid(column=0, row=1)


window.mainloop()
