import warnings
import winsound
from tkinter import *

from classes import *

warnings.filterwarnings('ignore')


placeholderText = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
placeholderText2 = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inven."

protagonist =  Protagonist("")
Willy = NPC("Willy")

def playSound(relativeFilePath:str):
    winsound.PlaySound(relativeFilePath, winsound.SND_ASYNC)


def showNextFrame(currentFrame:Frame, nextFrame:Frame, nextLabelFrame:Frame=None, nextLabelFrameText: str=None):
     currentFrame.pack_forget()
     nextFrame.pack(fill="both", expand=True)
     if (nextLabelFrame != None):
          updateLabelFrame(nextLabelFrame, nextLabelFrameText)


def updateLabelFrame(labelFrame:Label, updatedText:str):
     playSound('sounds/animalese (1).wav')
     labelFrame.config(text="")
     for i, word in enumerate(updatedText):
          labelFrame.after(20 * i, lambda w=word: labelFrame.configure(text=labelFrame.cget("text")+w))


def createLabelFrame(referenceFrame:Frame, txt:str, fontSize:int, height:int, padX:int, padY: int):
     return Label(referenceFrame, text=txt, height=height, wraplength=860, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", fontSize), padx=padX, pady=padY)


def createNameFrame(window:Frame, chatFrame:Frame, characterName:str, xLocation:int):
     
     shadow1 = Label(window, text=characterName, background="#1f1f1f", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow1.place(in_=chatFrame, x=xLocation+5, y=-23)
     shadow2 = Label(window, text=characterName, background="#2e2e2e", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow2.place(in_=chatFrame, x=xLocation+4, y=-24)
     shadow3 = Label(window, text=characterName, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow3.place(in_=chatFrame, x=xLocation+3, y=-25)

     nameLabelFrame = Label(window, text=characterName, background="#d1aa73", foreground="black", font=("roboto", 18), padx=5, pady=5, highlightbackground="#A7885C", highlightthickness=2)
     nameLabelFrame.place(in_=chatFrame, x=xLocation, y=-28)


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

     return startingFrame


def createDialogueFrame(window:Tk, imgFilePath, characterName, characterNameLocation, nextFrame:Frame=None, nextLabelFrame:Frame=None, nextLabelFrameText:str=""):
     storyFrame = Frame(window)
     img = PhotoImage(file=imgFilePath)
     pictureFrame = Label(storyFrame, image=img, border="2", highlightbackground="red", highlightthickness=2, height=550)
     pictureFrame.image = img
     pictureFrame.config(image=img) #gotta do this weird thing to load images
     pictureFrame.pack(side=TOP, fill="both")

     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5, height=300)
     chatFrame.pack(side=BOTTOM, fill="both", expand=TRUE)

     createNameFrame(window, chatFrame, characterName, characterNameLocation)

     dialogueContainer = createLabelFrame(chatFrame, "", 16, 0, 50, 20)
     dialogueContainer.pack(side=LEFT)

     chatButtonContainer = Frame(chatFrame, background="#d1aa73")
     chatButtonContainer.pack(side=RIGHT, fill="both")

     chatButton = Button(chatButtonContainer, text='Continue >>', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), padx=2, pady=2)
     chatButton.pack(side=BOTTOM)

     return storyFrame, dialogueContainer



def createOptionsFrameWithoutDialogueBox  (window:Tk, imgFilePath:str, options):
     storyFrame = Frame(window)

     img = PhotoImage(file=imgFilePath)

     pictureFrame = Label(storyFrame, image=img, highlightbackground="red", highlightthickness=2)
     pictureFrame.image = img
     pictureFrame.config(image=img) #gotta do this weird thing to load images
     pictureFrame.pack(fill="both", expand=TRUE,)

     for option in options:
          nextFrame = option['showNextFrame'][0]
          nextLabelFrame = option['showNextFrame'][1]
          nextLabelFrameText = option['showNextFrame'][2]
          NPC = None 
          affectionChange = None
          if (len(option) == 4):
               affectionChange = option['showNextFrame'][3][0]
               NPC = option['showNextFrame'][3][1]
          def create_lambda(nextFrame=nextFrame, nextLabelFrame=nextLabelFrame, nextLabelFrameText=nextLabelFrameText, NPC=NPC):
               if (NPC and affectionChange=="decrease"):
                    return lambda: [showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), NPC.decreaseAffectionLevel()]
               if (NPC and affectionChange=="increase"):
                    return lambda: [showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText), NPC.increaseAffectionLevel()]
               return lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText)
          optionButton = Button(pictureFrame, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font=("roboto",20), command=create_lambda(), padx=2, pady=6)
          optionButton.pack(fill=X, padx=50, pady=10, expand=TRUE)

     return storyFrame


def main():
     window = Tk()
     window.geometry("1080x720")
     placeholderFrame = Frame()
     
     [storyFrame18, dialogueContainer18] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, placeholderFrame, placeholderFrame)
     [storyFrame17, dialogueContainer17] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame18, dialogueContainer18,'dialogue 2')
     [storyFrame16, dialogueContainer16] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame17, dialogueContainer17,'dialog1ue 2')
     [storyFrame15, dialogueContainer15] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame16, dialogueContainer16,'dialogu23e 2')
     [storyFrame14, dialogueContainer14] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame15, dialogueContainer15,'dialogue23 2')
     [storyFrame13, dialogueContainer13] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame14, dialogueContainer14,'dialog2ue 2')
     [storyFrame12, dialogueContainer12] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 41, storyFrame13, dialogueContainer13,'dialo3gue 2')
     [storyFrame11, dialogueContainer11] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame12, dialogueContainer12,'dialog2ue 3122')
     [storyFrame10, dialogueContainer10] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame11, dialogueContainer11,'dialogue 2')
     [storyFrame9, dialogueContainer9] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 40, storyFrame10, dialogueContainer10,'dialo2gue 2')
     [storyFrame8, dialogueContainer8] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5004", 45, storyFrame9, dialogueContainer9,'dialog4ue 2')
     [storyFrame7, dialogueContainer7] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5003", 40, storyFrame8, dialogueContainer8,'dialog5ue 2')
     [storyFrame6, dialogueContainer6] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5002", 40, storyFrame7, dialogueContainer7,'dialog2ue 322')
     [storyFrame5, dialogueContainer5] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5001", 35, storyFrame6, dialogueContainer6,'dia1logue 2')
     [storyFrame4, dialogueContainer4] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog5000", 43, storyFrame5, dialogueContainer5,'dialogu22e 2')

     storyFrame3 = createOptionsFrameWithoutDialogueBox(window, "pictures/Mob_Balrog.png", [{'text':'Option 1', 'showNextFrame':[storyFrame4, dialogueContainer4, 'dede', [Willy, 'decrease']]},
                                                                                               {'text':'Option 2', 'showNextFrame':[storyFrame4, dialogueContainer4, 'damn']},
                                                                                               {'text':'Option 3', 'showNextFrame':[storyFrame4, dialogueContainer4, 'tete']}])
     
     [storyFrame2, dialogueContainer2] = createDialogueFrame(window, "pictures/dog.png", "D.O.G", 60, storyFrame3)

     [storyFrame, dialogueContainer] = createDialogueFrame(window, "pictures/Mob_Balrog.png", "Balrog", 30, storyFrame2, dialogueContainer2, placeholderText2)

     createStartingFrame(window, storyFrame, dialogueContainer)

     window.mainloop()

if __name__ == '__main__':
      main()



# This is to create an option screen where the options are in a dialogue box like a typical dialogue screen instead of on the picture, not used atm.
# def createOptionsFrame  (window:Tk, imgFilePath:str, characterName:str, options):
#      storyFrame = Frame(window)

#      img = PhotoImage(file=imgFilePath)
#      pictureFrame = Label(storyFrame, image=img, border="2", highlightbackground="red", highlightthickness=2, height=550)
#      pictureFrame.image = img
#      pictureFrame.config(image=img) #gotta do this weird thing to load images
#      pictureFrame.pack(side=TOP, fill="both")

#      chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5, height=300)
#      chatFrame.pack(side=BOTTOM, fill="both", expand=TRUE)

#      if (characterName != ""):
#           shadow = Label(window, text=characterName, height=0, borderwidth=2, wraplength=860, justify=LEFT, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=7, pady=5)
#           shadow.place(in_=chatFrame, x=39, y=-25)
#           nameLabelFrame = createLabelFrame(window, characterName, 18, 0, 5, 5)
#           nameLabelFrame.place(in_=chatFrame, x=40, y=-28)

#      chatButtonContainer = Frame(chatFrame, background="#d1aa73", pady=20)
#      chatButtonContainer.pack(fill="both")

#      for option in options:
#           nextFrame = option['showNextFrame'][0]
#           nextLabelFrame = option['showNextFrame'][1]
#           nextLabelFrameText = option['showNextFrame'][2]
#           def create_lambda(nextFrame=nextFrame, nextLabelFrame=nextLabelFrame, nextLabelFrameText=nextLabelFrameText):
#                return lambda: showNextFrame(storyFrame, nextFrame, nextLabelFrame, nextLabelFrameText)
#           optionButton = Button(chatButtonContainer, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font="roboto", command=create_lambda(), padx=1, pady=1)
#           optionButton.pack(side=TOP)
#           empty_label = Label(chatButtonContainer, text='', background="#d1aa73", font=("roboto", 1))
#           empty_label.pack()

#      return storyFrame