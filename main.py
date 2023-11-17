import warnings
import winsound
from tkinter import *

from classes import *


def playSound():
    # Replace 'sound.wav' with your sound file name and path
    winsound.PlaySound('sounds/animalese (1).wav', winsound.SND_ASYNC)

winsound.PlaySound('sounds/justforfun.wav', winsound.SND_ASYNC)
warnings.filterwarnings('ignore')

placeholderText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
placeholderText2 = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inven."

protagonist =  Protagonist("")

def showNextFrame(currentFrame:Frame, nextFrame:Frame, nextLabelFrame:Frame=None, nextLabelFrameText: str=None):
     currentFrame.pack_forget()
     nextFrame.pack(fill="both", expand=True)
     if (nextLabelFrame != None):
       
          updateLabelFrame(nextLabelFrame, nextLabelFrameText)

def updateLabelFrame(labelFrame:Label, updatedText):
     playSound()
     labelFrame.config(text="")
     for i, word in enumerate(updatedText):
          labelFrame.after(20 * i, lambda w=word: labelFrame.configure(text=labelFrame.cget("text")+w))

def createLabelFrame(referenceFrame:Frame, txt:str, fontSize:int, height:int, padX:int, padY: int):
     return Label(referenceFrame, text=txt, height=height, borderwidth=2, wraplength=860, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", fontSize), padx=padX, pady=padY)

def createStartingFrame(window:Frame, storyFrame:Frame, nextLabelFrame:Frame):
     startingFrame = Frame(window)
     startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)
     Label(startingFrame, text="Enter your name").pack()
     nameInput = Entry(startingFrame)
     nameInput.pack()
     textbox = Label(startingFrame, text="Starting Screen", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox.pack(side=LEFT)
          
     startButton = Button(startingFrame, text="Start Story", borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: 
          [protagonist.setName(nameInput.get()),showNextFrame(startingFrame, storyFrame, nextLabelFrame, f"Hi {protagonist.name}! " + placeholderText)])
     startButton.pack(side=RIGHT)

     startingFrame.tkraise()

     return startingFrame

def createStoryFrameWithoutOptions(window:Tk, img, characterName, nextFrame:Frame=None, nextLabelFrame:Frame=None, nextLabelFrameText:str=""):
     storyFrame = Frame(window)
     img = PhotoImage(file=img)
     pictureFrame = Label(storyFrame, image=img, border="2", highlightbackground="red", highlightthickness=2, height=550)
     pictureFrame.image = img
     pictureFrame.config(image=img) #gotta do this weird thing to load images
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5, height=300)
     chatFrame.pack(side=BOTTOM, fill="both", expand=TRUE)

     

     shadow = Label(window, text=characterName, height=0, borderwidth=2, wraplength=860, justify=LEFT, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=7, pady=5)
     shadow.place(in_=chatFrame, x=39, y=-25)
     nameLabelFrame = createLabelFrame(window, characterName, 18, 0, 5, 5)
     nameLabelFrame.place(in_=chatFrame, x=40, y=-28)


     chatLabelFrame = createLabelFrame(chatFrame, "", 16, 0, 50, 20)
     chatLabelFrame.pack(side=LEFT)

     chatButtonContainer = Frame(chatFrame, background="#d1aa73")
     chatButtonContainer.pack(side=RIGHT, fill="both")

     chatButton = Button(chatButtonContainer, text='Continue >>', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), padx=2, pady=2)
     chatButton.pack(side=BOTTOM)

     return storyFrame, chatLabelFrame

def createStoryFrameWithOptions(window:Tk, img, characterName, 
                                nextFrame1:Frame = None, nextLabelFrame1:Frame = None, nextLabelFrameText1:str = "",
                                nextFrame2:Frame = None, nextLabelFrame2:Frame = None, nextLabelFrameText2:str = ""):
     storyFrame = Frame(window)
     img = PhotoImage(file=img)

     pictureFrame = Label(storyFrame, image=img, border="2", highlightbackground="red", highlightthickness=2, height=550)
     pictureFrame.image = img
     pictureFrame.config(image=img) #gotta do this weird thing to load images
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5, height=300)
     chatFrame.pack(side=BOTTOM, fill="both", expand=TRUE)


     shadow = Label(window, text=characterName, height=0, borderwidth=2, wraplength=860, justify=LEFT, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=7, pady=5)
     shadow.place(in_=chatFrame, x=39, y=-25)
     nameLabelFrame = createLabelFrame(window, characterName, 18, 0, 5, 5)
     nameLabelFrame.place(in_=chatFrame, x=40, y=-28)


     chatButtonContainer = Frame(chatFrame, background="#d1aa73", pady=20)
     chatButtonContainer.pack(fill="both")
     
     optionButton1 = Button(chatButtonContainer, text='Do this option 1', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), padx=2, pady=2)
     optionButton1.pack(side=TOP)
     empty_label = Label(chatButtonContainer, text='', background="#d1aa73", pady=1)
     empty_label.pack()
     optionButton2 = Button(chatButtonContainer, text='Do this option 2 etc', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), padx=2, pady=2)
     optionButton2.pack(side=BOTTOM)

     return storyFrame

def main():
     window = Tk()
     window.geometry("1080x720")
     placeholderFrame = Frame()

     storyFrame3 = createStoryFrameWithOptions(window, "pictures/Mob_Balrog.png", "Balrog 2", placeholderFrame)

     [storyFrame2, chatLabelFrame2] = createStoryFrameWithoutOptions(window, "pictures/dog.png", "D.O.G", storyFrame3)

     [storyFrame, chatLabelFrame] = createStoryFrameWithoutOptions(window, "pictures/Mob_Balrog.png", "Balrog", storyFrame2, chatLabelFrame2, placeholderText2)

     createStartingFrame(window, storyFrame, chatLabelFrame)

     window.mainloop()

if __name__ == '__main__':
      main()