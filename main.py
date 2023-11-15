import warnings
from tkinter import *

import startingFrame
import storyFrame
from helperFunctions import *

warnings.filterwarnings('ignore')


def main():
       window = Tk()
       window.geometry("600x720")
       storyPage = storyFrame.run(window)
       startingPage = startingFrame.run(window, storyPage)

       storyPage.grid(row=0, column=0, sticky="nsew")
       startingPage.grid(row=0, column=0, sticky="nsew")
       showFrame(startingPage)
       window.mainloop()

if (__name__ == '__main__'):
       main()
