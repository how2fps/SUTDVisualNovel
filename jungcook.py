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

def createScenes(window: Tk, currentFrame: Frame, textImgNameSound: list):
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

def JC(name):
       diag = [["Day 1", "pictures/dog.png", [1]], 
       ["Haiz, why does uni have to be so hard. Why can't the proffessor just give everyone passes", picmain, [2], name, "sounds/animalese (1).wav"],
       ["(As you are heading back dorm, you smelt an amazing scent coming from the kitchen)", picmain, [3]],
       ("(Curiosity got the better of you as you decide to check it out.)", picmain, [4]),
       ("(This seems to be some short of event happenning in the common kitchen)", pic, [5]),
       ("(Thinking about it now, aren't the grub club in charge of the dessert aspect of the Prom.)", picmain, [6]),
       ("Maybe I can sneak a peek at what dessert will be at prom in advanced!!", picmain, [7], name, "sounds/animalese (1).wav"), 
       ("(As you are trying to see through the crowd to see what food they are preparing, a shadow can be seen creeping up behind her)", pic, [8], "scary sound?"),
       ("Oi!! What are you doing ?!?", pic, [9], "JungCook", "sounds/animalese (1).wav"),
       ("(Wah!! Shit scared the hell outta me.)", picmain, [10], "scary sound?"),
       ("(Who is the annoying guy spoiling my business!!!)", picmain, [11]),
       ("(You turn around to see a tall handsome man with curly hair)", picofJC, [12], "wow sounds??"),
       ("(OMG itss JungCook!!!)", picmain, [13]),
       ("(You might be wondering why the Grub Club was in charge of the dessert for Prom)", pic, [14]),
       ("(It is all because of this one man! JungCook is from a renowned family of chef, he also has an impressive history of winning multiple competitions. He is the star chef of SUTD)", picofJC, [15]),
       ("(JungCook has specially requested to help with the Prom dessert, with his reputation, no one would refuse his proposition!)", picofJC, [16]),
       ("Hellooo, did you not hear me. WHAT ARE YOU DOING HERE!!!", picofJC, [17], "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("O nothing im just here chilling randomly outside a window, for no apparent reason, just ignore me. ", picmain, [20], "sounds/animalese (1).wav"),
       ("Okay weirdo, give me a reason why I shouldn’t just report you for suspicious activity huh.", picofJC, [21], "sounds/animalese (1).wav"),
       ("Because of that UFO over there", picmain, [22], "sounds/animalese (1).wav"),
       ("(As JungCook turns around, you immediately ran away.)", picmain, [23]),
       ("What the!?? What a interesting lady she is.", picofJC, [28], "sound"),
       ("(You stare at JungCook for awhile before turning and walking away)", picmain, [25]),
       ("????????", picofJC, [28]),
       ("O i'm just curious about what they are cooking ", picmain, [27], "sounds/animalese (1).wav"),
       ("If you are curious about cooking, how about you pay attention to our grub club telegram rather than stand outside like a weirdo", picofJC, [28], "sounds/animalese (1).wav"),
       ("WTF?!!??", picmain, [28], "sounds/animalese (1).wav"),
       ("Day End", picofmoon, [29]),
       ("Day 2 ", picofsun, [30]),
       ("(You just finished the last lesson of the day and is walking with your friend)", [31]),
       ("Ahhh im stravinggg, wanna go eat gom-gom, canteen getting kinda boring", picmain, [32], "sounds/animalese (1).wav"),
       ("Sorry sis, i got project meeting right now. Have fun, CHAO!", "shadow human pic", [33], "sounds/animalese (1).wav"),
       ("Everyday project, haiz guess im going gom-gom alone", picmain, [34], "sounds/animalese (1).wav"),
       ("(Reaches Gom-Gom)", "pic of gomngom", [35]),
       ("Didn’t expect gom-gom to have such a long queue today.", picmain, [35], "sounds/animalese (1).wav"),
       ("(As you are queuing you hear a male voice behind you talking loudly, you turn around to realise that it was JungCook and as you saw him, he saw you as well)", [36]),
       ("Huh didn’t expect to see you here again suspicious woman", picofJC, [37], "sounds/animalese (1).wav"),
       ("Nice to see you too!! Why can't you just say hello like normal people", picmain, [38], "sounds/animalese (1).wav"),
       ("And just to clarify I wasn’t being weird I just happen to be there when you arrive ", picmain, [39], "sounds/animalese (1).wav"),
       ("Whatever", picofJC, [40], "sound"),
       ("O what a sweet couple, we happen to have a promotion where you can get 2 sandwiches for 50%% off would you two like to share this?", picofshadow, [41], "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "I will TAKE TWO FOR MYSELF", "nextSceneIndex": 42, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "No thanks", "nextSceneIndex": 46}, {"text": "Clarify the relationship", "nextSceneIndex": 55, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("NOOO!!! I will take two chicken sandwichesss for myself, such a good offer", picmain, [43], "sounds/animalese (1).wav"),
       ("(JungCook rolling his eyes at your response)", picofJC, [44]),
       ("I will just have a avocado bowl thanks", picofJC, [45], "sounds/animalese (1).wav"),
       ("(As you are waitin for the food, JungCook starts having casual chat with you about school project as well as assignments, a friendship has started to form.)", [59]),
       ("O no thanks, I will just have a chicken sandwich that’s all", picmain, [47], "sounds/animalese (1).wav"),
       ("Give me on avocado bowl thanks", picofJC, [48], "sounds/animalese (1).wav"),
       ("(As you are waiting for the food to be prepared)", [49]),
       ("You know you couldve ordered 2 chicken sandwich and split it with me, I wouldn’t have mind", picofJC, [50], "sounds/animalese (1).wav"),
       ("I didn’t want to them to get the wrong idea that we are dating, we just met recently afterall. ", picmain, [51], "sounds/animalese (1).wav"),
       ("We could be friends tho since we happened to meet coincidentally again so soon.", picmain, [52], "sounds/animalese (1).wav"),
       ("Sure im JungCook im sure you already know who I am", picofJC, [53], "sounds/animalese (1).wav"),
       ("Ahha I do know you, im {}, Nice to know you.".format(name), picmain, [54], "sounds/animalese (1).wav"),
       ("(After chatting while waiting for food, you left after taking your order. A new friendship was form)", [59]),
       ("O no no no we aren't dating, he is just a random guy I met yesterday", picmain, [56], "sounds/animalese (1).wav"),
       ("As If my standards would be so low, I rather date a cow then her.", picofJC, [57], "sounds/animalese (1).wav"),
       ("Heyyyyy!!! Rude much", picmain, [58], "sounds/animalese (1).wav"),
       ("(You ordered a chicken sandwich and left after receiving it, you did not bother interacting with JungCook in anyway)", [59]),
       ("Day End", picofmoon, [60]),
       ("Day 3", picofsun, [70], "sound"),
       ("(After lesson, you decided that studying in dorm was unproductive hence you decided to visit the library)",[71]),
       ("Woah the library is surprisingly full today", picmain, [72], "sounds/animalese (1).wav"),
       ("(As you are trying to find a seat, you spotted JungCook sitting alone in a corner, you also saw your group of friends sitting at the other side)", picmain, [73]),
       ("(You decided to approach JungCook)", [74]),
       ("Hi JC, I see you are reading a recipe book, is it so you can prepare me dinner?? ", picmain, [75], "sounds/animalese (1).wav"),
       ("very funny. As you know im in charge of the dessert portion of the prom, I need to find a good dessert option for the day, something easy yet delicious. ", picofJC, [76], "sounds/animalese (1).wav"),
       ("Haiz, here I thought you would be treating your dear friend to your cooking.", pic, [77], "sounds/animalese (1).wav"),
       ("One day one day I will cook for you.", picofJC, [78], "sounds/animalese (1).wav"),
       ("Anyways JC seriously?? Is that suppose to be my name?", picofJC, [79], "sounds/animalese (1).wav"),
       ("Ya, JungCook short form would be JC, such a good nickname", picmain, [80], "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Join JungCook to study", "nextSceneIndex": 81, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Join your classmate ", "nextSceneIndex": 86}, {"text": "Joke with him", "nextSceneIndex": 89, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("ANYWAYS NO GOING BACK ON YOUR WORDS, THAT WAS A PROMISE TO COOK ME A MEAL", picmain, [82], "sounds/animalese (1).wav"),
       ("Anyways mind if I sit here.", picmain, [83], "sounds/animalese (1).wav"),
       ("Nope", picofJC, [84], "sounds/animalese (1).wav"),
       ("(You proceeded to study, as time pass you and JC had more conversation throughout the sessions until you have to leave for your project meeting)", [85]),
       ("See you soon JC, I will wait for your treat", picmain, [93], "sounds/animalese (1).wav"),
       ("Ok see you next time then, imma go study with my classmate", picmain, [87], "sounds/animalese (1).wav"),
       ("Ok see you", picofJC, [88], "sounds/animalese (1).wav"),
       ("(You study with your friends until you had to leave)", [93]),
       ("Anyways, you should stop reading more recipe, you seem rounder today", picmain, [90], "sounds/animalese (1).wav"),
       ("Excuse me! I dare you to say that again.", picofJC, [91], "sounds/animalese (1).wav"),
       ("Jeez i'm just kidding, why gotta be so defensive", picmain, [92], "sounds/animalese (1).wav"),
       ("(You then go to study with your friend)", picmain, [93], "sounds/animalese (1).wav"),
       ("Day End", picofmoon, [94]),
       ("Day 4", picofsun, [95]),
       ("God dammit why is this assignment so hard!!", picmain, [96], "sounds/animalese (1).wav"),
       ("(Looking at your phone you realise that you has been studying for 8 hours straight and that it is now 3am)", picmain, [97]),
       ("I need to sleep if not I will miss tomorrow classes.", picmain, [98], "sounds/animalese (1).wav"),
       ("(As you are standing up, you suddenly hear a rumbling noise from your stomach.)", picmain, [99]),
       ("Hmm I guess I will go to the pantry and get a snack.", picmain, [100], "sounds/animalese (1).wav"),
       ("(You proceeded to the pantry)", [101]),
       ("Hmm what snack should I pick???", picmain, [102], "sounds/animalese (1).wav"),
       ("You shouldn’t eat snack so late at night you know, it's bad for your health.", picshadow, [103], "sounds/animalese (1).wav"),
       ("O god, O is just you JC, scared the hell outta me", picmain, [104], "sounds/animalese (1).wav"),
       ("I have no choice man, I'm hungry and there isn’t anything for me to eat. If it's so unhealthy, why are you here as well", picmain, [105], "sounds/animalese (1).wav"),
       ("Please, does it look like I need to buy snacks? I'm the best chef here, when I'm hungry I can just cook myself a delicacy.", picofJC, [106], "sounds/animalese (1).wav"),
       ("Which is why I'm here, I'm was planning to cook a simple meal before I sleep.", picofJC, [107], "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Doubt Him", "nextSceneIndex": 108, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Agree with him", "nextSceneIndex": 125}, {"text": "Cooking is EZ", "nextSceneIndex": 133, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Huhh best chef, when did you get that title, I don’t believe you. Unlesssss I get to taste the food you cook.", picmain, [109], "sounds/animalese (1).wav"),
       ("Tsk I don’t need your approval however my title and honour as the best chef In SUTD will not tolerate any insults. ", picofJC, [110], "sounds/animalese (1).wav"),
       ("Prepared to be blown away, food will never taste the same again.", picofJC, [111], "sounds/animalese (1).wav"),
       ("Ya right, prove me wrong", picmain, [112], "sounds/animalese (1).wav"),
       ("(Hehe free food from the chef JungCook himself WORTHHH!!!!)", picmain, [113]),
       ("(JC was indeed an amazing chef, with his fast movement and precision knife work, he was able to make ingredients the way he wanted it.)", [114]),
       ("(It looks so simple yet complex at the same time. Looking at him work, it was like watching a performance)", [115]),
       ("(This didn’t last long as JC quickly prepared a simple dish of egg fried rice)", [116]),
       ("Wow that was fast!", picmain, [117], "sounds/animalese (1).wav"),
       ("Of Course, a good chef does not keep his customers hungry", picofJC, [118], "sounds/animalese (1).wav"),
       ("Now for the main judging", picmain, [119], "sounds/animalese (1).wav"),
       ("O wow, this is delicious.", picmain, [120], "sounds/animalese (1).wav"),
       ("I mean hmm its acceptable, better than most fried rice I've tasted ", picmain, [121], "sounds/animalese (1).wav"),
       ("Don’t try to deny it, your action has already betrayed your words.", picofJC, [122], "sounds/animalese (1).wav"),
       ("You can eat it slowly, I cooked more than one persons worth. Enjoy!!", picofJC, [123], "sounds/animalese (1).wav"),
       ("Thadwadnkss", picmain, [124], "sounds/animalese (1).wav"),
       ("(You enjoyed yourself and thanked JC, you went to sleep)", [137]),
       ("Well good for you that you know how to cook, I’ve never had any chance or time to learn cooking. ", picmain, [126], "sounds/animalese (1).wav"),
       ("Maybe one day I will ask you to teach me how to cook.", picmain, [127], "sounds/animalese (1).wav"),
       ("No problem, just hit me up and I will teach you the best cooking tutorial you have ever seen", picofJC, [128], "sound"),
       ("Anyways what are you cooking?", picmain, [129], "sounds/animalese (1).wav"),
       ("Just a simple egg fried rice, do you want some as well?", picofJC, [130], "sounds/animalese (1).wav"),
       ("If you wouldn’t mind cooking extra, I would love to have your cooking.", picmain, [131], "sounds/animalese (1).wav"),
       ("(JC nods and proceed to cook fried rice)", [132]),
       ("(You eat the fried rice with pleasure and awe, you then leave after finishing and saying goodbye)", [137]),
       ("Show off! You can cook so what, I don’t think cooking is that hard anyway.", picmain, [134], "sounds/animalese (1).wav"),
       ("Its certainly harder than you just yapping, get out of my way, I need to get my equipments.", picofJC, [135], "sounds/animalese (1).wav"),
       ("TSK this pantry aint yours.", picmain, [136], "sounds/animalese (1).wav"),
       ("(You bought snacks and leave)", [137]),
       ("Day End", picofmoon, [138]),
       ("Day 5", picofsun, [139], "sound"),
       ("(Today was a chill day, you enjoyed the peaceful moments (Affection with JungCook too low))", picmain, ['day end no'], {"NPC": JUNGCOOK, "comparison": BIGGER, "amount": 3, "altSceneIndex": 140 }),
       ("(You just finished her fifth row of volleyball training)", [141]),
       ("Good training guys, see you guys CHAOOO", picmain, [142], "sounds/animalese (1).wav"),
       ("Woo, all those workout got me famished, what do I want what do I want", picmain, [143], "sounds/animalese (1).wav"),
       ("Hmm Mcd sounds good, hmm meggi sounds amazing as well. O man how I wish I could just get both.", picmain, [144], "sounds/animalese (1).wav"),
       ("(As you are thinking about what to eat, JungCook approaches you)", [145]),
       ("O hi, JC.", picmain, [146], "sounds/animalese (1).wav"),
       ("Yo, you free now? ", picofJC, [147], "sounds/animalese (1).wav"),
       ("YASss, why?", picmain, [148], "sounds/animalese (1).wav"),
       ("Nothing much just that remember when I owe you dinner, well I’m free now to cook for you", picofJC, [149], "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "LETSS GOOOOO", "nextSceneIndex": 150, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Be Polite", "nextSceneIndex": 155}, {"text": "Reject Him", "nextSceneIndex": 159, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Letss gooooooo, I was just nice hungry after training. I will say first, I not someone with a small stomach.", picmain, [151], "sounds/animalese (1).wav"),
       ("No problem, do you know who I am? My name is Cook, JungCook.", picofJC, [152], "sounds/animalese (1).wav"),
       ("Cooking a meal for the whole school wouldn’t be an issue to me much less one person.", picofJC, [153], "sounds/animalese (1).wav"),
       ("Hahha good, I shall feast tonight then.", picmain, [154], "sounds/animalese (1).wav"),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", [164]),
       ("Oo, I was just joking hahah, I wont force you to treat me dinner.", picmain, [156], "sounds/animalese (1).wav"),
       ("No issue, I have already prepared the ingredients in advanced. You can think of it as me treating my friend to dinner. I am your friend right?", picofJC, [157], "sounds/animalese (1).wav"),
       ("Of Course, well lets go then. Thank you for the meal.", picmain, [158], "sounds/animalese (1).wav"),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", [164]),
       ("Thanks but no thanks, imma go mac.", picmain, [160], "sounds/animalese (1).wav"),
       ("Actually picking mcd over my cooking? Tsk suit urself.", picofJC, [161]), 
       ("(JungCook walk away)", [162]), 
       ("Eh whatever", picmain, [163], "sounds/animalese (1).wav"), 
       ("(You ordered mac delivery and enjoyed yourself)", [164]), 
       ("Day End", picofmoon, [165]), 
       ("Day 6", picofsun, [166]), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'),  
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound'), 
       ("", pic, [], 'sound')] 
       return diag




              
       
     