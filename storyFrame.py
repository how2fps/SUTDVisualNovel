import warnings
from tkinter import *

from helperFunctions import *

warnings.filterwarnings('ignore')

def run(window:Tk):
      
       mainFrame = Frame(window)

       
       chatFrame = Frame(mainFrame ,bg="black",width=500,height=300)
       chatFrame.pack(side="bottom", fill="x")
       text = Label(chatFrame, text="cool text for novel", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       text.pack(side=LEFT)
       button1 = Button(chatFrame, text='Start', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command= lambda: print('test'))
       button1.pack(side=RIGHT)

       return mainFrame


