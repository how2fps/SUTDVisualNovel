

picmain = "pic of main path"
picofJC = "pic of JC path"

def JC():
       window = Tk()
       window.title('SUTDoki')
       width = 1080
       height = 720 
       ws = window.winfo_screenwidth()
       hs = window.winfo_screenheight()
       x = (ws/2) - (width/2)
       y = (hs/2) - (height/2) - 100
       window.geometry('%dx%d+%d+%d' % (width, height, x, y))

       startingFrame = Frame(window)
       startingFrame.pack(anchor=W, fill=Y, expand=False, side=LEFT)
       Label(startingFrame, text="Enter your name").pack()
       nameInput = Entry(startingFrame)
       nameInput.pack()
       def txtImgOptNameSndAff(text:str, imgFilePath: str, options: list = [], name:str = None, soundFilePath: str = None, affectionCheck: dict = None):
            return {"text": text, "imgFilePath": imgFilePath, "name": name, "soundFilePath": soundFilePath, "options": options, "affectionCheck": affectionCheck}
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
       
       textbox = Label(startingFrame, text="Starting Screen", borderwidth=2, background="#d1aa73", foreground="black", font="roboto")
       textbox.pack(side=LEFT)
       print (nameInput.get())
       # If not sure can check main for Finn examples
       # How to find out what index your dialogue is in the array: Take the current line of your array and subtract from the starting line. P.S: Put your dialogues in this vertical manner. 
       startButton = Button(startingFrame, text="Start Story", borderwidth=2, background="#d1aa73", foreground="black", font="roboto", command=lambda: 
              [protagonist.setName(nameInput.get()), (createScenes(window, startingFrame, 
              [txtImgOptNameSndAff("Day 1", "pictures/dog.png", [1]), 
              txtImgOptNameSndAff("Haiz, why does uni have to be so hard. Why can't the proffessor just give everyone passes", picmain, [2], nameInput.get(), "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As you are heading back dorm, you smelt an amazing scent coming from the kitchen)", picmain, [3]),
              txtImgOptNameSndAff("(Curiosity got the better of you as you decide to check it out.)", picmain, [4]),
              txtImgOptNameSndAff("(This seems to be some short of event happenning in the common kitchen)", "picture of kitchen", [5]),
              txtImgOptNameSndAff("(Thinking about it now, aren't the grub club in charge of the dessert aspect of the Prom.)", picmain, [6]),
              txtImgOptNameSndAff("Maybe I can sneak a peek at what dessert will be at prom in advanced!!", picmain, [7], nameInput.get(), "sounds/animalese (1).wav"), 
              txtImgOptNameSndAff("(As you are trying to see through the crowd to see what food they are preparing, a shadow can be seen creeping up behind her)", "pic of main with shadow", [8], "scary sound?"),
              txtImgOptNameSndAff("Oi!! What are you doing ?!?", "pic of shadow figure", [9], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(Wah!! Shit scared the hell outta me.)", picmain, [10], "scary sound?"),
              txtImgOptNameSndAff("(Who is the annoying guy spoiling my business!!!)", picmain, [11]),
              txtImgOptNameSndAff("(You turn around to see a tall handsome man with curly hair)", picofJC, [12], "wow sounds??"),
              txtImgOptNameSndAff("(OMG itss JungCook!!!)", picmain, [13]),
              txtImgOptNameSndAff("(You might be wondering why the Grub Club was in charge of the dessert for Prom)", [14]),
              txtImgOptNameSndAff("(It is all because of this one man! JungCook is from a renowned family of chef, he also has an impressive history of winning multiple competitions. He is the star chef of SUTD)", picofJC, [15]),
              txtImgOptNameSndAff("(JungCook has specially requested to help with the Prom dessert, with his reputation, no one would refuse his proposition!)", picofJC, [16]),
              txtImgOptNameSndAff("Hellooo, did you not hear me. WHAT ARE YOU DOING HERE!!!", picofJC, [17], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
              txtImgOptNameSndAff("O nothing im just here chilling randomly outside a window, for no apparent reason, just ignore me. ", picmain, [20], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Okay weirdo, give me a reason why I shouldn’t just report you for suspicious activity huh.", picofJC, [21], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Because of that UFO over there", picmain, [22], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As JungCook turns around, you immediately ran away.)", picmain, [23]),
              txtImgOptNameSndAff("What the!?? What a interesting lady she is.", picofJC, [28], "sound"),
              txtImgOptNameSndAff("(You stare at JungCook for awhile before turning and walking away)", picmain, [25]),
              txtImgOptNameSndAff("????????", picofJC, [28]),
              txtImgOptNameSndAff("O i'm just curious about what they are cooking ", picmain, [27], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("If you are curious about cooking, how about you pay attention to our grub club telegram rather than stand outside like a weirdo", picofJC, [28], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("WTF?!!??", picmain, [28], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Day End", picofmoon, [29]),
              txtImgOptNameSndAff("Day 2 ", picofsun, [30]),
              txtImgOptNameSndAff("(You just finished the last lesson of the day and is walking with your friend)", [31]),
              txtImgOptNameSndAff("Ahhh im stravinggg, wanna go eat gom-gom, canteen getting kinda boring", picmain, [32], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Sorry sis, i got project meeting right now. Have fun, CHAO!", "shadow human pic", [33], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Everyday project, haiz guess im going gom-gom alone", picmain, [34], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(Reaches Gom-Gom)", "pic of gomngom", [35]),
              txtImgOptNameSndAff("Didn’t expect gom-gom to have such a long queue today.", picmain, [35], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As you are queuing you hear a male voice behind you talking loudly, you turn around to realise that it was JungCook and as you saw him, he saw you as well)", [36]),
              txtImgOptNameSndAff("Huh didn’t expect to see you here again suspicious woman", picofJC, [37], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Nice to see you too!! Why can't you just say hello like normal people", picmain, [38], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("And just to clarify I wasn’t being weird I just happen to be there when you arrive ", picmain, [39], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Whatever", picofJC, [40], "sound"),
              txtImgOptNameSndAff("O what a sweet couple, we happen to have a promotion where you can get 2 sandwiches for 50%% off would you two like to share this?", picofshadow, [41], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("", picofsun, [{"text": "I will TAKE TWO FOR MYSELF", "nextSceneIndex": 42, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "No thanks", "nextSceneIndex": 46}, {"text": "Clarify the relationship", "nextSceneIndex": 55, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
              txtImgOptNameSndAff("NOOO!!! I will take two chicken sandwichesss for myself, such a good offer", picmain, [43], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(JungCook rolling his eyes at your response)", picofJC, [44]),
              txtImgOptNameSndAff("I will just have a avocado bowl thanks", picofJC, [45], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As you are waitin for the food, JungCook starts having casual chat with you about school project as well as assignments, a friendship has started to form.)", [59]),
              txtImgOptNameSndAff("O no thanks, I will just have a chicken sandwich that’s all", picmain, [47], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Give me on avocado bowl thanks", picofJC, [48], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As you are waiting for the food to be prepared)", [49]),
              txtImgOptNameSndAff("You know you couldve ordered 2 chicken sandwich and split it with me, I wouldn’t have mind", picofJC, [50], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("I didn’t want to them to get the wrong idea that we are dating, we just met recently afterall. ", picmain, [51], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("We could be friends tho since we happened to meet coincidentally again so soon.", picmain, [52], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Sure im JungCook im sure you already know who I am", picofJC, [53], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Ahha I do know you, im {}, Nice to know you.".format(nameInput.get()), picmain, [54], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(After chatting while waiting for food, you left after taking your order. A new friendship was form)", [59]),
              txtImgOptNameSndAff("O no no no we aren't dating, he is just a random guy I met yesterday", picmain, [56], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("As If my standards would be so low, I rather date a cow then her.", picofJC, [57], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Heyyyyy!!! Rude much", picmain, [58], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(You ordered a chicken sandwich and left after receiving it, you did not bother interacting with JungCook in anyway)", [59]),
              txtImgOptNameSndAff("Day End", picofmoon, [60]),
              txtImgOptNameSndAff("Day 3", picfsun, [70], "sound"),
              txtImgOptNameSndAff("(After lesson, you decided that studying in dorm was unproductive hence you decided to visit the library)",[71]),
              txtImgOptNameSndAff("Woah the library is surprisingly full today", picmain, [72], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(As you are trying to find a seat, you spotted JungCook sitting alone in a corner, you also saw your group of friends sitting at the other side)", picmain, [73]),
              txtImgOptNameSndAff("(You decided to approach JungCook)", [74]),
              txtImgOptNameSndAff("Hi JC, I see you are reading a recipe book, is it so you can prepare me dinner?? ", picmain, [75], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("very funny. As you know im in charge of the dessert portion of the prom, I need to find a good dessert option for the day, something easy yet delicious. ", picofJC, [76], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Haiz, here I thought you would be treating your dear friend to your cooking.", pic, [77], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("One day one day I will cook for you.", picofJC, [78], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Anyways JC seriously?? Is that suppose to be my name?", picofJC, [79], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Ya, JungCook short form would be JC, such a good nickname", picmain, [80], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("", picofsun, [{"text": "Join JungCook to study", "nextSceneIndex": 81, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Join your classmate ", "nextSceneIndex": 86}, {"text": "Joke with him", "nextSceneIndex": 89, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
              txtImgOptNameSndAff("ANYWAYS NO GOING BACK ON YOUR WORDS, THAT WAS A PROMISE TO COOK ME A MEAL", picmain, [82], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Anyways mind if I sit here.", picmain, [83], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Nope", picofJC, [84], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(You proceeded to study, as time pass you and JC had more conversation throughout the sessions until you have to leave for your project meeting)", [85]),
              txtImgOptNameSndAff("See you soon JC, I will wait for your treat", picmain, [93], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Ok see you next time then, imma go study with my classmate", picmain, [87], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Ok see you", picofJC, [88], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(You study with your friends until you had to leave)", [93]),
              txtImgOptNameSndAff("Anyways, you should stop reading more recipe, you seem rounder today", picmain, [90], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Excuse me! I dare you to say that again.", picofJC, [91], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Jeez i'm just kidding, why gotta be so defensive", picmain, [92], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("(You then go to study with your friend)", picmain, [93], "sounds/animalese (1).wav"),
              txtImgOptNameSndAff("Day End", picofmoon, [94]),
              txtImgOptNameSndAff("Day 4", picofsun, [95]),



              ]))])
       startButton.pack(side=RIGHT)
       window.mainloop()
     