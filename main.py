import warnings
from tkinter import *

import helperFunctions
import startingFrame
import storyFrame

warnings.filterwarnings('ignore')


def main():
       window = Tk()
       window.geometry("1280x720")
       startingFrame.run(window)
       storyFrame.run(window)

if (__name__ == '__main__'):
       main()


