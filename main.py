# Type "python main.py" without the " " in the terminal to run this project. ctrl + ` to open the terminal.
# Only need to add more scenes using txtImgOptNameSndAff function. Guide to use is below.
import warnings
import winsound
from tkinter import *
from classes import *
from jungcook import *
from adamcmith import *

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
       # How to find out what index your dialogue is in the array: Take the current line of your array and subtract from the starting line. P.S: Put your dialogues in this vertical manner. 
       currentFrame.pack_forget()
       selectFrame = Frame(window)
       selectFrame.pack(fill=BOTH, expand=1)
       for i in range(4):
              row = i // 2
              column = i % 2
              NPC = NPCList[i]
              image = photoList[i].subsample(3,3)
              photoList[i] = image  # keep the reference to the new PhotoImage
              if NPC == XIAOMING:
                     chatButton1 = Button(selectFrame, text=NPC.getName(), image= image, compound=TOP,  borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda i=i :createScenes(window, selectFrame,
                            [txtImgOptNameSndAff("(After a long and tiring day of classes, school has finally ended...)", "pictures/dog.png", [1]), 
                            txtImgOptNameSndAff("Damn, I can't believe that it is already 6pm... time to go home and submit my assignment.", "pictures/dog.png", [2], name, "sounds/xm1.wav"),
                            txtImgOptNameSndAff("(You head for the classroom door, ready to head home...)", "pictures/Mob_Balrog.png", [3]),
                            txtImgOptNameSndAff("(Suddenly, you felt someone grab your shoulders!)", "pictures/dog.png", [4]),
                            txtImgOptNameSndAff("NOOO WE ARE GONNA BE LATE, LETS GO NOW!", "pictures/dog.png", [5], "Mia", "sounds/xm2.wav"),
                            txtImgOptNameSndAff("", "pictures/dog.png", [{"text": "Scene 6", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Scene 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]),
                            txtImgOptNameSndAff("SCENE 6!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": SMALLER, "amount": 5, "altSceneIndex": 2 }), 
                            txtImgOptNameSndAff("SCENE 7!", "pictures/dog.png", [4], "YAY", "sounds/animalese (1).wav"),
                            ]), padx=2, pady=2)
                     chatButton1.grid(row=row, column=column+2, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     description1 = Label(selectFrame, text="Shy yet sporty tech student\n\n-Introverted coder\n\n-Confident athlete\n\n-Uses his tech prowess \nto solve challenges\n\nJoin him on his journey from \nnovice coder to top tech expert", bg="#8cb9ed", font=("Comic Sans MS", 15))
                     description1.grid(row=row, column=column+3, sticky=W+E)

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
                                   print(sixth)
                            else:
                                   sixth = None
                            list.append(txtImgOptNameSndAff(textls, picls, third, fourth, fifth, sixth))
                     chatButton2 = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda i=i :createScenes(window, selectFrame,
                            list), padx=2, pady=2)
                     chatButton2.grid(row=row, column=column+2, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     description2 = Label(selectFrame, text="-Fiery Korean chef with a tsundere personality\n\n-Known as the 'Korean Gordon Ramsey'\n\n-Despite his tough exterior, he has a\nsoft spot for those he cares about.\n\n-Uses his culinary prowess to create\nmouth-watering dishes that leave everyone in awe.\n\nJoin him on his journey from being a\nrenowned chef to the star of the Prom night", bg="#ed8ce0",font=("Comic Sans MS", 15))
                     description2.grid(row=row, column=column+3, sticky=W+E)
              if NPC == ADAMCMITH:
                     list = []
                     for i in AC(name):
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
                                   print(sixth)
                            else:
                                   sixth = None
                            list.append(txtImgOptNameSndAff(textls, picls, third, fourth, fifth, sixth))
                     chatButton3 = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda i=i :createScenes(window, selectFrame,
                            list), padx=2, pady=2)
                     chatButton3.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     description3 = Label(selectFrame, text="Your childhood friend with a heart of gold.\n\n-A familiar face from your past,\nalways there in your memories.\n\n-Always there when you need him.\n\nDespite the time that's passed,\nyour bond with him remains strong.\n\n-He is a constant source of support and companionship.\n\nJoin him on a journey of reconnection,\nfrom accidental encounters to shared memories.",bg="#8ced8f", font=("Comic Sans MS", 15))
                     description3.grid(row=row, column=column+2, sticky=W+E)
              if NPC == JOHNNYSIN:
                     chatButton4 = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20))
                     chatButton4.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     description4 = Label(selectFrame, text="An exchange student from the USA with\na heart as warm as his home state.\n\nHis charm lies in his adventurous spirit\nand his willingness to immerse\nhimself in new experiences.\n\n-Johnny's enthusiasm is infectious\n\n-He brings a touch of foreign intrigue\nand a lot of friendly warmth.\n\nJoin him on his journey of cultural exchange.", bg="#ed8c8c",font=("Comic Sans MS", 15))
                     description4.grid(row=row, column=column+2, sticky=W+E)
       
                  # Make the rows and columns expandable
       # Make the rows and columns expandable
       for i in range(2):
              selectFrame.grid_rowconfigure(i, weight=1)
              for j in range(4):
                     selectFrame.grid_columnconfigure(j, weight=1)    

       # Make the window open up to the size of the elements
       window.update_idletasks()
       window.geometry(window.geometry())  # set the window size to the size of its elements

       # Get screen size
       screen_width = window.winfo_screenwidth()
       screen_height = window.winfo_screenheight()

       # Get window size
       window_width = window.winfo_reqwidth()
       window_height = window.winfo_reqheight()

       # Calculate position
       position_top = int(screen_height / 2 - window_height / 2)
       position_right = int(screen_width / 2 - window_width / 2)

       # Position the window
       window.geometry("+{}+{}".format(position_right, position_top))



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
              if (len(options) > 1): # If there are multiple options, show multiple options.
                     showContinue = False
                     pictureFrame.pack(side="top", fill="both", expand= True)
                     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="#A7885C", highlightthickness=2, padx=5, pady=5, height=300) # Container for the chat which includes dialogue and continue buttons
                     chatFrame.pack(side="bottom", fill="both", expand=FALSE)
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
                                   print(NPC.getAffectionLevel()) 
                            optionButton = Button(chatFrame, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda idx=option: [updateCurrentIndex(idx.get("nextSceneIndex"), idx.get("affection").get("affectedNPC"), idx.get("affection").get("change")), updateDialogue()], padx=2, pady=6)
                            optionButton.pack(side = "top", fill=X, padx=50, pady=10, expand=FALSE)
              else:
                     pictureFrame.pack(side="top", fill="both")
                     showContinue = True
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
              if(showContinue):
                     chatButton = Button(chatButtonContainer, text='Continue >>', borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=continueDialogue, padx=2, pady=2)
                     chatButton.pack(side="bottom")
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
       currentIndex:int = 0
       return updateDialogue()

from tkinter import *


def main():
    window = Tk()
    window.title('SUTDoki')
    window.minsize(1080, 720)  # set a minimum size for the window

    # Get screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Update idle tasks to get updated window size
    window.update_idletasks()

    # Get window size
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # Calculate position
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)

    # Position the window
    window.geometry("+{}+{}".format(position_right, position_top))

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
     

if __name__ == '__main__':
       main()



