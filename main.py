import warnings
from tkinter import *

warnings.filterwarnings('ignore')

placeholderText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

def showFrame(currentFrame:Frame, nextFrame:Frame):
     currentFrame.pack_forget()
     nextFrame.pack(fill="both", expand=True)

def updateLabelText(labelFrame:Label, updatedText):
     labelFrame.config(text=updatedText)

def createLabelText(referenceFrame:Frame, txt:str, fontSize:int, height:int, padX:int, padY: int):
     return Label(referenceFrame, text=txt, height=height, borderwidth=2, wraplength=480, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", fontSize), highlightbackground='green', highlightthickness=1, padx=padX, pady=padY)


def main():
     window = Tk()
     window.geometry("600x720")
     storyFrame = Frame(window)
     pictureFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="red", highlightthickness=2)
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5)
     chatFrame.pack(side=BOTTOM, fill="both")

     namebox = createLabelText(window, "protagonist name", 18, 0, 4, 4)
     namebox.place(in_=chatFrame, x=20, y=-28)

     textbox = createLabelText(chatFrame, 'visual novel text', 16, 0, 20, 20)
     textbox.pack(side=LEFT)
     button1 = Button(chatFrame, text='Start', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: updateLabelText(textbox, placeholderText))
     button1.pack(side=RIGHT)
     

     startingFrame = Frame(window)
     startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)

     textbox2 = Label(startingFrame, text="test", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox2.pack(side=LEFT)
     
     button2 = Button(startingFrame, text='Switch to Story', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showFrame(startingFrame, storyFrame))
     button2.pack(side=RIGHT)
     
     startingFrame.tkraise()
     window.mainloop()


if __name__ == '__main__':
      main()