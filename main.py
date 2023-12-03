# Type "python main.py" without the " " in the terminal to run this project. ctrl + ` to open the terminal.
# Only need to add more scenes using txtImgOptNameSndAff function. Guide to use is below.
import warnings
import winsound
from tkinter import *

from adamcmith import *
from classes import *
from jungcook import *
from xiaoming import *
from johnnysin import *

warnings.filterwarnings('ignore')

# Create your characters here, e.g. Xiao Ming => XIAOMING = NPC("Xiao Ming")
# Already created for you guys, just edit the name if you want
#yuchuan testing stuff
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
       shadow1 = Label(window, text=characterName, background="#1f1f1f", foreground="black", font=("roboto", 32), padx=6, pady=6)
       shadow1.place(in_=chatFrame, x=xLocation+5, y=-35)
       shadow2 = Label(window, text=characterName, background="#2e2e2e", foreground="black", font=("roboto", 32), padx=6, pady=6)
       shadow2.place(in_=chatFrame, x=xLocation+4, y=-36)
       shadow3 = Label(window, text=characterName, background="#3b3a3a", foreground="black", font=("roboto", 32), padx=6, pady=6)
       shadow3.place(in_=chatFrame, x=xLocation+3, y=-37)
       nameLabelFrame = Label(window, text=characterName, background="#d1aa73", foreground="black", font=("roboto", 32), padx=5, pady=5, highlightbackground="#A7885C", highlightthickness=2)
       nameLabelFrame.place(in_=chatFrame, x=xLocation, y=-40)

def cleanUp(afterIds:list, dialogueContainer:Label, storyFrame:Frame):
       winsound.PlaySound(None, winsound.SND_PURGE)
       for afterId in afterIds:
              dialogueContainer.after_cancel(afterId)       
       for widget in storyFrame.winfo_children():
              widget.destroy() 

def create_button_hover_effect(button, bg_normal='#d1aa73', bg_hover='#A7885C'):
       def on_enter(e):
              button.config(bg=bg_hover)
       def on_leave(e):
              button.config(bg=bg_normal)
       button.bind("<Enter>", on_enter)
       button.bind("<Leave>", on_leave)

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
                     xiaomingScenes = []
                     for i in XIAO_MING(name):
                            listy = {1:'',2:'',3:[],4:None,5:None,6:None}
                            length = len(i)
                            for j in range(1, length + 1):
                                   listy[j] = i[j - 1]
                            xiaomingScenes.append(txtImgOptNameSndAff(listy[1], listy[2], listy[3], listy[4], listy[5], listy[6]))
                     xiaomingStartBtn = Button(selectFrame, text=XIAOMING.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", activebackground="#A7885C", foreground="black", font=("roboto", 20), command=lambda:createScenes(window, selectFrame, xiaomingScenes), padx=2, pady=2)
                     xiaomingStartBtn.grid(row=row, column=column+2, sticky=N+E+W+S, padx=10, pady=10)
                     create_button_hover_effect(xiaomingStartBtn)
                     xiaomingDescription = Label(selectFrame, text="Shy yet sporty tech student\n\n-Introverted coder\n\n-Confident athlete\n\n-Uses his tech prowess \nto solve challenges\n\nJoin him on his journey from \nnovice coder to top tech expert", bg="#8cb9ed", font=("Comic Sans MS", 15))
                     xiaomingDescription.grid(row=row, column=column+3, sticky=W+E)

              elif NPC == JUNGCOOK:
                     jungcookScenes = []
                     for i in JC(name):
                            listy = {1:'',2:'',3:[],4:None,5:None,6:None}
                            length = len(i)
                            for j in range(1, length + 1):
                                   listy[j] = i[j - 1]
                            jungcookScenes.append(txtImgOptNameSndAff(listy[1], listy[2], listy[3], listy[4], listy[5], listy[6]))
                     jungcookStartBtn = Button(selectFrame, text=JUNGCOOK.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", activebackground="#A7885C", foreground="black", font=("roboto", 20), command=lambda:createScenes(window, selectFrame, jungcookScenes), padx=2, pady=2)
                     jungcookStartBtn.grid(row=row, column=column+2, sticky=N+E+W+S, padx=10, pady=10)
                     create_button_hover_effect(jungcookStartBtn)
                     jungcookDescription = Label(selectFrame, text="-Fiery Korean chef with a tsundere personality\n\n-Known as the 'Korean Gordon Ramsey'\n\n-Despite his tough exterior, he has a\nsoft spot for those he cares about.\n\n-Uses his culinary prowess to create\nmouth-watering dishes that leave everyone in awe.\n\nJoin him on his journey from being a\nrenowned chef to the star of the Prom night", bg="#ed8ce0",font=("Comic Sans MS", 15))
                     jungcookDescription.grid(row=row, column=column+3, sticky=W+E)

              elif NPC == ADAMCMITH:
                     adamcmithScenes = []
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
                            adamcmithScenes.append(txtImgOptNameSndAff(textls, picls, third, fourth, fifth, sixth))
                     adamcmithStartBtn = Button(selectFrame, text=ADAMCMITH.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", activebackground="#A7885C", font=("roboto", 20), command=lambda:createScenes(window, selectFrame, adamcmithScenes), padx=2, pady=2)
                     adamcmithStartBtn.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     create_button_hover_effect(adamcmithStartBtn)
                     adamcmithDescription = Label(selectFrame, text="Your childhood friend with a heart of gold.\n\n-A familiar face from your past,\nalways there in your memories.\n\n-Always there when you need him.\n\nDespite the time that's passed,\nyour bond with him remains strong.\n\n-He is a constant source of support and companionship.\n\nJoin him on a journey of reconnection,\nfrom accidental encounters to shared memories.",bg="#8ced8f", font=("Comic Sans MS", 15))
                     adamcmithDescription.grid(row=row, column=column+2, sticky=W+E)

              elif NPC == JOHNNYSIN:
                     affection_score = 0
                     TOO_LOW_AFFECTION = -10
                     NORMALLY_HIGH_AFFECTION = 10
                     SUPER_HIGH_AFFECTION = 20
                     ABNORMALLY_LOW_AFFECTION = -20
                     def update_affection(change):
                            global affection_score
                            if change == "INCREASE":
                                   affection_score += 1
                            elif change == "DECREASE":
                                   affection_score -= 1
                     def determine_ending(affection_score):
                            if affection_score <= ABNORMALLY_LOW_AFFECTION:
                                    return "abnormally_low_ending"
                            elif affection_score <= TOO_LOW_AFFECTION:
                                   return "too_low_ending"
                            elif affection_score < NORMALLY_HIGH_AFFECTION:
                                   return "normal_ending"
                            elif affection_score < SUPER_HIGH_AFFECTION:
                                    return "high_affection_ending"
                            else:
                                   return "super_high_affection_ending"

                     def end_game(affection_score):
                            ending = determine_ending(affection_score)
                            if ending == "abnormally_low_ending":
                                   show_abnormally_low_ending()
                            elif ending == "too_low_ending":
                                   show_too_low_ending()
                            elif ending == "normal_ending":
                                   show_normal_ending()
                            elif ending == "high_affection_ending":
                                   show_high_affection_ending()
                            elif ending == "super_high_affection_ending":
                                   show_super_high_affection_ending()

                           
                     def show_abnormally_low_ending():
                            return ([txtImgOptNameSndAff("(HI)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav")])
                     

                     def show_too_low_ending():
                             return ([txtImgOptNameSndAff("(HI)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav")])
                     

                     def show_normal_ending():
                             return ([txtImgOptNameSndAff("(HI)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav")])
                     

                     def show_high_affection_ending():
                             return ([txtImgOptNameSndAff("(HI)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav")])
                     

                     def show_super_high_affection_ending():
                             return ([txtImgOptNameSndAff("(HI)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav")])
                     
                     chatButton4 = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda i=i :createScenes(window, selectFrame,
                     [txtImgOptNameSndAff("(Day 1 You're buried in books at the SUTD library, preparing for your final exams.)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", "pictures/libraryjohnny2.png", [2], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/libraryjohnny2.png", [{"text": "Sure, the architecture section is that way. \n But beware, the librarian is a stealthy guardianSure, the architecture section is that way. \n But beware, the librarian is a stealthy guardian.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Can't you see I'm trying to decode the mysteries of the universe here? Ask Google, my friend", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Absolutely, fellow adventurer! Let's embark on this scholarly quest together. \n Post-exams, we can explore the real deal!", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}]),    
                     txtImgOptNameSndAff("Intriguing! Im digging this blend of modern and traditional vibes. Whats your major", "pictures/libraryjohnny2.png", [4],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("I'm prepping for my final exams. It's a bit overwhelming.", "pictures/libraryjohnny3.png", [5],"You", "xm2.wav"),
                     txtImgOptNameSndAff("Maybe after your exams, you could show me around the city's architectural highlights?", "pictures/libraryjohnny3.png", [6],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/libraryjohnny2.png", [{"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "A quest for later. Now, I must return to my study dungeon.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("That sounds like a plan. It would be a nice break from all this studying.", "pictures/libraryjohnny3.png", [8], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(The conversation flows smoothly, and you're both surprised at how comfortable you feel around each other. Johnny's charm and your shared interest in architecture make for a promising start.)", "pictures/libraryjohnny3.png", [10]),
                     txtImgOptNameSndAff("(Day2 The next morning in SUTD track in the late afternoon.)", "pictures/trackjohnny2.png", [11], "sounds/animalese.wav"),
                     txtImgOptNameSndAff("Hey, I noticed you yesterday at the library. I'm going for a run. Care to join me? It's a great way to unwind.", "pictures/trackjohnny1.png", [12], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/trackjohnny1.png", [{"text": "I'm not much of a runner, but why not? It might be fun. Running at sunset sounds perfect.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Running with the setting sun? Tempting, but my brain cells need me more.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "Chasing sunsets? Running isn't really my thing. I'm more of a moonlight wanderer. Go away boi", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("Trust me, the view at sunset is worth it. Plus, I could use the company.", "pictures/trackjohnny1.png", [14],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("(During the run) Look at that sunset! It's like the sky's putting on a show just for us.", "pictures/sunsetjohnny2.png", [15],"Johnny Sin", "sounds/animalese.wav"),
                     txtImgOptNameSndAff("", "pictures/sunsetjohnny2.png", [{"text": "It's beautiful. I never took the time to appreciate it like this.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It is nice. But let's not stop; we should keep our pace.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Honestly, I'm just here so I don’t get fined for skipping leg day", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Back home, moments like these are rare. I'm glad I got to share it with you.", "pictures/sunsetjohnny2.png", [17],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Me too, Johnny. This was unexpectedly enjoyable.", "pictures/sunsetjohnny2.png", [17], "You", "sounds/xm2.wav"), 
                     txtImgOptNameSndAff("(The run turns into a fun and light-hearted experience. Your laughter echoes in the cool evening air, and the shared moment at sunset feels special.)", "pictures/eveningjohnny1.png", [18]),
                     txtImgOptNameSndAff("(Day 3 Today I have Art class, with an assignment to draw a portrait.)", "pictures/classroomjohnny1.png", [19], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("I've been thinking about the assignment, and I would like to draw your portrait. Would that be okay with you?", "pictures/classroomjohnny2.png", [20], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/classroomjohnny2.png", [{"text": "Me? Well, that's quite the compliment. That sounds like fun! I've always wanted to be someone's muse.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I guess that's fine. But I'm no Venus de Milo. Just dont expect a masterpiece.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I'm not really comfortable being your subject, sorry.Me? \n Why not draw the cafeteria lady instead? She's got character", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("You have a certain...expression, it's captivating. Like the Mona Lisa.", "pictures/monalisa.png", [22],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("That's quite the compliment. I guess I can't say no to being compared to a masterpiece.", "pictures/monalisa.png", [23], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(While drawing) You know, this reminds me of a scene from Titanic. Minus the drama, of course.", "pictures/classroomjohnny2.png", [24],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/classroomjohnny2.png", [{"text": "Well, let's keep it that way. No icebergs in Singapore, thankfully.", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just make sure you get my good side!", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope you're better at drawing than making movie references. \n Keep the charm, Picasso. Lets not turn this into a meme", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Just a sunny island with a sunny girl.", "pictures/classroomjohnny2.png", [26],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("(The session is filled with playful banter. Johnny's focus on capturing your essence is flattering, and the mood is reminiscent of a classic romantic movie.)", "pictures/classroomjohnny1.png", [27]),
                     txtImgOptNameSndAff("(Day 4 Sports stadium, buzzing with excitement.)", "pictures/stadiumjohnny1.png", [28], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("I'm really glad you came. Your support means a lot to me.", "pictures/stadiumjohnny2.png", [29], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/stadiumjohnny2.png", [{"text": "I wouldn't miss it. Seeing you run is inspiring. I brought a banner to cheer you on. Go Johnny!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I'm curious to see how fast you run. Good luck!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I just hope it doesn't drag on too long.", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("Just knowing you're here in the crowd makes me want to run faster.", "pictures/stadiumjohnny2.png", [31],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/stadiumjohnny2.png", [{"text": "Well, then I expect nothing less than a win from you!", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just focus on your race. Don’t worry about the crowd.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope this doesnt take too long. Ive got a date with Netflix later.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("(The energy of the competition is electric. As Johnny races, you find yourself fully invested in his success. His win feels like a shared victory.)", "pictures/stadiumjohnny3.png", [33]),
                     txtImgOptNameSndAff("(Day 5 Changi City Point mall, bustling with activity.)", "pictures/ccp1.png", [34], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("This mall is huge! Where should we start?", "pictures/ccp2.png", [35], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/ccp2.png", [{"text": "How about some window shopping? There are some great clothing stores here.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Maybe grab a bite first? I'm a bit hungry.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Navigating through crowds? That's a hard pass. Got a teleporter handy?", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's explore together and find the best spot in CCP!", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
                     txtImgOptNameSndAff("Sounds good. Maybe you can help me pick out something that screams 'Singapore'!", "pictures/ccp2.png", [37],"Johnny Sin", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(In a café) This coffee is great, but not as sweet as your company.", "pictures/cafejohnny1.png", [38],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/cafejohnny1.png", [    {"text": "Smooth line, Johnny. Been practicing?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "You and your compliments! But thanks, the coffee is good.", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "BRUH are you always this cheesy?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Maybe a little. But only the best for today.", "pictures/cafejohnny1.png", [40],"Johnny Sin", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(Before the movie) I'm glad we did this. Today was perfect.", "pictures/cafejohnny1.png", [41],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Me too, Johnny. It's nice to just relax and enjoy the day.", "pictures/cafejohnny1.png", [42], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(The day is a mix of casual shopping, sipping coffee, and watching a movie. It's comfortable and easy, with a hint of budding romance.)", "pictures/cafejohnny1.png", [43]),
                     txtImgOptNameSndAff("(Day 6 University observatory, under a starlit sky.)", "pictures/star1.png", [44], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("These stars... they're like nothing I've seen back home.", "pictures/star1.png", [45], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "They have a way of making everything seem so possible, so magical.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Yeah, it's a clear night. Perfect for star-gazing.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "I'm more of a city lights person, but this is okay.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},    {"text": "It's like they're shining just for us tonight.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
                     txtImgOptNameSndAff("You know, I've been meaning to tell you something. These past few days with you have been the highlight of my trip.", "pictures/star1.png", [47],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Really? I've enjoyed our time together too.", "pictures/star1.png", [48], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("I feel like there's something special between us. I know my time here is limited, but I had to let you know.", "pictures/star1.png", [49],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "Johnny, I feel it too. Let's just enjoy this moment, under the stars.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "That's really sweet, Johnny. I'm glad we met.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Easy there, cowboy. We are just two astronauts on a space walk.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("(The night is filled with heartfelt confessions and quiet understanding. The stars above seem to bless this new, uncertain yet hopeful chapter in your lives.)", "pictures/star1.png", [51]),
                     txtImgOptNameSndAff("(Day 7 A quiet spot on campus, preparing to say goodbye.)", "pictures/sutdscene.png", [52], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("This week with you has been the best part of my exchange. I wish it didn't have to end.", "pictures/sutdscene.png", [53], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/sutdscene.png", [{"text": "I feel the same way, Johnny. This week was unforgettable.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It's been great, hasn't it? We made some good memories.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "All good things come to an end, rollercoasters are fun, but eventually, you have to get off", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's make a promise to see each other again, no matter what.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"), 
                     txtImgOptNameSndAff("I hope we can keep in touch. Maybe you could visit me in the States someday?", "pictures/sutdscene.png", [55],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/sutdscene.png", [{"text": "I'd like that. It's not goodbye, just see you later.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Sure, we can try to stay in touch. Who knows what the future holds?", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "It's hard to make such promises, Johnny. But let's enjoy today.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff( "It's been an amazing week, Johnny Sin. Thanks for sharing it with me.", "pictures/sutdscene.png", [57], "You", "sounds/justforfun.wav"),
                     txtImgOptNameSndAff( end_game(affection_score), "pictures/sutdscene.png", [57], "You", "sounds/justforfun.wav"),
                     end_game(affection_score)]))
                     

                     chatButton4.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     
                     description4 = Label(selectFrame, text="An exchange student from the USA with\na heart as warm as his home state.\n\nHis charm lies in his adventurous spirit\nand his willingness to immerse\nhimself in new experiences.\n\n-Johnny's enthusiasm is infectious\n\n-He brings a touch of foreign intrigue\nand a lot of friendly warmth.\n\nJoin him on his journey of cultural exchange.", bg="#ed8c8c",font=("Comic Sans MS", 15))
                     description4.grid(row=row, column=column+2, sticky=W+E)
                     johnny_dialogues = []
                     
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
       winsound.PlaySound(None, winsound.SND_PURGE)
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
                                   
                            
                            optionButton = Button(chatFrame, text=option['text'], borderwidth=1, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda idx=option: [updateCurrentIndex(idx.get("nextSceneIndex"), idx.get("affection").get("affectedNPC"), idx.get("affection").get("change")), updateDialogue()], padx=2, pady=6, activebackground="#A7885C")
                            optionButton.pack(side = "top", fill=X, padx=50, pady=5, expand=FALSE)
                            create_button_hover_effect(optionButton)
              else:
                     pictureFrame.pack(side="top", fill="both")
                     showContinue = True
                     chatFrame = Frame(storyFrame, background="#d1aa73", border="2", highlightbackground="#A7885C", highlightthickness=2, padx=5, pady=5, height=300) # Container for the chat which includes dialogue and continue buttons
                     chatFrame.pack(side="bottom", fill="both", expand=TRUE)
              if (name != None and len(name) > 0):
                     createNameFrame(window, chatFrame, name)
              dialogueContainer = Label(chatFrame, text="", height=0, wraplength=1100, justify=LEFT, background="#d1aa73", foreground="black", font=("roboto", 24), padx=50, pady=20)
              dialogueContainer.pack(side="left")
              dialogueContainer.config(text="")
              afterIds.clear()
              for i, word in enumerate(dialogue): # Creates the text effect
                     def updateText(w=word):
                            currentText = dialogueContainer.cget("text")
                            dialogueContainer.configure(text=currentText + w)
                     afterId = dialogueContainer.after(20 * i, updateText) # Logs the afterId so I can stop it from running when I go to the next scene
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
                     chatButton = Button(chatButtonContainer, text='Continue >>', font=("roboto", 24), borderwidth=2, background="#d1aa73", foreground="black", command=continueDialogue, padx=2, pady=2, activebackground="#A7885C")
                     chatButton.pack(side="bottom")
                     def onEnter(e):
                            chatButton.config(bg='#A7885C')
                     def onLeave(e):
                            chatButton.config(bg='#d1aa73')
                     chatButton.bind("<Enter>", onEnter)
                     chatButton.bind("<Leave>", onLeave)
                     
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


def main():
    window = Tk()
    window.title('SUTDoki')
    window.minsize(1280, 720)  # set a minimum size for the window

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

    winsound.PlaySound("sounds/justforfun.wav", winsound.SND_ASYNC)
    # Load background image for start menu
    bg_photo = PhotoImage(file='pictures/start_menu_bg3.png')
    bg_label = Label(window, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Create a frame to hold the start menu widgets
    start_menu_frame = Frame(window, bg='#d1aa73', highlightbackground="#A7885C", highlightthickness=4)
    start_menu_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    # Create a label for the game title
    title_label = Label(start_menu_frame, text="SUTDoki", bg='#d1aa73', font=('Comic Sans MS', 48))
    title_label.pack(pady=20)

    # Create an entry for the player to input their name
    name_label = Label(start_menu_frame, text="What's your name?", bg='#d1aa73', font=('Comic Sans MS', 24), padx=2)
    name_label.pack()
    name_entry = Entry(start_menu_frame, font=('Comic Sans MS', 24))
    name_entry.pack(padx=10, pady=10)

    NPClist = [JOHNNYSIN,JUNGCOOK,ADAMCMITH,XIAOMING]
    photoList = [
           PhotoImage(file="pictures/johnnysin_profile_resized2.png"),
           PhotoImage(file="pictures/JC/JCPP.png"),
           PhotoImage(file="pictures/dog.png"),
           PhotoImage(file="pictures/dog.png")
    ]

    # Create the start button
    start_button = Button(start_menu_frame, text="Start Story", font=('Roboto', 24), bg='#d1aa73', activebackground="#A7885C", command=lambda: 
            [protagonist.setName(name_entry.get()), showSelectNPCWindow(window, start_menu_frame, name_entry.get(), NPClist, photoList)])
    start_button.pack(pady=20, expand=TRUE)
    create_button_hover_effect(start_button)
    window.attributes("-fullscreen", True)
    window.bind("<F11>", lambda event: window.attributes("-fullscreen",
                                   not window.attributes("-fullscreen")))
    window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))
    show_toast("Press F11 to toggle Fullscreen\nPress Escape to exit Fullscreen")
    window.mainloop()

def show_toast(message, duration=3000):  # Duration in milliseconds
    toast = Toplevel()
    toast.overrideredirect(1)

    # Get screen width and height
    screen_width = toast.winfo_screenwidth()
    screen_height = toast.winfo_screenheight()

    # Specify dimensions of the toast
    toast_width = 450
    toast_height = 75

    # Calculate position to center the toast
    position_top = int(0)
    position_right = int(screen_width / 2 - toast_width / 2)

    toast.geometry(f"{toast_width}x{toast_height}+{position_right}+{position_top}")

    toast.after(duration, toast.destroy)
    Label(toast, text=message, bg="black", fg="white", font=("Helvetica", 25)).pack()
     

if __name__ == '__main__':
       main()


