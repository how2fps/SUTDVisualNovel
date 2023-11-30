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
XM = "Xiao Ming"

DECREASE = "decrease"
INCREASE = "increase"
NEUTRAL = "neutral"
BIGGER = "bigger"
SMALLER = "smaller"

# #[txtImgOptNameSndAff("(After a long and tiring day of classes, school has finally ended...)", "pictures/dog.png", [1]), 
                            # txtImgOptNameSndAff("Damn, I can't believe that it is already 6pm... time to go home and submit my assignment.", "pictures/dog.png", [2], name, "sounds/xm1.wav"),
                            # txtImgOptNameSndAff("(You head for the classroom door, ready to head home...)", "pictures/Mob_Balrog.png", [3]),
                            # txtImgOptNameSndAff("(Suddenly, you felt someone grab your shoulders!)", "pictures/dog.png", [4]),
                            # txtImgOptNameSndAff("NOOO WE ARE GONNA BE LATE, LETS GO NOW!", "pictures/dog.png", [5], "Mia", "sounds/xm2.wav"),
                            # txtImgOptNameSndAff("", "pictures/dog.png", [{"text": "Scene 6", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Scene 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}},{"text": "Neutral 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}]),
                            # txtImgOptNameSndAff("SCENE 6!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": SMALLER, "amount": 5, "altSceneIndex": 2 }), 
                            # txtImgOptNameSndAff("SCENE 7!", "pictures/dog.png", [4], "YAY", "sounds/animalese (1).wav"),
                            # ]), padx=2, pady=2)

def XM2(name):
    diag = [["Day 1", "pictures/dog.png", [1]],
            ["After a long and tiring day of classes, school has finally ended.", picmain, [2], "sounds/animalese (1).wav"],
            ["Damn, I can't believe that it is already 6pm...... time to go home and submit my assignment.", picmain, [3], name, "sounds/animalese (1).wav"],
            ["You head for the classroom door, ready to head home.", picmain, [4], name, "sounds/animalese (1).wav"],
            ["Suddenly, you felt someone grabbed your shoulders.", picmain, [5], name, "sounds/animalese (1).wav"],
            ["NOOO WE ARE GONNA BE LATE, LETS GO NOW", picmain, [6], "Mia", "sounds/animalese (1).wav"],
            ["You stare at her, confused.", picmain, [7], "sounds/animalese (1).wav"],
            ["THERES A FOOTBALL MATCH ONGOING, I GOTTA SUPPORT THE BOISSSSSSSSS AND YOUR COMING WITH MEEEEEE!!!", picmain, [8], "Mia", "sounds/animalese (1).wav"],
            ["As much as you are tired, you are just too kind to reject your best friend. Reluctantly, you head towards the football field.....", picmain, [9], "sounds/animalese (1).wav"],
            ["You grudgingly make your way to the stadium", picmain, [10], "sounds/animalese (1).wav"],
            ["You expect the stadium to be filled with cheers and energy.", picmain, [11], "sounds/animalese (1).wav"],
            ["You were wrong.", picmain, [12], "sounds/animalese (1).wav"],
            ["There is an ongoing match, but it's just a scrimmage. There is almost no one watching them except for a few girls “scouting” their potential boyfriends.....", picmain, [13], "sounds/animalese (1).wav"],
            ["Your friend is one of them.", picmain, [13], "sounds/animalese (1).wav"],
            ["Fortunately, the scrimmage seems pretty intense. Both teams are even and all players are going all out, desperately trying to take the lead.", picmain, [14], "sounds/animalese (1).wav"], 
            ["No one seem to stand out....except one.", picmain, [15], "sounds/animalese (1).wav"],
            ["You see a tall, charming and muscular guy with spiky hair intercepting a pass.", picmain, [16], "sounds/animalese (1).wav"],
            ["He dribbles the ball up gracefully and strikes a powerful shot into goal with ease.", picmain, [17], "sounds/animalese (1).wav"], 
            ["For the rest of the match, you had your eyes on him the entire time, being absolutely impressed by his skills and presence on the field.", picmain, [18], "sounds/animalese (1).wav"],
            ["Guys!! The game isn’t over, protect the lead. Keep it up till the whistle!!", picmain, [19], "The Guy", "sounds/animalese (1).wav"],
            ["He seems to give off such an energetic and fearsome aura over the whole field.... you could feel it all the way at the stands.", picmain, [20], "sounds/animalese (1).wav"],
            ["He must be really passionate about the game... after all it’s just a scrimmage.", picmain, [21], name, "sounds/animalese (1).wav"],
            ["I wonder what class he is from.....", picmain, [21], name, "sounds/animalese (1).wav"],
            ["The game ends, Mia drags you back towards dorm while rumbling about how cool her crush was in the field.", picmain, [22], name, "sounds/animalese (1).wav"],
            ["None of the conversation entered your head.... as the passionate spiky hair boy you witnessed earlier is stuck on your mind.", picmain, [23], "sounds/animalese (1).wav"],
            # DAY 2
            ["It’s 3pm. Lesson just ended and you decide to grab a quick late lunch in the canteen.", picmain, [], "sounds/animalese (1).wav"],
            ["Its pretty late... I hope there is not many people in the canteen at this time.", picmain, [], name, "sounds/animalese (1).wav"],
            ["You enter the canteen.", picmain, [], "sounds/animalese (1).wav"], 
            ["To your relief, there is almost no one in the canteen..... but someone catches your attention.", picmain, [], "sounds/animalese (1).wav"],
            ["You notice the spiky hair dude that was on your mind last night.", picmain, [], "sounds/animalese (1).wav"],
            ["He is sitting at the very corner of the canteen, having his own meal.", picmain, [], "sounds/animalese (1).wav"],
            ["You saw the great opportunity and mustered up your courage, approaching him with slight nervousness.", picmain, [], "sounds/animalese (1).wav"],
            ["Hey...?", picmain, [], name, "sounds/animalese (1).wav"],
            ["hello.....uhhh....do I know you?", picmain, [], "?", "sounds/animalese (1).wav"], #nervous
            ["Hi! I am {}. I was at the scrimmage yesterday. You were amazing out there! Mind if I join you?".format(name), picmain, [], name, "sounds/animalese (1).wav"],
            ["Oh, um, sure. I guess.", picmain, [], "?", "sounds/animalese (1).wav"], #surprised
            ["You ask for his name. He very shyly tells you that his name is Xiao Ming.", picmain, [], "sounds/animalese (1).wav"],
            ["You can tell that he is super shy and introverted.....maybe even socially awkward.", picmain, [], "sounds/animalese (1).wav"], 
            ["He acts completely different from when he was playing in the field yesterday.", picmain, [], "sounds/animalese (1).wav"], 
            ["I've been meaning to ask, what's the story behind your incredible moves on the field? Are you self-taught, or did you have a coach?", picmain, [], name, "sounds/animalese (1).wav"],
            ["Well..... my dad played a bit back in the day. He taught me the basics, and I guess the rest just kind of came naturally.", picmain, [], XM, "sounds/animalese (1).wav"], #shy
            ["That's amazing! It must be great having that connection with your dad. How long have you been playing football for? You seemed to be a beast out on the field last night.", picmain, [], name, "sounds/animalese (1).wav"],
            ["As XM gradually opened up about his love for the sport, Me discovered more about the person behind the athlete.", picmain, [], "sounds/animalese (1).wav"],
            ["The more you listen, the more charmed you are.", picmain, [], "sounds/animalese (1).wav"],
            ["You found the contrast between his shy demeanour and his ferocious game-time energy to be really cute. After all, how can someone be as fierce as a tiger one moment and super shy and awkward in the next?", picmain, [], "sounds/animalese (1).wav"], 
            ["He doesn’t even dare to look into your eyes while speaking...", picmain, [], "sounds/animalese (1).wav"],
            ["I noticed you seem really in the zone when you play. Is there a specific routine you follow before a game?", picmain, [], name, "sounds/animalese (1).wav"],
            ["Not really, just a bit of stretching and listening to some calming music. Helps me focus.", picmain, [], XM, "sounds/animalese (1).wav"], 
            ["Despite his reserved nature, Me sensed a hidden passion within XM.", picmain, [], "sounds/animalese (1).wav"],
            ["You know, XM, you're not at all what I expected.", picmain, [], name, "sounds/animalese (1).wav"],
            ["What did you expect?", picmain, [], XM, "sounds/animalese (1).wav"], #shy
#("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]) 
            ["", picmain, [{"text": "I don't know, maybe someone more... distant. But you're surprisingly easy to talk to.", "nextSceneIndex": 50, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "You seemed to be more conservative and shy, especially after seeing your energy and passion out on the field last night", "nextSceneIndex": 52, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "You seemed to be more conservative and shy, especially after seeing your energy and passion out on the field last night.", "nextSceneIndex": 53, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
            ["….Ahhh thanks a lot for that! I am aware I am quite socially awkward... but hearing someone say that I am approachable and easy to talk to sure is nice!!", picmain, [], XM, "sounds/animalese (1).wav"],
            ["I will keep improving ok!!", picmain, [], XM, "sounds/animalese (1).wav"],
            ["yeahh..... I get that a lot. I just don’t have a lot of energy in me unless I am playing football.... hope that’s ok.", picmain, [], XM, "sounds/animalese (1).wav"],
            ["ohhh mannn.... I know I can be pretty awkward at times. Sorry if I wasn’t able to match your energy... I will keep trying......", picmain, [], XM, "sounds/animalese (1).wav"]]
    return diag