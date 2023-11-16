import warnings
from tkinter import *

warnings.filterwarnings('ignore')

def showFrame(currentFrame:Frame, nextFrame:Frame):
     currentFrame.pack_forget()
     nextFrame.pack(fill="both", expand=True)




def main():
     window = Tk()
     window.geometry("600x720")
     storyFrame = Frame(window)
     pictureFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="red", highlightthickness=2)
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", height=100, border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5)
     chatFrame.pack(side=BOTTOM, fill="both")
     chatFrame.pack_propagate(0)


     textbox = Label(chatFrame, text="initial novel text", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox.pack(side=LEFT)
     button1 = Button(chatFrame, text='Start', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: textbox.config(text='text'))
     button1.pack(side=RIGHT)
     

     startingFrame = Frame(window)
     startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)

     textbox2 = Label(startingFrame, text="test", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox2.pack(side=LEFT)
     
     button2 = Button(startingFrame, text='Switch to Story', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showFrame(startingFrame,storyFrame))
     button2.pack(side=RIGHT)
     
     startingFrame.tkraise()
     window.mainloop()


if __name__ == '__main__':
      main()