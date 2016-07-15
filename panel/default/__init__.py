import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class Panel:
    def __init__(self, master):
        self.master = master
        self.master.minsize(width=300, height=70)
        self.master.maxsize(width=300, height=70)
        master.title("Admin Panel | SeyyedMohammad Hosseini")

        self.message = "Welcome To Panel"

        self.up = Button(master, text=" Up ", command=self.forwardBtn)
        self.down = Button(master, text="Down", command=self.backwardBtn)
        self.right = Button(master, text="Right", command=self.rightBtn)
        self.left = Button(master, text="Left", command=self.leftBtn)

        self.up.grid(row=5, column=3,sticky=W+E)
        self.down.grid(row=20, column=3,sticky=W+E)
        self.right.grid(row=15, column=4,sticky=W+E)
        self.left.grid(row=15, column=2,sticky=W+E)
        pass

    def forwardBtn(self):
        print "Up"
        pass;

    def backwardBtn(self):
        print "backward"
        pass

    def rightBtn(self):
        print "Right"
        pass

    def leftBtn(self):
        print "Left"
        pass

class controller:
    def __init__(self, action):
        self.timer = action.get("timer")
        self.config = action.get("config")
        root = Tk()
        root.geometry("170x200+30+30")
        Panel(root)
        root.mainloop()
