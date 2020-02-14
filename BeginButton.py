from tkinter import *


class Start(Frame):
    def __init__(self, master, closeFile, creditScreen):
        super(Start, self).__init__(master)
        self.grid()
        self.closeFile = closeFile
        self.creditScreen = creditScreen
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="$ RICHR $", font=("Comic Sans MS", 32), fg="Green").grid(row=1, column=0, sticky=N)
        self.sumText = Text(self, width=50, height=10, wrap=WORD)
        self.sumText.grid(row=2, column=0, sticky=W)
        introText = "Have you ever wanted to be a cosmic deity capable of granting an unimaginable fortune to anyone?" \
                    " Now you can be a cosmic deity capable of granting an unimaginable fortune to anyone, with the " \
                    "click " \
                    "of a button!"
        self.sumText.insert(0.0, introText)
        self.BeginButton = Button(self, text="Begin", font=("Comic Sans MS", 20), fg="black", bg="Red",
                                  command=self.buttonClicked)
        self.BeginButton.grid(row=4, column=0, sticky=N)
        self.CreditButton = Button(self, text="Credits", font=("Comic Sans MS", 20), fg="black", bg="yellow",
                                   command=self.creditButton)
        self.CreditButton.grid(row=5, column=0, sticky=N)

    def buttonClicked(self):
        self.closeFile()

    def creditButton(self):
        self.creditScreen()
