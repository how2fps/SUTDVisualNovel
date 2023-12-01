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
picofkitchen = "pictures/JC/kitchensutd.png"
pickitchenmain = "pictures/JC/mainkitchen1.png"
pickitchenJCangry = "pictures/JC/JCkitchenangry.png"
pickitchenJCnorm = "pictures/JC/JCkitchennormal.png"
picgom = "pictures/JC/gomorign.png"
picgomJC = "pictures/JC/gomJC1.png"
picmgommain = "pictures/JC/gommain1.png"
picmgommain2 = "pictures/JC/gommain2.png"
picofsun = "pictures/JC/JCsun.png"
picofmoon = "pictures/JC/jcmoonfinal.png"
picofgomcash = "pictures/JC/gomcashier.png"
piclib = "pictures/JC/libmain.png"
piclib2 = "pictures/JC/libmainnice.png"
picJClib = 'pictures/JC/JClibgeneric.png'
pic = "pictures/dog.png"
picofgomgom = "pictures/JC/gomgomnew.png"
sound = "sounds/animalese (1).wav"
Jung = "sounds/animaleseJC (1).wav"
name2 = "JungCook"

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
       diag = [
       ["Day 1", picofsun, [1]], 
       ["Haiz, why does uni have to be so hard. Why can't the proffessor just give everyone passes", "pictures/JC/mainday1start.png", [2], name, sound],
       ["(As you are heading back dorm, you smelt an amazing scent coming from the kitchen)", "pictures/JC/mainday1start.png", [3]],
       ("(Curiosity got the better of you as you decide to check it out.)", "pictures/JC/mainday1start.png", [4]),
       ("(This seems to be some short of event happenning in the common kitchen)", picofkitchen, [5]),
       ("(Thinking about it now, aren't the grub club in charge of the dessert aspect of the Prom.)", pickitchenmain, [6]),
       ("Maybe I can sneak a peek at what dessert will be at prom in advanced!!", pickitchenmain, [7], name, sound), 
       ("(As you are trying to see through the crowd to see what food they are preparing, a shadow can be seen creeping up behind her)", "pictures/JC/kitchenshadow.png", [8]),
       ("Oi!! What are you doing ?!?", pickitchenJCangry, [9], "JungCook", Jung),
       ("(Wah!! Shit scared the hell outta me.)", pickitchenmain, [10], name),
       ("(Who is the annoying guy spoiling my business!!!)", pickitchenmain, [11], name),
       ("(You turn around to see a tall handsome man with curly hair)", pickitchenJCnorm, [12]),
       ("(OMG itss JungCook!!!)", pickitchenmain, [13], name),
       ("(You might be wondering why the Grub Club was in charge of the dessert for Prom)", pickitchenmain, [14]),
       ("(It is all because of this one man! JungCook is from a renowned family of chef, he also has an impressive history of winning multiple competitions. He is the star chef of SUTD)", pickitchenJCnorm, [15]),
       ("(JungCook has specially requested to help with the Prom dessert, with his reputation, no one would refuse his proposition!)", pickitchenJCnorm, [16]),
       ("Hellooo, did you not hear me. WHAT ARE YOU DOING HERE!!!", pickitchenJCangry, [17], "JungCook", Jung),
       ("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("BooBoo Gaga", pic, []),
       ("O nothing im just here chilling randomly outside a window, for no apparent reason, just ignore me. ", pickitchenmain, [20], name, sound),
       ("Okay weirdo, give me a reason why I shouldn’t just report you for suspicious activity huh.", pickitchenJCangry, [21], "JungCook", Jung),
       ("Because of that UFO over there", pickitchenmain, [22], name , sound),
       ("(As JungCook turns around, you immediately ran away.)", pickitchenmain, [23]),
       ("What the!?? What a interesting lady she is.", pickitchenJCnorm, [29], "JungCook", Jung),
       ("(You stare at JungCook for awhile before turning and walking away)", pickitchenmain, [25]),
       ("????????", pickitchenJCnorm,[29], "JungCook"),
       ("O i'm just curious about what they are cooking ", pickitchenJCnorm, [27], name, sound),
       ("If you are curious about cooking, how about you pay attention to our grub club telegram rather than stand outside like a weirdo", pickitchenJCangry, [28], "JungCook", Jung),
       ("WTF?!!??", pickitchenmain, [29], name, sound),
       ("Day End", picofmoon, [30]),
       #Day 2 Done!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("Day 2 ", picofsun, [31]),
       ("(You just finished the last lesson of the day and is walking with your friend)", "pictures/JC/schwalk.png", [32]),
       ("Ahhh im stravinggg, wanna go eat gom-gom, canteen getting kinda boring", "pictures/JC/schwalk.png", [33], name, sound),
       ("Sorry sis, i got project meeting right now. Have fun, CHAO!", "pictures/JC/schwalk.png", [34], "Friend 1", sound),
       ("Everyday project, haiz guess im going gom-gom alone", "pictures/JC/schwalk.png", [35], name , sound),
       ("(Reaches Gom-Gom)", picgom, [36]),
       ("Didn’t expect gom-gom to have such a long queue today.", picmgommain, [37], name, sound),
       ("(As you are queuing you hear a male voice behind you talking loudly, you turn around to realise that it was JungCook and as you saw him, he saw you as well)", picgomJC, [38]),
       ("Huh didn’t expect to see you here again suspicious woman", picgomJC, [39], "JungCook", Jung),
       ("Nice to see you too!! Why can't you just say hello like normal people", picmgommain2, [40], name, sound),
       ("And just to clarify I wasn’t being weird I just happen to be there when you arrive ", picmgommain, [41], name,sound),
       ("Whatever", picgomJC, [42], "JungCook", Jung),
       ("O what a sweet couple, we happen to have a promotion where you can get 2 sandwiches for 50% off would you two like to share this?", picofgomcash, [43], "CASHIER", sound),
       ("", picofsun, [{"text": "I will TAKE TWO FOR MYSELF", "nextSceneIndex": 44, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "No thanks", "nextSceneIndex": 48, "affection":{"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Clarify the relationship", "nextSceneIndex": 57, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("NOOO!!! I will take two chicken sandwichesss for myself, such a good offer", picmgommain, [45], name, sound),
       ("(JungCook rolling his eyes at your response)", picgomJC, [46]),
       ("I will just have a avocado bowl thanks", picgomJC, [47], "JungCook", Jung),
       ("(As you are waitin for the food, JungCook starts having casual chat with you about school project as well as assignments, a friendship has started to form.)", picgom, [61]),
       ("O no thanks, I will just have a chicken sandwich that’s all", picmgommain2, [49],name, sound),
       ("Give me on avocado bowl thanks", picgomJC, [50], "JungCook", Jung),
       ("(As you are waiting for the food to be prepared)", picgom, [51]),
       ("You know you couldve ordered 2 chicken sandwich and split it with me, I wouldn’t have mind", picgomJC, [52], "JungCook", Jung),
       ("I didn’t want to them to get the wrong idea that we are dating, we just met recently afterall. ", picmgommain2, [53], name, sound),
       ("We could be friends tho since we happened to meet coincidentally again so soon.", picmgommain, [54], sound),
       ("Sure im JungCook im sure you already know who I am", picgomJC, [55], "JungCook", Jung),
       ("Ahha I do know you, im {}, Nice to know you.".format(name), picmgommain, [56],name, sound),
       ("(After chatting while waiting for food, you left after taking your order. A new friendship was form)", picgom, [61]),
       ("O no no no we aren't dating, he is just a random guy I met yesterday", picmgommain2, [58], name, sound),
       ("As If my standards would be so low, I rather date a cow then her.", picgomJC, [59], "JungCook", Jung),
       ("Heyyyyy!!! Rude much", picmgommain2, [60],name, sound),
       ("(You ordered a chicken sandwich and left after receiving it, you did not bother interacting with JungCook in anyway)", picgom, [61]),
       ("Day End", picofmoon, [62]),
       #Day 3 Done !--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("Day 3", picofsun, [63]),
       ("(After lesson, you decided that studying in dorm was unproductive hence you decided to visit the library)","pictures/JC/libstart.png", [64]),
       ("Woah the library is surprisingly full today", piclib, [65], name, sound),
       ("(As you are trying to find a seat, you spotted JungCook sitting alone in a corner, you also saw your group of friends sitting at the other side)", "pictures/JC/JCreadbook.png", [66]),
       ("(You decided to approach JungCook)", piclib, [67]),
       ("Hi JC, I see you are reading a recipe book, is it so you can prepare me dinner?? ", piclib, [68],name, sound),
       ("very funny. As you know im in charge of the dessert portion of the prom, I need to find a good dessert option for the day, something easy yet delicious. ", picJClib, [69], "JungCook", Jung),
       ("Haiz, here I thought you would be treating your dear friend to your cooking.", piclib, [70],name,  sound),
       ("One day one day I will cook for you.", picJClib, [71], "JungCook", Jung),
       ("Anyways JC seriously?? Is that suppose to be my name?", picJClib, [72], "JungCook",Jung),
       ("Ya, JungCook short form would be JC, such a good nickname", piclib2, [73],name, sound),
       ("", picofsun, [{"text": "Join JungCook to study", "nextSceneIndex": 74, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Join your classmate ", "nextSceneIndex": 79, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Joke with him", "nextSceneIndex": 82, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("ANYWAYS NO GOING BACK ON YOUR WORDS, THAT WAS A PROMISE TO COOK ME A MEAL", piclib2, [75], name, sound),
       ("Anyways mind if I sit here.", piclib, [76],name, sound),
       ("Nope", picJClib, [77], "JungCook", Jung),
       ("(You proceeded to study, as time pass you and JC had more conversation throughout the sessions until you have to leave for your project meeting)", pic, [78]),
       ("See you soon JC, I will wait for your treat", piclib, [86],name, sound),
       ("Ok see you next time then, imma go study with my classmate", piclib2, [80],name ,sound),
       ("Ok see you", picJClib, [81], "JungCook", Jung),
       ("(You study with your friends until you had to leave)", "pictures/JC/libstart.png", [86]),
       ("Anyways, you should stop reading more recipe, you seem rounder today", piclib2, [83],name, sound),
       ("Excuse me! I dare you to say that again.", "pictures/JC/JCandmainlibangry.png", [84], "JungCook",Jung),
       ("Jeez i'm just kidding, why gotta be so defensive", piclib, [85],name, sound),
       ("(You then go to study with your friend)", "pictures/JC/libstart.png", [86]),
       ("Day End", picofmoon, [87]),
       #Day 4 Done!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("Day 4", picofsun, [88]),
       ("God dammit why is this assignment so hard!!", "pictures/JC/mainrm.png", [89], name, sound),
       ("(Looking at your phone you realise that you has been studying for 8 hours straight and that it is now 3am)", "pictures/JC/mainrm.png", [90]),
       ("I need to sleep if not I will miss tomorrow classes.", "pictures/JC/mainrm.png", [91],name, sound),
       ("(As you are standing up, you suddenly hear a rumbling noise from your stomach.)", "pictures/JC/mainrm.png", [92]),
       ("Hmm I guess I will go to the pantry and get a snack.", "pictures/JC/mainrm.png", [93], name,sound),
       ("(You proceeded to the pantry)", picofkitchen, [94]),
       ("Hmm what snack should I pick???", pickitchenmain, [95], name,sound),
       ("You shouldn’t eat snack so late at night you know, it's bad for your health.", "pictures/JC/kitchenshadow.png", [96], "UNKNOWN", Jung),
       ("O god, O is just you JC, scared the hell outta me", pickitchenmain, [97], name, sound),
       ("I have no choice man, I'm hungry and there isn’t anything for me to eat. If it's so unhealthy, why are you here as well", pickitchenmain, [98], name, sound),
       ("Please, does it look like I need to buy snacks? I'm the best chef here, when I'm hungry I can just cook myself a delicacy.", pickitchenJCnorm, [99], "JungCook", Jung),
       ("Which is why I'm here, I'm was planning to cook a simple meal before I sleep.", pickitchenJCnorm, [100], "JungCook", Jung),
       ("", picofsun, [{"text": "Doubt Him", "nextSceneIndex": 101, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Agree with him", "nextSceneIndex": 118, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Cooking is EZ", "nextSceneIndex": 126, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Huhh best chef, when did you get that title, I don’t believe you. Unlesssss I get to taste the food you cook.", pickitchenmain, [102], name, sound),
       ("Tsk I don’t need your approval however my title and honour as the best chef In SUTD will not tolerate any insults. ", pickitchenJCnorm, [103], "JungCook", Jung),
       ("Prepared to be blown away, food will never taste the same again.", pickitchenJCnorm, [104], "JungCook", Jung),
       ("Ya right, prove me wrong", pickitchenmain, [105], name, sound),
       ("(Hehe free food from the chef JungCook himself WORTHHH!!!!)", pickitchenmain, [106]),
       ("(JC was indeed an amazing chef, with his fast movement and precision knife work, he was able to make ingredients the way he wanted it.)", pickitchenJCnorm, [107]),
       ("(It looks so simple yet complex at the same time. Looking at him work, it was like watching a performance)", pickitchenmain, [108]),
       ("(This didn’t last long as JC quickly prepared a simple dish of egg fried rice)", pickitchenJCnorm, [109]),
       ("Wow that was fast!", pickitchenmain, [110], name, sound),
       ("Of Course, a good chef does not keep his customers hungry", pickitchenJCnorm, [111], "JungCook", Jung),
       ("Now for the main judging", pickitchenmain, [112], name, sound),
       ("O wow, this is delicious.", pickitchenmain, [113], name, sound),
       ("I mean hmm its acceptable, better than most fried rice I've tasted ", pickitchenmain, [114], name, sound),
       ("Don’t try to deny it, your action has already betrayed your words.", pickitchenJCnorm, [115], "JungCook", Jung),
       ("You can eat it slowly, I cooked more than one persons worth. Enjoy!!", pickitchenJCnorm, [116], "JungCook", Jung),
       ("Thadwadnkss", pickitchenmain, [117], name, sound),
       ("(You enjoyed yourself and thanked JC, you went to sleep)", picofkitchen,[130]),
       ("Well good for you that you know how to cook, I’ve never had any chance or time to learn cooking. ", pickitchenmain, [119], name,sound),
       ("Maybe one day I will ask you to teach me how to cook.", pickitchenmain, [120], name,sound),
       ("No problem, just hit me up and I will teach you the best cooking tutorial you have ever seen", pickitchenJCnorm, [121], "JungCook", Jung),
       ("Anyways what are you cooking?", pickitchenmain, [122], name,sound),
       ("Just a simple egg fried rice, do you want some as well?", pickitchenJCnorm, [123], "JungCook", Jung),
       ("If you wouldn’t mind cooking extra, I would love to have your cooking.", pickitchenmain, [124], name, sound),
       ("(JC nods and proceed to cook fried rice)", picofkitchen, [125]),
       ("(You eat the fried rice with pleasure and awe, you then leave after finishing and saying goodbye)", picofkitchen, [130]),
       ("Show off! You can cook so what, I don’t think cooking is that hard anyway.", pickitchenmain, [127], name, sound),
       ("Its certainly harder than you just yapping, get out of my way, I need to get my equipments.", pickitchenJCangry, [128], "JungCook", Jung),
       ("TSK this pantry aint yours.", pickitchenJCnorm, [129], name, sound),
       ("(You bought snacks and leave)", picofkitchen, [130]),
       ("Day End", picofmoon, [131]),
       #Day 5 Done !-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("Day 5", picofsun, [132]),
       ("(Today was a chill day, you enjoyed the peaceful moments [Affection with JungCook too low])", picofmoon, [157], '',sound , {"NPC": JUNGCOOK, "comparison": BIGGER, "amount": 3, "altSceneIndex": 133 }),
       ("(You just finished her fifth row of volleyball training)", "pictures/JC/mainday1start.png", [134]),
       ("Good training guys, see you guys CHAOOO", "pictures/JC/mainday1start.png", [135], name, sound),
       ("Woo, all those workout got me famished, what do I want what do I want", "pictures/JC/mainday1start.png", [136], name, sound),
       ("Hmm Mcd sounds good, hmm meggi sounds amazing as well. O man how I wish I could just get both.", "pictures/JC/mainday1start.png", [137], name, sound),
       ("(As you are thinking about what to eat, JungCook approaches you)", "pictures/JC/jcwalkway.png", [138]),
       ("O hi, JC.", "pictures/JC/mainday1start.png", [139], name,sound),
       ("Yo, you free now? ", "pictures/JC/jcwalkway.png", [140], "JungCook", Jung),
       ("YASss, why?", "pictures/JC/mainday1start.png", [141], name, sound),
       ("Nothing much just that remember when I owe you dinner, well I’m free now to cook for you", "pictures/JC/jcwalkway.png", [142], "JungCook", Jung),
       ("", picofsun, [{"text": "LETSS GOOOOO", "nextSceneIndex": 143, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Be Polite", "nextSceneIndex": 148, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Reject Him", "nextSceneIndex": 152, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]),
       ("Letss gooooooo, I was just nice hungry after training. I will say first, I not someone with a small stomach.", "pictures/JC/mainday1start.png", [144], name,sound),
       ("No problem, do you know who I am? My name is Cook, JungCook.", "pictures/JC/jcwalkway.png", [145], "JungCook", sound),
       ("Cooking a meal for the whole school wouldn’t be an issue to me much less one person.", "pictures/JC/jcwalkway.png", [146], "JungCook", Jung),
       ("Hahha good, I shall feast tonight then.", "pictures/JC/mainday1start.png", [147], name,sound),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", picofkitchen,[157]),
       ("Oo, I was just joking hahah, I wont force you to treat me dinner.", "pictures/JC/mainday1start.png", [149], name,sound),
       ("No issue, I have already prepared the ingredients in advanced. You can think of it as me treating my friend to dinner. I am your friend right?", "pictures/JC/jcwalkway.png", [150], "JungCook", Jung),
       ("Of Course, well lets go then. Thank you for the meal.", "pictures/JC/mainday1start.png", [151], name,sound),
       ("(You followed JC to the block communal kitchen where JC had prepared the food ingredients beforehand. JC cooked a feast for you and you two enjoyed yourselves)", picofkitchen, [157]),
       ("Thanks but no thanks, imma go mac.", "pictures/JC/mainday1start.png", [153], name,sound),
       ("Actually picking mcd over my cooking? Tsk suit urself.", "pictures/JC/jcangrywalkway.png", [154], "JungCook", Jung), 
       ("(JungCook walk away)", "pictures/JC/walkwayorigin.png", [155]), 
       ("Eh whatever", "pictures/JC/mainday1start.png", [156], name,sound), 
       ("(You ordered mac delivery and enjoyed yourself)", "pictures/JC/mainrm.png",[157]), 
       ("Day End", picofmoon, [158]), 
       #Day 6 Done!---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("Day 6", picofsun, [159]), 
       ("(You are with your friend at ccp, deciding what to eat.)", "pictures/JC/ccpfriend.png" ,[160]), 
       ("Hmmmm, what should we eat?", "pictures/JC/ccpfriend.png", [161], name, sound), 
       ("How bout Sukiya? Its nice and cheap?", "pictures/JC/ccpfriend.png", [162], "Friend 1", sound), 
       ("I just had that yesterday though", "pictures/JC/ccpfriend.png", [163], "Friend 2", sound), 
       ("(Time passed as they discussed, finally deciding to eat Seoul Garden HotPot)", "pictures/JC/soeulorigin.png", [164]), 
       ("(Main and her friends enjoyed the food and was having fun talking)", "pictures/JC/friendseoul.png", [165]), 
       ("I go pay first ah", "pictures/JC/soeulmain.png", [166], name, sound),  
       ("(You stand up and went to the cashier)", "pictures/JC/soeulmain.png", [167]), 
       ("(You noticed that JC happened to be there and is eating alone)", "pictures/JC/jcsoeul.png", [168]), 
       ("", picofsun, [{"text": "Approach Him", "nextSceneIndex": 169, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Pay First Then Approach Him", "nextSceneIndex": 179, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Ignore Him", "nextSceneIndex": 187, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]), 
       ("O hiii, JC what a coincidence. ", "pictures/JC/soeulmain.png", [170], name, sound), 
       ("O hi, did you have your dinner here as well?", "pictures/JC/jcsoeul.png", [171], "JungCook", Jung), 
       ("Yaa, the food was not bad, Im going to pay for my meal now", "pictures/JC/soeulmain.png", [172], name, sound), 
       ("O in that case, I will just treat you the meal", "pictures/JC/jcsoeul.png", [173], "JungCook", Jung), 
       ("O no, theres no need for that, this meal is with my friends, the price must be enormous", "pictures/JC/soeulmain.png", [174], name, sound),
       ("Hahah no worries, this restaurant is actually under my family. Plus your friends can be my friends too, do let intro me to them next time.", "pictures/JC/jcsoeul.png", [175], "JungCook", Jung),
       ("But I feel like I have been taking too much free stuff from you recently.", "pictures/JC/soeulmain.png", [176], name, sound),
       ("Isnt that what being friend is all about, just tell me your table number and go enjoy the food.", "pictures/JC/jcsoeul.png", [177], "JungCook",Jung),
       ("Ok thanks a lot, I will pay you back next time.", "pictures/JC/soeulmain.png", [178], name, sound),
       ("(You enjoy the company of your friends, you also inform them about JC treating which resulted in them teasing you about it. You can’t help to think that maybe JC does have interest in you)", "pictures/JC/friendseoul.png", [190]),
       ("(You went to pay for the meal before approaching JC)", "pictures/JC/jcsoeul.png", [180]),
       ("Hi, JC what a coincidence. ", "pictures/JC/soeulmain.png", [181], name, sound),
       ("O hi, did you have your dinner here as well?", "pictures/JC/jcsoeul.png", [182], name2, Jung),
       ("Yaa, the food was not bad, Im going to pay for my meal now", "pictures/JC/soeulmain.png", [183], name, sound),
       ("O in that case, I will just treat you the meal", "pictures/JC/jcsoeul.png", [184], name2, Jung),
       ("O theres no need for that, I already paid for the meal.", "pictures/JC/soeulmain.png", [185], name, sound),
       ("O ok, enjoy the meal.", "pictures/JC/jcsoeul.png", [186], name2, Jung),
       ("(Main enjoy the company of her friends)", "pictures/JC/friendseoul.png", [190]),
       ("Im just gonna pay and go, I have nothing to talk to him about anyway", "pictures/JC/soeulmain.png", [188], name, sound),
       ("(You went to pay at the cashier)", 'pictures/JC/friend1soeul.png', [189]),
       ("(You didn’t know that JC had actually notice you was there and was unhappy you didn’t come say hi)", "pictures/JC/jcsouelangry.png", [190]),
       ("Day End", picofmoon, [191]),
       #Day 7!-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("(Today was a chill day, you enjoyed the peaceful moments [Affection with JungCook too low])", picofmoon, [217], '',sound , {"NPC": JUNGCOOK, "comparison": BIGGER, "amount": 5, "altSceneIndex": 192 }),
       ("(You are in your dorm, studying)", "pictures/JC/mainrm.png", [193]),
       #ring sounds
       ("(Phone rings, it’s a call from JC)", "pictures/JC/mainrm.png", [194]),
       ("Hi JC, wassup.", "pictures/JC/mainrm.png", [195], name, sound),
       ("Are you free today afternoon?, I need help with something.", "pictures/JC/jcrm.png", [196], name2, Jung),
       ("hmm should be free.", "pictures/JC/mainrm.png", [197], name, sound),
       ("Wonderful, meet you at our block kitchen at 2pm then.", "pictures/JC/jcrm.png", [198], name2, Jung),
       ("Sure see you.", "pictures/JC/mainrm.png", [199], name, sound),
       ("(At 2pm)", picofkitchen, [200]),
       ("Come lets go in, I need help deciding the finishing touch to my dessert.", pickitchenJCnorm, [201], name2, Jung),
       ("Dessert? For prom?", pickitchenmain, [202], name, sound),
       ("Yes for Prom, I had a discussion with the other chef and we have different opinions about it.", pickitchenJCnorm, [203], name2, Jung),
       ("So I wanted to consult a consumer and the first person I thought of was you.", pickitchenJCnorm, [204], name2, Jung),
       ("Ah I see, what the dessert and the finishing touches you guys were arguing about.", pickitchenmain, [205], name, sound),
       ("Tomorrow is prom day so its prob ok for me to tell you this, it’s a pound cake muffin. ", pickitchenJCnorm, [206], name2, Jung),
       ("However we were deciding whether we should use whip cream and strawberry or just drizzle of lemon topping. Both has their advantages.", "pictures/JC/choicemuffin.png", [207], name2, Jung),
       ("HMmmm both sounds so good, but if I were to choose.", pickitchenmain, [208], name, sound),
       ("", picofsun, [{"text": "Whip Cream and Strawberry", "nextSceneIndex": 209, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Drizzle of Lemon Syrup", "nextSceneIndex": 210, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Why Not Both", "nextSceneIndex": 211, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}]),
       ("I would probably choose the whip cream and strawberry. ", pickitchenmain, [213], name, sound),
       ("I would probably choose the lemon drizzle.", pickitchenmain, [213], name, sound),
       ("Actually I don’t see why we cant just combine both. I feel like having lemon drizzle on the whip cream and strawberry could actually work.", pickitchenmain, [212], name, sound),
       ("Interesting, I will test it out and let you know.", pickitchenJCnorm, [213],name2, Jung),
       ("Thanks for the help. Here is the sample of the cake just for the help.", pickitchenJCnorm, [214], name2, Jung),
       ("YAYYYY", pickitchenmain, [215], name, sound),
       ("(You eat the cake and chatted with JC)", "pictures/JC/eat.png", [216], name),
       ("(You left after thanking JC.)", pickitchenmain, [217], name, sound),
       ("Day End", picofmoon, [218]),
       #Prom Day Done !-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       ("PROM DAY", picofsun, [219]),
       ("(Its Prom Day, as others were preparing for prom. You realise that you do not have any partner for tonight.)", picofmoon, [220], '', sound, {"NPC": JUNGCOOK, "comparison": BIGGER, "amount": 5, "altSceneIndex": 222 }),
       ("(If you had made better choices maybe someone would have asked you to be their prom date.)", picofmoon, [221], '',sound),
       ("Too bad You Losttt", picofmoon, [234], sound),
       #ring sound
       ("(Ringing!! Ringing!!)", "pictures/JC/mainrm.png", [223], '',sound),
       ("Hi JC!!", "pictures/JC/mainrm.png", [224], name, sound),
       ("Hi, today is Prom Day. I just want to check if you are free for tonight.", "pictures/JC/jcrm.png", [225], "JungCook", Jung),
       ("Of Course, I am!!", "pictures/JC/mainrm.png", [226], name, sound),
       ("I will pick you up at 8pm", "pictures/JC/jcrm.png", [227], "JungCook", Jung),
       ("Okkk!!!", "pictures/JC/mainrm.png", [228], name, sound),
       ("(At 8pm)", pic, [229]),
       #JC in suit
       ("(JC waited outside the door, You came out showing him your new dress you just bought for today. )", "pictures/JC/picmaindress.png", [230]),
       ("(JC was dressed more than normal as well. With his fancy blazer and Gucci shoes.)", "pictures/JC/jungcooksexyprom.png", [231]),
       ("(You guys then proceed to Prom and enjoyed yourselves. )", "pictures/JC/promtgt.png", [232]),
       ("Story End", picofsun, [233]),
       ("Congratss you got JungCook Heart", picofsun, [234]),
       ("Thanks for playing!!!!!", picofsun, [])
       ]
       return diag




              
       
     