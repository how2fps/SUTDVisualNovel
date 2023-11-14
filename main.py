
import warnings
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

warnings.filterwarnings('ignore')

root = Tk()




def main():
       window = Tk()
       window.geometry("1920x1080")
       mainFrame = ttk.Frame(window, padding=10)
       mainFrame.grid()
       
       chatboxFrame = ttk.Frame(window, width=100, padding=10, highlightbackground='red', highlightthickness=3)
       chatboxFrame.grid(row=4,column=5)
       ttk.Label(mainFrame, text="Hello World!").grid(column=0, row=0)
       ttk.Button(mainFrame, text="Quit", command=window.destroy).grid(column=1, row=0)
       ttk.Button(mainFrame, text="Quit", command=window.destroy).grid(column=5, row=2)
       window.mainloop()

if __name__ == '__main__':
    main()