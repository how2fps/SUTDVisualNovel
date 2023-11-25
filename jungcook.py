
from main import *

picmain = "pic of main path"
picofJC = "pic of JC path"

def main():
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
              txtImgOptNameSndAff("Day End", picofsun, [29]),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),
              txtImgOptNameSndAff("", pic, [], "sound"),

              ]))])
       startButton.pack(side=RIGHT)
       window.mainloop()
     

if __name__ == '__main__':
       main()