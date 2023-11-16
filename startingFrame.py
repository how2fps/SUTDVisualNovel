import warnings
from tkinter import *

from helperFunctions import *

warnings.filterwarnings('ignore')

def run(window: Tk, storyStartPage:Frame):

       mainFrame = Frame(window)
       mainFrame.pack()
       
       text = Label(mainFrame, text="test", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       text.pack(side=LEFT)
       button1 = Button(mainFrame, text='Start', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command= lambda: showFrame(storyStartPage))
       button1.pack(side=RIGHT)

       return mainFrame