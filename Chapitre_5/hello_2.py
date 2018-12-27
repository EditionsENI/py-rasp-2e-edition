#!/usr/bin/env python3
import tkinter
from tkinter import Label


def main():
    fenetre = tkinter.Tk()
    fenetre.geometry('300x150')
    label = Label(fenetre, text='Hello world avec tkinter!')
    label.place(x=100, y=70)
    fenetre.mainloop()


if __name__ == '__main__':
    main()
