import warnings
from tkinter import *

import storyFrame
from helperFunctions import *

warnings.filterwarnings('ignore')



def run(window):

       mainFrame = Frame(window)
       mainFrame.pack()
 
       text = Label(mainFrame, text="cool text for cool visual novel", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       # text.insert(INSERT, 'cool text for cool visual novel')
       text.pack(side=LEFT)
       button1 = Button(mainFrame, text='Hello', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showFrame())
       button1.pack(side=RIGHT)
       window.mainloop()

       return mainFrame