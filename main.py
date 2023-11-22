import warnings
import winsound
from tkinter import *

from classes import *

warnings.filterwarnings('ignore')

protagonist =  Protagonist("", "")
Willy = NPC("Willy")

def playSound(relativeFilePath:str):
    winsound.PlaySound(relativeFilePath, winsound.SND_ASYNC)

def createLabelFrame(referenceFrame:Frame, txt:str, fontSize:int, height:int, padX:int, padY: int):
     return Label(referenceFrame, text=txt, height=height, wraplength=860, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", fontSize), padx=padX, pady=padY)

def createNameFrame(window:Frame, chatFrame:Frame, characterName:str, xLocation:int = 40):
     shadow1 = Label(window, text=characterName, background="#1f1f1f", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow1.place(in_=chatFrame, x=xLocation+5, y=-23)
     shadow2 = Label(window, text=characterName, background="#2e2e2e", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow2.place(in_=chatFrame, x=xLocation+4, y=-24)
     shadow3 = Label(window, text=characterName, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=6, pady=6)
     shadow3.place(in_=chatFrame, x=xLocation+3, y=-25)
     nameLabelFrame = Label(window, text=characterName, background="#d1aa73", foreground="black", font=("roboto", 18), padx=5, pady=5, highlightbackground="#A7885C", highlightthickness=2)
     nameLabelFrame.place(in_=chatFrame, x=xLocation, y=-28)


def createDialogueFrameNew(window: Tk, currentFrame: Frame, textImgNameSound: list):
    storyFrame = Frame(window)
    storyFrame.pack(fill=BOTH, expand=True)
    after_ids = []
    def update_dialogue():
       currentIndex
       pictureFrame = Label(storyFrame, image="", border="2", highlightbackground="red", highlightthickness=2, height=550)
       name = textImgNameSound[currentIndex].get("name")
       dialogue = textImgNameSound[currentIndex].get("text")
       imgFilePath = textImgNameSound[currentIndex].get("imgFilePath")
       soundFilePath = textImgNameSound[currentIndex].get("soundFilePath")
       options = textImgNameSound[currentIndex].get("options")
       currentFrame.pack_forget()
       img = PhotoImage(file=imgFilePath)
       pictureFrame.image = img
       pictureFrame.config(image=img)
       pictureFrame.pack(side="top", fill="both")
       if (len(options) > 1):
            for option in options:
                def updateCurrentIndex(updatedIndex=option.get("nextSceneIndex")):
                       nonlocal currentIndex
                       currentIndex = updatedIndex
                       print(currentIndex)
                       winsound.PlaySound(None, winsound.SND_PURGE)
                       for after_id in after_ids:
                              dialogueContainer.after_cancel(after_id)
                       for widget in storyFrame.winfo_children():
                              widget.destroy()
                optionButton = Button(pictureFrame, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda idx=option.get("nextSceneIndex"): [updateCurrentIndex(idx), update_dialogue()], padx=2, pady=6)
                optionButton.pack(fill=X, padx=50, pady=10, expand=TRUE)
       chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="white", highlightthickness=2, padx=5, pady=5, height=300)
       chatFrame.pack(side="bottom", fill="both", expand=TRUE)
       if (name != None and len(name) > 0):
           createNameFrame(window, chatFrame, name)
       dialogueContainer = createLabelFrame(chatFrame, "", 16, 0, 50, 20)
       dialogueContainer.pack(side="left")
       dialogueContainer.config(text="")
       after_ids.clear()
       for i, word in enumerate(dialogue):
            def update_text(w=word):
                current_text = dialogueContainer.cget("text")
                dialogueContainer.configure(text=current_text + w)
            after_id = dialogueContainer.after(20 * i, update_text)
            after_ids.append(after_id)  # Store the after ID 
       if (soundFilePath != None):
         playSound(soundFilePath)
       chatButtonContainer = Frame(chatFrame, background="#d1aa73")
       chatButtonContainer.pack(side="right", fill="both")
       def continue_dialogue():
           nonlocal currentIndex
           winsound.PlaySound(None, winsound.SND_PURGE)
           for after_id in after_ids:
               dialogueContainer.after_cancel(after_id)
           for widget in storyFrame.winfo_children():
               widget.destroy()
           if (len(options) == 1):
                currentIndex = options[0]
           else: 
                currentIndex += 1
           update_dialogue()
       chatButton = Button(chatButtonContainer, text='Continue >>', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=continue_dialogue, padx=2, pady=2)
       chatButton.pack(side="bottom")
    currentIndex = 0
    return update_dialogue()

def main():
     window = Tk()
     window.geometry("1080x720")
     startingFrame = Frame(window)
     startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)
     Label(startingFrame, text="Enter your name").pack()
     nameInput = Entry(startingFrame)
     nameInput.pack()
     # text is what the dialogue in the chatbox reads, leave it empty during multiple option scenes.
     # imgFilePath is the relative image file path to this file, a few examples are shown (please create the characters on the background)
     # name is the name of the character who is speaking, it will appear in the name box at the top left of the chatbox, leave it empty to not have the name box shown.
     # soundFilePath is the relative sound file path to this file, a few examples are shown.
     # https://acedio.github.io/animalese.js/ < please use this to generate more animal crossing sounds, need to format this to .wav even though it is already .wav if not winsound wouldn't run it
     # https://cloudconvert.com/wav-converter < use this to reformat the animal crossing sounds

     # options is a list that dictates what scenes the buttons go to.
     # In multiple options, create a list of dictionary [{"text": "Scene 6", "nextSceneIndex": 6}, {"text": "Scene 7", "nextSceneIndex": 7}] like this,
     # where "text" is the text shown in the option button, and "nextSceneIndex" is the scene's index in the array it will jump to when the button is pressed.
     # If you put options as a single number in a list e.g. [3], it will go to the scene at array index 3.
     # If you put options as [], an empty list, it will go to the scene in the next index.

     def txtImgOptNameSnd(text:str, imgFilePath: str, options: list = [], name:str = None, soundFilePath: str = None):
          return {"text": text, "imgFilePath": imgFilePath, "name": name, "soundFilePath": soundFilePath, "options": options}
     textbox = Label(startingFrame, text="Starting Screen", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
     textbox.pack(side=LEFT)
     scenesList = [txtImgOptNameSnd("(After a long and tiring day of classes, school has finally ended...)", "pictures/dog.png", [1]), 
                   txtImgOptNameSnd("Damn, I can't believe that it is already 6pm... time to go home and submit my assignment.", "pictures/dog.png", [2], nameInput.get(), "sounds/animalese (1).wav"),
                   txtImgOptNameSnd("(You head for the classroom door, ready to head home...)", "pictures/dog.png", [3]),
                   txtImgOptNameSnd("(Suddenly, you felt someone grab your shoulders!)", "pictures/dog.png", [4]),
                   txtImgOptNameSnd("NOOO WE ARE GONNA BE LATE, LETS GO NOW!", "pictures/dog.png", [5], "Mia", "sounds/animalese (1).wav"),
                   txtImgOptNameSnd("", "pictures/dog.png", [{"text": "Scene 6", "nextSceneIndex": 6}, {"text": "Scene 7", "nextSceneIndex": 7}]),
                   txtImgOptNameSnd("SCENE 6!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav"),
                   txtImgOptNameSnd("SCENE 7!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav")
                   ]
     startButton = Button(startingFrame, text="Start Story", borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: 
          [protagonist.setName(nameInput.get()), (createDialogueFrameNew(window, startingFrame, scenesList))])
     
 
     startButton.pack(side=RIGHT)
     window.mainloop()
     

if __name__ == '__main__':
      main()

