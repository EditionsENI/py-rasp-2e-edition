#!/usr/bin/env python3 
import tkinter
from tkinter import Label
from tkinter import Button
from tkinter import YES
from tkinter import BOTH
from tkinter import BOTTOM


def main():
    fenetre = tkinter.Tk()
    fenetre.geometry('300x150')
    label = Label(fenetre, text='Hello world avec tkinter!',
                  fg='red', bg='blue')
    label.pack(expand=YES, fill=BOTH)
    bouton = Button(fenetre, text='Fermer', command=fenetre.quit)
    bouton.pack(side=BOTTOM)
    fenetre.mainloop()


if __name__ == '__main__':
    main()
