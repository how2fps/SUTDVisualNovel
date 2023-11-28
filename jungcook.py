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
picofgomgom = "pictures/dog.png"
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

def JC(name):
       diag = [["Day 1", "pictures/dog.png", [1]], 
       ["Haiz, why does uni have to be so hard. Why can't the proffessor just give everyone passes", picmain, [2], name, "sounds/animalese (1).wav"],
       ["(As you are heading back dorm, you smelt an amazing scent coming from the kitchen)", picmain, [3]],
       ("(Curiosity got the better of you as you decide to check it out.)", picmain, [4]),
       ("(This seems to be some short of event happenning in the common kitchen)", pic, [5]),
       ("(Thinking about it now, aren't the grub club in charge of the dessert aspect of the Prom.)", picmain, [6]),
       ("Maybe I can sneak a peek at what dessert will be at prom in advanced!!", picmain, [7], name, "sounds/animalese (1).wav"), 
       ("(As you are trying to see through the crowd to see what food they are preparing, a shadow can be seen creeping up behind her)", pic, [8]),
       ("Oi!! What are you doing ?!?", pic, [9], "JungCook", "sounds/animalese (1).wav"),
       ("(Wah!! Shit scared the hell outta me.)", picmain, [10], name),
       ("(Who is the annoying guy spoiling my business!!!)", picmain, [11], name),
       ("(You turn around to see a tall handsome man with curly hair)", picofJC, [12]),
       ("(OMG itss JungCook!!!)", picmain, [13], name),
       ("(You might be wondering why the Grub Club was in charge of the dessert for Prom)", pic, [14]),
       ("(It is all because of this one man! JungCook is from a renowned family of chef, he also has an impressive history of winning multiple competitions. He is the star chef of SUTD)", picofJC, [15]),
       ("(JungCook has specially requested to help with the Prom dessert, with his reputation, no one would refuse his proposition!)", picofJC, [16]),
       ("Hellooo, did you not hear me. WHAT ARE YOU DOING HERE!!!", picofJC, [17], "JungCook", "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("BooBoo Gaga", pic, []),
       ("O nothing im just here chilling randomly outside a window, for no apparent reason, just ignore me. ", picmain, [20], name, "sounds/animalese (1).wav"),
       ("Okay weirdo, give me a reason why I shouldn’t just report you for suspicious activity huh.", picofJC, [21], "JungCook", "sounds/animalese (1).wav"),
       ("Because of that UFO over there", picmain, [22], name , "sounds/animalese (1).wav"),
       ("(As JungCook turns around, you immediately ran away.)", picmain, [23]),
       ("What the!?? What a interesting lady she is.", picofJC, [28], "JungCook", "sounds/animalese (1).wav"),
       ("(You stare at JungCook for awhile before turning and walking away)", picmain, [25]),
       ("????????", picofJC,[28], "JungCook"),
       ("O i'm just curious about what they are cooking ", picmain, [27], name, "sounds/animalese (1).wav"),
       ("If you are curious about cooking, how about you pay attention to our grub club telegram rather than stand outside like a weirdo", picofJC, [28], "JungCook", "sounds/animalese (1).wav"),
       ("WTF?!!??", picmain, [29], name, "sounds/animalese (1).wav"),
       ("Day End", picofmoon, [30]),
       #Day 2!!!!!!!!!!!!!!!
       ("Day 2 ", picofsun, [31]),
       ("(You just finished the last lesson of the day and is walking with your friend)", pic, [32]),
       ("Ahhh im stravinggg, wanna go eat gom-gom, canteen getting kinda boring", picmain, [33], name, "sounds/animalese (1).wav"),
       ("Sorry sis, i got project meeting right now. Have fun, CHAO!", picshadow, [34], "Friend 1", "sounds/animalese (1).wav"),
       ("Everyday project, haiz guess im going gom-gom alone", picmain, [35], name , "sounds/animalese (1).wav"),
       ("(Reaches Gom-Gom)", picofgomgom, [36]),
       ("Didn’t expect gom-gom to have such a long queue today.", picmain, [37], name, "sounds/animalese (1).wav"),
       ("(As you are queuing you hear a male voice behind you talking loudly, you turn around to realise that it was JungCook and as you saw him, he saw you as well)", pic, [38]),
       ("Huh didn’t expect to see you here again suspicious woman", picofJC, [39], "JungCook", "sounds/animalese (1).wav"),
       ("Nice to see you too!! Why can't you just say hello like normal people", picmain, [40], name, "sounds/animalese (1).wav"),
       ("And just to clarify I wasn’t being weird I just happen to be there when you arrive ", picmain, [41], name,"sounds/animalese (1).wav"),
       ("Whatever", picofJC, [42], "JungCook", "sounds/animalese (1).wav"),
       ("O what a sweet couple, we happen to have a promotion where you can get 2 sandwiches for 50%% off would you two like to share this?", picofshadow, [43], "CASHIER", "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "I will TAKE TWO FOR MYSELF", "nextSceneIndex": 44, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "No thanks", "nextSceneIndex": 48, "affection":{"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Clarify the relationship", "nextSceneIndex": 57, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("NOOO!!! I will take two chicken sandwichesss for myself, such a good offer", picmain, [45], name, "sounds/animalese (1).wav"),
       ("(JungCook rolling his eyes at your response)", picofJC, [46]),
       ("I will just have a avocado bowl thanks", picofJC, [47], "JungCook", "sounds/animalese (1).wav"),
       ("(As you are waitin for the food, JungCook starts having casual chat with you about school project as well as assignments, a friendship has started to form.)", pic, [61]),
       ("O no thanks, I will just have a chicken sandwich that’s all", picmain, [49],name, "sounds/animalese (1).wav"),
       ("Give me on avocado bowl thanks", picofJC, [50], "JungCook", "sounds/animalese (1).wav"),
       ("(As you are waiting for the food to be prepared)", "", [51]),
       ("You know you couldve ordered 2 chicken sandwich and split it with me, I wouldn’t have mind", picofJC, [52], "JungCook", "sounds/animalese (1).wav"),
       ("I didn’t want to them to get the wrong idea that we are dating, we just met recently afterall. ", picmain, [53], name, "sounds/animalese (1).wav"),
       ("We could be friends tho since we happened to meet coincidentally again so soon.", picmain, [54], "sounds/animalese (1).wav"),
       ("Sure im JungCook im sure you already know who I am", picofJC, [55], "JungCook", "sounds/animalese (1).wav"),
       ("Ahha I do know you, im {}, Nice to know you.".format(name), picmain, [56],name, "sounds/animalese (1).wav"),
       ("(After chatting while waiting for food, you left after taking your order. A new friendship was form)", pic, [61]),
       ("O no no no we aren't dating, he is just a random guy I met yesterday", picmain, [58], name, "sounds/animalese (1).wav"),
       ("As If my standards would be so low, I rather date a cow then her.", picofJC, [59], "JungCook", "sounds/animalese (1).wav"),
       ("Heyyyyy!!! Rude much", picmain, [60],name, "sounds/animalese (1).wav"),
       ("(You ordered a chicken sandwich and left after receiving it, you did not bother interacting with JungCook in anyway)", pic, [61]),
       ("Day End", picofmoon, [62]),
       #Day 3 !!!!!!!!!!!
       ("Day 3", picofsun, [63]),
       ("(After lesson, you decided that studying in dorm was unproductive hence you decided to visit the library)",pic, [64]),
       ("Woah the library is surprisingly full today", picmain, [65], name, "sounds/animalese (1).wav"),
       ("(As you are trying to find a seat, you spotted JungCook sitting alone in a corner, you also saw your group of friends sitting at the other side)", picmain, [66]),
       ("(You decided to approach JungCook)", pic, [67]),
       ("Hi JC, I see you are reading a recipe book, is it so you can prepare me dinner?? ", picmain, [68],name, "sounds/animalese (1).wav"),
       ("very funny. As you know im in charge of the dessert portion of the prom, I need to find a good dessert option for the day, something easy yet delicious. ", picofJC, [69], "JungCook", "sounds/animalese (1).wav"),
       ("Haiz, here I thought you would be treating your dear friend to your cooking.", pic, [70],name,  "sounds/animalese (1).wav"),
       ("One day one day I will cook for you.", picofJC, [71], "JungCook", "sounds/animalese (1).wav"),
       ("Anyways JC seriously?? Is that suppose to be my name?", picofJC, [72], "JungCook","sounds/animalese (1).wav"),
       ("Ya, JungCook short form would be JC, such a good nickname", picmain, [73],name, "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Join JungCook to study", "nextSceneIndex": 74, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Join your classmate ", "nextSceneIndex": 79, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Joke with him", "nextSceneIndex": 82, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("ANYWAYS NO GOING BACK ON YOUR WORDS, THAT WAS A PROMISE TO COOK ME A MEAL", picmain, [75], name, "sounds/animalese (1).wav"),
       ("Anyways mind if I sit here.", picmain, [76],name, "sounds/animalese (1).wav"),
       ("Nope", picofJC, [77], "JungCook", "sounds/animalese (1).wav"),
       ("(You proceeded to study, as time pass you and JC had more conversation throughout the sessions until you have to leave for your project meeting)", pic, [78]),
       ("See you soon JC, I will wait for your treat", picmain, [86],name, "sounds/animalese (1).wav"),
       ("Ok see you next time then, imma go study with my classmate", picmain, [80],name ,"sounds/animalese (1).wav"),
       ("Ok see you", picofJC, [81], "JungCook", "sounds/animalese (1).wav"),
       ("(You study with your friends until you had to leave)", pic, [86]),
       ("Anyways, you should stop reading more recipe, you seem rounder today", picmain, [83],name, "sounds/animalese (1).wav"),
       ("Excuse me! I dare you to say that again.", picofJC, [84], "JungCook","sounds/animalese (1).wav"),
       ("Jeez i'm just kidding, why gotta be so defensive", picmain, [85],name, "sounds/animalese (1).wav"),
       ("(You then go to study with your friend)", picmain, [86]),
       ("Day End", picofmoon, [87]),
       #Day 4!!!!!!!!!!!!!!
       ("Day 4", picofsun, [88]),
       ("God dammit why is this assignment so hard!!", picmain, [89], name, "sounds/animalese (1).wav"),
       ("(Looking at your phone you realise that you has been studying for 8 hours straight and that it is now 3am)", picmain, [90]),
       ("I need to sleep if not I will miss tomorrow classes.", picmain, [91],name, "sounds/animalese (1).wav"),
       ("(As you are standing up, you suddenly hear a rumbling noise from your stomach.)", picmain, [92]),
       ("Hmm I guess I will go to the pantry and get a snack.", picmain, [93], name,"sounds/animalese (1).wav"),
       ("(You proceeded to the pantry)", pic, [94]),
       ("Hmm what snack should I pick???", picmain, [95], name,"sounds/animalese (1).wav"),
       ("You shouldn’t eat snack so late at night you know, it's bad for your health.", picshadow, [96], "UNKNOWN", "sounds/animalese (1).wav"),
       ("O god, O is just you JC, scared the hell outta me", picmain, [97], name, "sounds/animalese (1).wav"),
       ("I have no choice man, I'm hungry and there isn’t anything for me to eat. If it's so unhealthy, why are you here as well", picmain, [98], name, "sounds/animalese (1).wav"),
       ("Please, does it look like I need to buy snacks? I'm the best chef here, when I'm hungry I can just cook myself a delicacy.", picofJC, [99], "JungCook", "sounds/animalese (1).wav"),
       ("Which is why I'm here, I'm was planning to cook a simple meal before I sleep.", picofJC, [100], "JungCook", "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "Doubt Him", "nextSceneIndex": 101, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Agree with him", "nextSceneIndex": 118, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Cooking is EZ", "nextSceneIndex": 126, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Huhh best chef, when did you get that title, I don’t believe you. Unlesssss I get to taste the food you cook.", picmain, [102], name, "sounds/animalese (1).wav"),
       ("Tsk I don’t need your approval however my title and honour as the best chef In SUTD will not tolerate any insults. ", picofJC, [103], "JungCook", "sounds/animalese (1).wav"),
       ("Prepared to be blown away, food will never taste the same again.", picofJC, [104], "JungCook", "sounds/animalese (1).wav"),
       ("Ya right, prove me wrong", picmain, [105], name, "sounds/animalese (1).wav"),
       ("(Hehe free food from the chef JungCook himself WORTHHH!!!!)", picmain, [106]),
       ("(JC was indeed an amazing chef, with his fast movement and precision knife work, he was able to make ingredients the way he wanted it.)", pic, [107]),
       ("(It looks so simple yet complex at the same time. Looking at him work, it was like watching a performance)", pic, [108]),
       ("(This didn’t last long as JC quickly prepared a simple dish of egg fried rice)", pic, [109]),
       ("Wow that was fast!", picmain, [110], name, "sounds/animalese (1).wav"),
       ("Of Course, a good chef does not keep his customers hungry", picofJC, [111], "JungCook", "sounds/animalese (1).wav"),
       ("Now for the main judging", picmain, [112], name, "sounds/animalese (1).wav"),
       ("O wow, this is delicious.", picmain, [113], name, "sounds/animalese (1).wav"),
       ("I mean hmm its acceptable, better than most fried rice I've tasted ", picmain, [114], name, "sounds/animalese (1).wav"),
       ("Don’t try to deny it, your action has already betrayed your words.", picofJC, [115], "JungCook", "sounds/animalese (1).wav"),
       ("You can eat it slowly, I cooked more than one persons worth. Enjoy!!", picofJC, [116], "JungCook", "sounds/animalese (1).wav"),
       ("Thadwadnkss", picmain, [117], name, "sounds/animalese (1).wav"),
       ("(You enjoyed yourself and thanked JC, you went to sleep)", pic,[130]),
       ("Well good for you that you know how to cook, I’ve never had any chance or time to learn cooking. ", picmain, [119], name,"sounds/animalese (1).wav"),
       ("Maybe one day I will ask you to teach me how to cook.", picmain, [120], name,"sounds/animalese (1).wav"),
       ("No problem, just hit me up and I will teach you the best cooking tutorial you have ever seen", picofJC, [121], "JungCook", "sounds/animalese (1).wav"),
       ("Anyways what are you cooking?", picmain, [122], name,"sounds/animalese (1).wav"),
       ("Just a simple egg fried rice, do you want some as well?", picofJC, [123], "JungCook", "sounds/animalese (1).wav"),
       ("If you wouldn’t mind cooking extra, I would love to have your cooking.", picmain, [124], name, "sounds/animalese (1).wav"),
       ("(JC nods and proceed to cook fried rice)", pic, [125]),
       ("(You eat the fried rice with pleasure and awe, you then leave after finishing and saying goodbye)", pic, [130]),
       ("Show off! You can cook so what, I don’t think cooking is that hard anyway.", picmain, [127], name, "sounds/animalese (1).wav"),
       ("Its certainly harder than you just yapping, get out of my way, I need to get my equipments.", picofJC, [128], "JungCook", "sounds/animalese (1).wav"),
       ("TSK this pantry aint yours.", picmain, [129], name, "sounds/animalese (1).wav"),
       ("(You bought snacks and leave)", pic, [130]),
       ("Day End", picofmoon, [131]),
       #Day 5!!!!!!!!!!!!!!!!!!!
       ("Day 5", picofsun, [132]),
       ("(Today was a chill day, you enjoyed the peaceful moments [Affection with JungCook too low])", picmain, [157], '??',"sounds/animalese (1).wav" , {"NPC": JUNGCOOK, "comparison": BIGGER, "amount": 3, "altSceneIndex": 133 }),
       ("(You just finished her fifth row of volleyball training)", picmain, [134]),
       ("Good training guys, see you guys CHAOOO", picmain, [135], name, "sounds/animalese (1).wav"),
       ("Woo, all those workout got me famished, what do I want what do I want", picmain, [136], name, "sounds/animalese (1).wav"),
       ("Hmm Mcd sounds good, hmm meggi sounds amazing as well. O man how I wish I could just get both.", picmain, [137], name, "sounds/animalese (1).wav"),
       ("(As you are thinking about what to eat, JungCook approaches you)", picofJC, [138]),
       ("O hi, JC.", picmain, [139], name,"sounds/animalese (1).wav"),
       ("Yo, you free now? ", picofJC, [140], "JungCook", "sounds/animalese (1).wav"),
       ("YASss, why?", picmain, [141], name, "sounds/animalese (1).wav"),
       ("Nothing much just that remember when I owe you dinner, well I’m free now to cook for you", picofJC, [142], "JungCook", "sounds/animalese (1).wav"),
       ("", picofsun, [{"text": "LETSS GOOOOO", "nextSceneIndex": 143, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Be Polite", "nextSceneIndex": 148, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Reject Him", "nextSceneIndex": 152, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Letss gooooooo, I was just nice hungry after training. I will say first, I not someone with a small stomach.", picmain, [144], name,"sounds/animalese (1).wav"),
       ("No problem, do you know who I am? My name is Cook, JungCook.", picofJC, [145], "JungCook", "sounds/animalese (1).wav"),
       ("Cooking a meal for the whole school wouldn’t be an issue to me much less one person.", picofJC, [146], "JungCook", "sounds/animalese (1).wav"),
       ("Hahha good, I shall feast tonight then.", picmain, [147], name,"sounds/animalese (1).wav"),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", pic,[157]),
       ("Oo, I was just joking hahah, I wont force you to treat me dinner.", picmain, [149], name,"sounds/animalese (1).wav"),
       ("No issue, I have already prepared the ingredients in advanced. You can think of it as me treating my friend to dinner. I am your friend right?", picofJC, [150], "JungCook", "sounds/animalese (1).wav"),
       ("Of Course, well lets go then. Thank you for the meal.", picmain, [151], name,"sounds/animalese (1).wav"),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", pic, [157]),
       ("Thanks but no thanks, imma go mac.", picmain, [153], name,"sounds/animalese (1).wav"),
       ("Actually picking mcd over my cooking? Tsk suit urself.", picofJC, [154], "JungCook", "sounds/animalese (1).wav"), 
       ("(JungCook walk away)", picofJC, [155]), 
       ("Eh whatever", picmain, [156], name,"sounds/animalese (1).wav"), 
       ("(You ordered mac delivery and enjoyed yourself)", picmain,[157]), 
       ("Day End", picofmoon, [158]), 
       #Day 6!!!!!!!!!!!!!!
       ("Day 6", picofsun, [159]), 
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




              
       
     