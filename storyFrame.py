import warnings
from tkinter import *

from helperFunctions import *

warnings.filterwarnings('ignore')

def run(window:Tk):
      
       mainFrame = Frame(window)
 
       text = Label(mainFrame, text="cool text for visual novel", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       text.pack(side=LEFT)
       button1 = Button(mainFrame, text='Start', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command= lambda: print('test'))
       button1.pack(side=RIGHT)

       return mainFrame


