import warnings
from tkinter import *

warnings.filterwarnings('ignore')

placeholderText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
placeholderText2 = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inven."

def showFrame(currentFrame:Frame, nextFrame:Frame, labelFrame:Frame=None, text: str=None):
     currentFrame.pack_forget()
     nextFrame.pack(fill="both", expand=True)
     if (labelFrame != None):
          updateLabelText(labelFrame, text)
     

def updateLabelText(labelFrame:Label, updatedText):
     labelFrame.config(text="")
     for i, word in enumerate(updatedText):
          labelFrame.after(10 * i, lambda w=word: labelFrame.configure(text=labelFrame.cget("text")+w))


def createLabelText(referenceFrame:Frame, txt:str, fontSize:int, height:int, padX:int, padY: int):
     return Label(referenceFrame, text=txt, height=height, borderwidth=2, wraplength=480, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", fontSize), padx=padX, pady=padY)


def createStartingFrame(window:Frame, storyFrame:Frame, nextLabelFrame:Frame):
     startingFrame = Frame(window)
     startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)

     textbox = Label(startingFrame, text="Starting Screen", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox.pack(side=LEFT)
     
     button = Button(startingFrame, text="Start Story", borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showFrame(startingFrame, storyFrame, nextLabelFrame, placeholderText))
     button.pack(side=RIGHT)
     startingFrame.tkraise()
     return startingFrame

def createStoryFrame(window:Tk, nextFrameText:str, img:str, nextFrame:Frame, labelFrame:Frame):
     storyFrame = Frame(window)
     img = PhotoImage(file=img)
     pictureFrame = Label(storyFrame, image=img, border="2", highlightbackground="red", highlightthickness=2, height=550)
     pictureFrame.image = img
     pictureFrame.config(image=img)
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5)
     chatFrame.pack(side=BOTTOM, fill="both")

     namebox = createLabelText(window, "protagonist name", 18, 0, 4, 4)
     namebox.place(in_=chatFrame, x=20, y=-28)

     textbox = createLabelText(chatFrame, "", 16, 0, 20, 20)
     textbox.pack(side=LEFT)

     button = Button(chatFrame, text='Continue', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showFrame(storyFrame, nextFrame, labelFrame, nextFrameText))
     button.pack(side=RIGHT)

     return storyFrame, textbox


def main():
     window = Tk()
     window.geometry("600x720")
     placeholderFrame = Frame()

     [storyFrame2, textbox2] = createStoryFrame(window, "dededede", "pictures/dog.png", placeholderFrame, placeholderFrame)

     [storyFrame, textbox] = createStoryFrame(window, placeholderText2, "pictures/Mob_Balrog.png", storyFrame2, textbox2)

     createStartingFrame(window, storyFrame, textbox)

     window.mainloop()

if __name__ == '__main__':
      main()