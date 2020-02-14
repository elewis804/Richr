from tkinter import *
from getChar import getRandomChar

class Description(Frame):
    def __init__(self, master):
        super(Description, self).__init__(master)
        self.granted = False
        self.grid()
        self.grantButton = None
        self.denyButton = None
        self.resultsLabel = Label(self)
        self.nextButton = Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.resultsLabel.destroy()
        self.nextButton.destroy()
        self.Char = getRandomChar()
        self.nameLabel = Label(self, text=self.Char.cName, font=("Comic Sans MS", 20), fg="black")
        self.nameLabel.grid(row=0, column=0, sticky =N)
        self.descriptionLabel = Text(self, width=33, height=15, wrap=WORD)
        self.descriptionLabel.grid(row=2, column=0, sticky=N)
        self.grantButton = Button(self, text="Grant them the money", font=("Comic Sans MS", 10), fg="black", bg="green",
                                  command=self.grantedResults)
        self.grantButton.grid(row=4, column=0, sticky=E)
        self.denyButton = Button(self, text="No Money for them!", font=("Comic Sans MS", 10), fg="black", bg="Red",
                                 command=self.deniedResults)
        self.denyButton.grid(row=4, column=0, sticky=W)
        self.descriptionLabel.delete(0.0, END)
        self.descriptionLabel.insert(0.0, self.Char.cDesc)

    def grantedResults(self):
        self.granted=True
        self.Results()

    def deniedResults(self):
        self.granted=False
        self.Results()

    def Results(self):
        self.grantButton.destroy()
        self.denyButton.destroy()
        self.nameLabel.destroy()
        self.resultsLabel = Label(self, text="Results:", font=("Comic Sans MS", 20), fg="black")
        self.resultsLabel.grid(row=0, column=0, sticky =N)
        self.nextButton = Button(self, text="Next", font=("Comic Sans MS", 10), bg="red", fg="black",
                                 command=self.create_widgets)
        self.nextButton.grid(row=5, column=0, sticky=N)
        if self.granted:
            self.descriptionLabel.delete(0.0, END)
            self.descriptionLabel.insert(0.0, self.Char.cGrant)
        if not self.granted:
            self.descriptionLabel.delete(0.0, END)
            self.descriptionLabel.insert(0.0, self.Char.cDeny)