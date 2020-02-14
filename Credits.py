from tkinter import *

class Credit(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.createwidgets()

    def createwidgets(self):
        Label(text="Made by Erik Lewis, based off of the game Prayr, by InstCoffee", font=("Comic Sans MS", 25))\
            .grid(row=1, column=0, sticky=N)