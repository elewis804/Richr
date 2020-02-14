from tkinter import *
from BeginButton import Start
from ChoiceAndDesc import Description
from Credits import Credit


class Manager(object):
    def __init__(self):
        self.root = Tk()
        self.currentScreen = None

    def beginButton(self):
        self.root.title("Start the Game!")
        self.currentScreen = Start(self.root, self.startup_ChoiceAndDesc, self.creditScreen)

    def startup_ChoiceAndDesc(self):
        self.currentScreen.destroy()
        self.root.title = "Do they get wealth or not?"
        self.currentScreen = Description(self.root)

    def creditScreen(self):
        self.currentScreen.destroy()
        self.root.title = "Credits"
        self.currentScreen = Credit(self.root)

def main():
    game = Manager()
    game.beginButton()
    game.root.mainloop()


main()