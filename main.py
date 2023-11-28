# Type "python main.py" without the " " in the terminal to run this project. ctrl + ` to open the terminal.
# Only need to add more scenes using txtImgOptNameSndAff function. Guide to use is below.
import warnings
import winsound
from tkinter import *

from classes import *
from jungcook import *

warnings.filterwarnings('ignore')

# Create your characters here, e.g. Xiao Ming => XIAOMING = NPC("Xiao Ming")
# Already created for you guys, just edit the name if you want
picmain = "pictures/dog.png"
picofJC = "pictures/dog.png"
picofsun = "pictures/dog.png"
picofmoon = "pictures/dog.png"
picofshadow = "pictures/dog.png"
picshadow = "pictures/dog.png"
pic = "pictures/dog.png"
protagonist =  Protagonist("", "")
XIAOMING = NPC("Xiao Ming")
JUNGCOOK = NPC("JungCook")
ADAMCMITH = NPC("Adam Cmith")
JOHNNYSIN = NPC("Johnny Sin")

DECREASE = "decrease"
INCREASE = "increase"
NEUTRAL = "neutral"
BIGGER = "bigger"
SMALLER = "smaller"

def txtImgOptNameSndAff(text:str, imgFilePath: str, options: list = [], name:str = None, soundFilePath: str = None, affectionCheck: dict = None):
            return {"text": text, "imgFilePath": imgFilePath, "name": name, "soundFilePath": soundFilePath, "options": options, "affectionCheck": affectionCheck}

def createNameFrame(window:Frame, chatFrame:Frame, characterName:str, xLocation:int = 40): # Creates the name box
       shadow1 = Label(window, text=characterName, background="#1f1f1f", foreground="black", font=("roboto", 18), padx=6, pady=6)
       shadow1.place(in_=chatFrame, x=xLocation+5, y=-23)
       shadow2 = Label(window, text=characterName, background="#2e2e2e", foreground="black", font=("roboto", 18), padx=6, pady=6)
       shadow2.place(in_=chatFrame, x=xLocation+4, y=-24)
       shadow3 = Label(window, text=characterName, background="#3b3a3a", foreground="black", font=("roboto", 18), padx=6, pady=6)
       shadow3.place(in_=chatFrame, x=xLocation+3, y=-25)
       nameLabelFrame = Label(window, text=characterName, background="#d1aa73", foreground="black", font=("roboto", 18), padx=5, pady=5, highlightbackground="#A7885C", highlightthickness=2)
       nameLabelFrame.place(in_=chatFrame, x=xLocation, y=-28)

def cleanUp(afterIds:list, dialogueContainer:Label, storyFrame:Frame):
       winsound.PlaySound(None, winsound.SND_PURGE)
       for afterId in afterIds:
              dialogueContainer.after_cancel(afterId)       
       for widget in storyFrame.winfo_children():
              widget.destroy() 

def showSelectNPCWindow(window: Tk, currentFrame: Frame, name, NPCList, photoList):
       currentFrame.pack_forget()
       selectFrame = Frame(window)
       selectFrame.pack(fill=BOTH, expand=1)
       for i in range(4):
              row = i // 2
              column = i % 2
              NPC = NPCList[i]
              image = photoList[i].subsample(3,3)
              if NPC == XIAOMING:
                     chatButton = Button(selectFrame, text=NPC.getName(), borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: createScenes(window, selectFrame,
                            [txtImgOptNameSndAff("(After a long and tiring day of classes, school has finally ended...)", "pictures/dog.png", [1]), 
                            txtImgOptNameSndAff("Damn, I can't believe that it is already 6pm... time to go home and submit my assignment.", "pictures/dog.png", [2], name, "sounds/xm1.wav"),
                            txtImgOptNameSndAff("(You head for the classroom door, ready to head home...)", "pictures/Mob_Balrog.png", [3]),
                            txtImgOptNameSndAff("(Suddenly, you felt someone grab your shoulders!)", "pictures/dog.png", [4]),
                            txtImgOptNameSndAff("NOOO WE ARE GONNA BE LATE, LETS GO NOW!", "pictures/dog.png", [5], "Mia", "sounds/xm2.wav"),
                            txtImgOptNameSndAff("", "pictures/dog.png", [{"text": "Scene 6", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Scene 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]),
                            txtImgOptNameSndAff("SCENE 6!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": SMALLER, "amount": 5, "altSceneIndex": 2 }), 
                            txtImgOptNameSndAff("SCENE 7!", "pictures/dog.png", [4], "YAY", "sounds/animalese (1).wav"),
                            ]), padx=2, pady=2)
                     chatButton.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)

              if NPC == JUNGCOOK:
                     list = []
                     for i in JC(name):
                            length = len(i)
                            textls = i[0]
                            picls = i[1]
                            if (length >= 3):
                                   third = i[2]
                            else:
                                   third = []
                            if (length >= 4):
                                   fourth = i[3]
                            else:
                                   fourth = None
                            if (length >= 5):
                                   fifth = i[4]
                            else:
                                   fifth = None
                            if (length >= 6):
                                   sixth = i[5]
                            else:
                                   sixth = None
                            list.append(txtImgOptNameSndAff(textls, picls, third, fourth, fifth))
                     chatButton = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: createScenes(window, selectFrame,
                            list), padx=2, pady=2)
                     chatButton.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
              if NPC == ADAMCMITH:
                     list = []
                     for i in JC(name):
                            length = len(i)
                            textls = i[0]
                            picls = i[1]
                            if (length >= 3):
                                   third = i[2]
                            else:
                                   third = []
                            if (length >= 4):
                                   fourth = i[3]
                            else:
                                   fourth = None
                            if (length >= 5):
                                   fifth = i[4]
                            else:
                                   fifth = None
                            if (length >= 6):
                                   sixth = i[5]
                            else:
                                   sixth = None
                            list.append(txtImgOptNameSndAff(textls, picls, third, fourth, fifth))
                     chatButton = Button(selectFrame, text=NPC.getName(), borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: createScenes(window, selectFrame,
                            ), padx=2, pady=2)
                     chatButton.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
              if NPC == JOHNNYSIN:
                     chatButton = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
                     chatButton.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     

           # Make the rows and columns expandable
       for i in range(2):
              selectFrame.grid_rowconfigure(i, weight=1)
              selectFrame.grid_columnconfigure(i, weight=1)



def createScenes(window: Tk, currentFrame: Frame, textImgNameSound: list):
       print('runn')
       storyFrame = Frame(window)
       storyFrame.pack(fill=BOTH, expand=True)
       afterIds = []
       def updateDialogue():
              nonlocal currentIndex
              name = textImgNameSound[currentIndex].get("name")
              dialogue = textImgNameSound[currentIndex].get("text")
              imgFilePath = textImgNameSound[currentIndex].get("imgFilePath")
              soundFilePath = textImgNameSound[currentIndex].get("soundFilePath")
              options = textImgNameSound[currentIndex].get("options")
              affectionCheck = textImgNameSound[currentIndex].get("affectionCheck")
              currentFrame.pack_forget() # Remove current frame
              img = PhotoImage(file=imgFilePath) # Some weird gimmick to make the image work
              pictureFrame = Label(storyFrame, image="", border="2", highlightbackground="#A7885C", highlightthickness=2, height=550)
              pictureFrame.image = img
              pictureFrame.config(image=img)
              pictureFrame.pack(side="top", fill="both")
              if (len(options) > 1): # If there are multiple options, show multiple options.
                     for option in options:
                            def updateCurrentIndex(updatedIndex=option.get("nextSceneIndex"), NPC:NPC=option.get("affection").get("affectedNPC") , affectionChange=option.get("affection").get("change") ):
                                   nonlocal currentIndex
                                   currentIndex = updatedIndex
                                   cleanUp(afterIds, dialogueContainer, storyFrame)
                                   if (affectionChange == 'increase'):
                                       print('increasing affection of ' + NPC.getName())
                                       NPC.increaseAffectionLevel()
                                   if (affectionChange =='decrease'):
                                       print('decreasing affection of ' + NPC.getName())
                                       NPC.decreaseAffectionLevel()
                                   if (affectionChange =='neutral'):
                                       print('no change of affection of ' + NPC.getName())
                            optionButton = Button(pictureFrame, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda idx=option: [updateCurrentIndex(idx.get("nextSceneIndex"), idx.get("affection").get("affectedNPC"), idx.get("affection").get("change")), updateDialogue()], padx=2, pady=6)
                            optionButton.pack(fill=X, padx=50, pady=10, expand=TRUE)
              chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="#A7885C", highlightthickness=2, padx=5, pady=5, height=300) # Container for the chat which includes dialogue and continue buttons
              chatFrame.pack(side="bottom", fill="both", expand=TRUE)
              if (name != None and len(name) > 0):
                     createNameFrame(window, chatFrame, name)
              dialogueContainer = Label(chatFrame, text="", height=0, wraplength=860, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", 16), padx=50, pady=20)
              dialogueContainer.pack(side="left")
              dialogueContainer.config(text="")
              afterIds.clear()
              for i, word in enumerate(dialogue): # Creates the text effect
                     def updateText(w=word):
                            currentText = dialogueContainer.cget("text")
                            dialogueContainer.configure(text=currentText + w)
                     afterId = dialogueContainer.after(27 * i, updateText) # Logs the afterId so I can stop it from running when I go to the next scene
                     afterIds.append(afterId)  # Store the after ID 
              if (soundFilePath != None):
                     winsound.PlaySound(soundFilePath, winsound.SND_ASYNC)
              chatButtonContainer = Frame(chatFrame, background="#d1aa73")
              chatButtonContainer.pack(side="right", fill="both")
              def continueDialogue():
                     nonlocal currentIndex
                     cleanUp(afterIds, dialogueContainer, storyFrame)
                     if (len(options) == 1):
                         currentIndex = options[0]
                     else: 
                         currentIndex += 1
                     updateDialogue()
              def continueDialogueToScene(sceneIndex: int):
                     nonlocal currentIndex
                     cleanUp(afterIds, dialogueContainer, storyFrame)
                     currentIndex = sceneIndex
                     updateDialogue()
              chatButton = Button(chatButtonContainer, text='Continue >>', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=continueDialogue, padx=2, pady=2)
              if(affectionCheck != None):
                     affectedNPC: NPC = affectionCheck.get("NPC")
                     comparison = affectionCheck.get("comparison")
                     amount: int = affectionCheck.get("amount")
                     altSceneIndex: int = affectionCheck.get("altSceneIndex")
                     if (comparison == BIGGER):
                            if (affectedNPC.getAffectionLevel() > amount):
                                   chatButton.config(command=continueDialogueToScene(altSceneIndex))
                            else:
                                   chatButton.config(command=continueDialogue)
                     if (comparison == SMALLER):
                            if (affectedNPC.getAffectionLevel() < amount):
                                   chatButton.config(command=continueDialogueToScene(altSceneIndex))
                            else:
                                   chatButton.config(command=continueDialogue)
              chatButton.pack(side="bottom")
       currentIndex:int = 0
       return updateDialogue()

from tkinter import *


def main():
    window = Tk()
    window.title('SUTDoki')
    width = 1080
    height = 720 
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2) - 70
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

    # Load background image for start menu
    bg_photo = PhotoImage(file='pictures/start_menu_bg.png')
    bg_label = Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame to hold the start menu widgets
    start_menu_frame = Frame(window, bg='#d1aa73', highlightbackground="#A7885C", highlightthickness=4)
    start_menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # Create a label for the game title
    title_label = Label(start_menu_frame, text="SUTDoki", bg='#d1aa73', font=('Comic Sans MS', 48))
    title_label.pack(pady=20)

    # Create an entry for the player to input their name
    name_label = Label(start_menu_frame, text="What's your name?", bg='#d1aa73', font=('Comic Sans MS', 24))
    name_label.pack()
    name_entry = Entry(start_menu_frame, font=('Arial', 24))
    name_entry.pack(padx=10, pady=10)

    NPClist = [JOHNNYSIN,JUNGCOOK,ADAMCMITH,XIAOMING]
    photoList = [
           PhotoImage(file="pictures/dog.png"),
           PhotoImage(file="pictures/dog.png"),
           PhotoImage(file="pictures/dog.png"),
           PhotoImage(file="pictures/dog.png")
    ]

    # Create the start button
    start_button = Button(start_menu_frame, text="Start Story", font=('Arial', 24), command=lambda: 
            [protagonist.setName(name_entry.get()), showSelectNPCWindow(window, start_menu_frame, name_entry.get(), NPClist, photoList)])
    start_button.pack(pady=20)

    window.mainloop()

# def main():
#        window = Tk()
#        window.title('SUTDoki')
#        width = 1080
#        height = 720 
#        ws = window.winfo_screenwidth()
#        hs = window.winfo_screenheight()
#        x = (ws/2) - (width/2)
#        y = (hs/2) - (height/2) - 70
#        window.geometry('%dx%d+%d+%d' % (width, height, x, y))

#        startingFrame = Frame(window)
#        startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)
#        Label(startingFrame, text="Enter your name").pack()
#        nameInput = Entry(startingFrame)
#        nameInput.pack()
       
       # ****FUNCTION txtImgOptNameSndAff****

       # "text" is what the dialogue in the chatbox reads, leave it empty during multiple option scenes.

       # "imgFilePath" is the relative image file path to this file, a few examples are shown (ONE image for each scene, edit the characters onto the image, 1080x550 resolution)

       # "name" is the name of the character who is speaking, it will appear in the name box at the top left of the chatbox, leave it empty to not have the name box shown.

       # "soundFilePath" is the relative sound file path to this file, a few examples are shown.

       # "affectionCheck" is a dictionary in this format {"NPC": XIAOMING, "comparison": SMALLER, "amount": 5, "altSceneIndex": 2 }. 
       # "NPC" is the NPC you want to check the affection level of.
       # "comparison" is to check whether it is smaller or bigger than the "amount".
       # "altSceneIndex" is the alternate scene you want to go to when the comparison returns TRUE.

       # "options" is a list that dictates what scenes the buttons go to.
       # If you have multiple options, create a list of dictionary
       # [{"text": "Scene 6", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, 
       #  {"text": "Scene 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}] < like this
       # where "text" is the text shown in the option button, and "nextSceneIndex" is the scene's index in the array it will jump to when the button is pressed.
       # If you put options as a single number in a list e.g. [3], it will go to the scene at array index 3.
       # If you put options as [], an empty list, it will go to the scene in the next index.
       # "affection" is a dictionary that takes in the affected NPC and whether the button will INCREASE or DECREASE his affection.
       # If neutral, just put {"text": "Neutral Option Example", "nextSceneIndex": 8}, without "affection"
       # [{"text": "Positive Option Example", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, 
       #  {"text": "Negative Option Example", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}},
       #  {"text": "Neutral Option Example", "nextSceneIndex": 8} ] < like this

       # https://acedio.github.io/animalese.js/ < please use this to generate more animal crossing sounds, need to format this to .wav even though it is already .wav if not winsound wouldn't run it
       # https://cloudconvert.com/wav-converter < use this to reformat the animal crossing sounds
       
       # textbox = Label(startingFrame, text="Starting Screen", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       # textbox.pack(side=LEFT)
       # NPClist = [JOHNNYSIN,JUNGCOOK,ADAMCMITH,XIAOMING]


       # # How to find out what index your dialogue is in the array: Take the current line of your array and subtract from the starting line. P.S: Put your dialogues in this vertical manner. 
       # startButton = Button(startingFrame, text="Start Story", borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: 
       #        [protagonist.setName(nameInput.get()), showSelectNPCWindow(window, startingFrame, nameInput.get(), NPClist)])
       # startButton.pack(side=RIGHT)
       # window.mainloop()
     

if __name__ == '__main__':
       main()



