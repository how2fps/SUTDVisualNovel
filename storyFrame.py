import warnings
from tkinter import *

import helperFunctions

warnings.filterwarnings('ignore')

root = Tk()


def run(window):

       mainFrame = Frame(window)
       mainFrame.pack()
       
       backgroundFrame = Frame(window, highlightbackground="blue", highlightthickness=3)
       backgroundFrame.pack()

       chatboxFrame = Frame(window, highlightbackground="red", highlightthickness=3, padx=50,pady=50, background="#d1aa73")
       chatboxFrame.pack(side="bottom", fill="x")

       text = Label(chatboxFrame, text="cool text for cool visual novel", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       # text.insert(INSERT, 'cool text for cool visual novel')
       text.pack(side=LEFT)
       button1 = Button(chatboxFrame, text='Hello', borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       button1.pack(side=RIGHT)
       
       return mainFrame


