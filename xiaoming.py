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
classroom = "pictures/xiaoming/class.png"
mia = "pictures/xiaoming/mia_1.png"
classroom_girl = "pictures/xiaoming/normal_girl.png"
field = "pictures/xiaoming/football field.png"
canteen = "pictures/xiaoming/canteen.png"
xm_canteen = "pictures/xiaoming/girl_xm_ct_shy.png"
xm_talk_ct = "pictures/xiaoming/xm_talk.png"
girl_talk_ct = "pictures/xiaoming/girl_ct_talk.png"
xm_sad_ct = "pictures/xiaoming/xm_sad_ct.png"
library = "pictures/xiaoming/library.png"
cs = "pictures/xiaoming/cs.png"
theatre = "pictures/xiaoming/cinema.png"
sm = "pictures/xiaoming/sm.png"
arcade = "pictures/xiaoming/arcade.png"


#sound effects
yawn = "sound/yawn.wav"
xm_hey = "sound/guy_hey.wav"
girl_hey = "sound/girl_hey.wav"
xm_wow = "sound/guy_wow.wav"
surprise = "sound/surprise-sound-effect-99300.wav"
animewow = "sound/woww.wav"
girl_hmm = "sound/hmm_girl.wav"
boo = "sound/boo.wav"
ohhhh = "sound/careless_whispers.wav"
bell = "sound/bell.wav"
awwcute = "sound/awwcute.wav"
awyeah = "sound/aw_yeah.wav"
xm_hmm = "sound/xm_hmm.wav"
sorry = "sound/sorry.wav"
sad = "sound/titanic.wav"
heartbeat = "sound/heartbeat.wav"


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

def XIAO_MING(name):
       diag =[
       ["Day 1", classroom, [1]],
       ["(After a long and tiring day of classes, school has finally ended.)", classroom, [2], "", bell],
       ["Damn, I can't believe that it is already 6pm...... time to go home and submit my assignment.", classroom_girl, [3], name, yawn],
       ["(You head for the classroom door, ready to head home.)", classroom, [4], name, "sounds/animalese (1).wav"],
       ["(Suddenly, you felt someone grabbed your shoulders.)", classroom, [5], name, surprise],
       ["NOOO WE ARE GONNA BE LATE, LETS GO NOW", mia, [6], "Mia", animewow],
       ["(You stare at her, confused.)", classroom, [7], "", girl_hmm],
       ["THERES A FOOTBALL MATCH ONGOING, I GOTTA SUPPORT THE BOISSSSSSSSS AND YOUR COMING WITH MEEEEEE!!!", mia, [8], "Mia", animewow],
       ["(As much as you are tired, you are just too kind to reject your best friend. Reluctantly, you head towards the football field.....)", classroom, [9], "", "sounds/animalese (1).wav"],
       ["(You grudgingly make your way to the stadium)", classroom, [10], "", yawn],
       ["(You expect the stadium to be filled with cheers and energy.)", field, [11], "", "sound/crowd.wav"],
       ["(You were wrong.)", field, [12], "", "sound/silence.wav"],
       ["(There is an ongoing match, but it's just a scrimmage. There is almost no one watching them except for a few girls “scouting” their potential boyfriends.....)", field, [13],  "", "sounds/animalese (1).wav"],
       ["(Your friend is one of them.)", "pictures/xiaoming/mia field.png", [], "", "sounds/animalese (1).wav"],
       ["(Fortunately, the scrimmage seems pretty intense. Both teams are even and all players are going all out, desperately trying to take the lead.)", field, [], "", "sounds/animalese (1).wav"],
       ["(No one seem to stand out....except one.)", field, [], "", "sounds/animalese (1).wav"],
       ["(You see a tall, charming and muscular guy with spiky hair intercepting a pass.)", "pictures/xiaoming/xm_field_smile.png", [], "", animewow],
       ["(He dribbles the ball up gracefully and strikes a powerful shot into goal with ease.)", "pictures/xiaoming/xm_field_smile.png", [], "", "sound/goal.wav"],
       ["(For the rest of the match, you had your eyes on him the entire time, being absolutely impressed by his skills and presence on the field.)", field, [], "", animewow],
       ["Guys!! The game isn’t over, protect the lead. Keep it up till the whistle!!", "pictures/xiaoming/xm_field2.png", [], "The Guy", xm_hey],
       ["(He seems to give off such an energetic and fearsome aura over the whole field.... you could feel it all the way at the stands.)", "pictures/xiaoming/xm_field_smile.png", [], "", animewow],
       ["(He must be really passionate about the game... after all it’s just a scrimmage.)", field, [], name, "sounds/animalese (1).wav"],
       ["I wonder what class he is from.....", field, [], name, girl_hmm],
       ["(The game ends, Mia drags you back towards dorm while rumbling about how cool her crush was in the field.)", "pictures/xiaoming/mia_dorm.png", [], name, "sounds/animalese (1).wav"],
       ["(None of the conversation entered your head.... as the passionate spiky hair boy you witnessed earlier is stuck on your mind.)", "pictures/xiaoming/main_dorm.png", [], "", ohhhh],
       # DAY 2
       ["(DAY 2\nIt’s 3pm. Lesson just ended and you decide to grab a quick late lunch in the canteen.)", classroom, [], "", bell],
       ["Its pretty late... I hope there is not many people in the canteen at this time.", classroom_girl, [], name, girl_hmm], 
       ["(You enter the canteen.)", canteen, [], "", "sounds/animalese (1).wav"], 
       ["(To your relief, there is almost no one in the canteen..... but someone catches your attention.)", canteen, [], "", "sounds/animalese (1).wav"],
       ["(You notice the spiky hair dude that was on your mind last night.)", "pictures/xiaoming/xm_canteen.png", [], "", "sounds/animalese (1).wav"],
       ["(He is sitting at the very corner of the canteen, having his own meal.)", "pictures/xiaoming/xm_canteen.png", [], "", "sounds/animalese (1).wav"],
       ["(You see the great opportunity and muster up your courage, approaching him with slight nervousness.)", canteen, [], "", "sounds/animalese (1).wav"],
       ["Hey...?", "pictures/xiaoming/girl_xm_ct_normal.png", [], name, girl_hey],
       ["hello.....uhhh....do I know you?", xm_canteen, [], "?", surprise], #nervous
       ["Hi! I am {}. I was at the scrimmage yesterday. You were amazing out there! Mind if I join you?".format(name), girl_talk_ct, [], name, girl_hey],
       ["Oh, um, sure. I guess.", xm_canteen, [], "?", xm_hey], #surprised
       ["(You ask for his name. He very shyly tells you that his name is Xiao Ming.)", canteen, [], "", "sounds/animalese (1).wav"],
       ["(You can tell that he is super shy and introverted.....maybe even socially awkward.)", "pictures/xiaoming/xm_shy_ct.png", [], "", "sounds/animalese (1).wav"], 
       ["(He acts completely different from when he was playing in the field yesterday.)", "pictures/xiaoming/xm_shy_ct.png", [], "", "sounds/animalese (1).wav"], 
       ["I've been meaning to ask, what's the story behind your incredible moves on the field? Are you self-taught, or did you have a coach?", girl_talk_ct, [], name, girl_hey],
       ["Well..... my dad played a bit back in the day. He taught me the basics, and I guess the rest just kind of came naturally.", xm_talk_ct, [], XM, xm_hey], #shy
       ["That's amazing! It must be great having that connection with your dad. How long have you been playing football for? You seemed to be a beast out on the field last night.", girl_talk_ct, [], name, awwcute],
       ["(As XM gradually opened up about his love for the sport, Me discovered more about the person behind the athlete.)", canteen, [], "", "sounds/animalese (1).wav"],
       ["(The more you listen, the more charmed you are.)", canteen, [], "", animewow],
       ["(You found the contrast between his shy demeanour and his ferocious game-time energy to be really cute. After all, how can someone be as fierce as a tiger one moment and super shy and awkward in the next?)", canteen, [], "", "sounds/animalese (1).wav"], 
       ["(He doesn’t even dare to look into your eyes while speaking...)", canteen, [], "", "sounds/animalese (1).wav"],
       ["I noticed you seem really in the zone when you play. Is there a specific routine you follow before a game?", girl_talk_ct, [], name, girl_hey],
       ["Not really, just a bit of stretching and listening to some calming music. Helps me focus.", xm_talk_ct, [], XM, xm_hey], 
       ["(Despite his reserved nature, Me sensed a hidden passion within XM.)", canteen, [], "", "sounds/animalese (1).wav"],
       ["You know, XM, you're not at all what I expected.", girl_talk_ct, [], name, girl_hmm],
       ["What did you expect?", xm_talk_ct, [], XM, xm_hey], #shy
       #("", picofsun, [{"text": "Act SUS", "nextSceneIndex": 19, "affection": {"affectedNPC": JUNGCOOK, "change": INCREASE}}, {"text": "Ignore him", "nextSceneIndex": 24, "affection": {"affectedNPC": JUNGCOOK, "change": NEUTRAL}}, {"text": "Act Curious", "nextSceneIndex": 26, "affection": {"affectedNPC": JUNGCOOK, "change": DECREASE}}]) 
       ["", picmain, [{"text": "I don't know, maybe someone more... distant. But you're surprisingly easy to talk to.", "nextSceneIndex": 52, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "I honestly expected you to be kinda energetic, but you seem to be very shy, conserved and even awkward.... but hey that’s kinda cute tho!!.", "nextSceneIndex": 55, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}, {"text": "You seem to be more conservative and shy, especially after seeing your energy and passion out on the field last night.", "nextSceneIndex": 54, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}]],
       ["….Ahhh thanks a lot for that! I am aware I am quite socially awkward... but hearing someone say that I am approachable and easy to talk to sure is nice!!", xm_canteen, [], XM, xm_hmm],
       ["I will keep improving ok!!", xm_talk_ct, [56], XM, xm_hmm],
       ["yeahh..... I get that a lot. I just don’t have a lot of energy in me unless I am playing football.... hope that’s ok.", xm_sad_ct, [56], XM, sorry],
       ["ohhh mannn.... I know I can be pretty awkward at times. Sorry if I wasn’t able to match your energy... I will keep trying......", xm_sad_ct, [], XM, sorry],
       ["(You continue the small talks with him and gained a deeper understanding of his character.) " , canteen, [], "", "sounds/animalese (1).wav"],
       ["(Despite being shy and awkward, Xiao Ming seems to be equally interested in you as well. At least it seems that he is happy to share his stories to you.)", "pictures/xiaoming/xm_canteen.png", [], "", "sounds/animalese (1).wav"],
       ["(You even managed to exchange contacts with him, making a promise to meet each other again at some point.)" , canteen, [], "", "sounds/animalese (1).wav"],
       ["(You head back to dorm with a huge smile on your face... perhaps it is the start of something you have been looking for......)" , canteen, [], "", "sounds/animalese (1).wav"],
       # DAY 3-----------------------------------
       ["DAY 3\n(There is no lessons today as it is Wednesday.)" , "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["(You realised that you have plenty of assignments uncompleted.)" , "pictures/xiaoming/dorm.png", [], "", yawn],
       ["wow there is so much homework...physics, maths, ctd, and hass. It never ends zzzzzz....", "pictures/xiaoming/girl_dorm.png", [], name, girl_hmm],
       ["(Trying to find a chance to meet XM, you invite him to study together in the library.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["How about tackling some assignments together? Two heads are better than one!" , "pictures/xiaoming/girl_dorm.png", [], name, girl_hey],
       ["Uh, sure. I usually study alone, though." , "pictures/xiaoming/xm_dorm.png", [], XM, xm_hey],
       ["", "pictures/xiaoming/girl_dorm.png", [{"text": "Why not give it a go? Who knows, you might find it more productive too!! If you run into a tough question, we can help each other out.", "nextSceneIndex": 75, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Ahh I see. Do you wanna try it out though? It can potentially be more productive :D .", "nextSceneIndex": 75, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "I understand, group studying might not be for everyone.", "nextSceneIndex": 67, "affection" : {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["Totally cool if it’s not your style, I shouldn’t disturb you.", "pictures/xiaoming/girl_dorm.png", [], name, girl_hmm],
       ["...yeah I am sorry, I realise that I am only productive when by myself so...", "pictures/xiaoming/xm_dorm.png", [], XM, sorry],
       ["(Being disappointed, you are about to just say goodbye and move on. However, before you have the chance to end the conversation, he says something that is quite surprising.)", "pictures/xiaoming/dorm.png", [], "", sad],
       ["hey, maybe we can’t really study together... BUT how about we get dinner tomorrow to make up for it", "pictures/xiaoming/xm_dorm.png", [], XM, xm_hey],
       ["(That caught you off guard.)", "pictures/xiaoming/girl_dorm_shy.png", [], "", surprise],
       ["uhhhh sure!! I am totally down for it!! See you tomorrow then!", "pictures/xiaoming/girl_dorm.png", [], name, awyeah],
       ["(That made your day.)", "pictures/xiaoming/dorm.png", [], "", awyeah],
       ["(You spend the whole day by yourself in the library, fully motivated and positive knowing that you will be able to see him the next day anyways.)", library, [96], "", awwcute],
       ["Sure, that sounds good. Teamwork might make this less daunting.", "pictures/xiaoming/xm_dorm.png", [], XM, xm_hey],
       ["(The library becomes a haven of shared knowledge as you both delve into your assignments. XM surprises you with his insightful contributions.)", library, [], "", "sounds/animalese (1).wav"],
       ["Thanks for your heIp. I wouldn't have figured that out on my own", "pictures/xiaoming/xm_library.png", [], XM, xm_hey],
       ["No problem at all! We make a great team. What do you say we celebrate a productive day with some sandwiches? My treat.", "pictures/xiaoming/main_library.png", [], name, girl_hey],
       ["Sandwich sounds nice. Sure.", "pictures/xiaoming/xm_library.png", [], XM, xm_hmm],
       ["Great! Let's head to Gom-Gom. They have a really solid selection of sandwiches!!", "pictures/xiaoming/main_library.png", [], name, girl_hey],
       ["(After a dreadful series of assignments, both of you went to grab some sandwiches for a well-deserved treat.)", "pictures/xiaoming/gomgom.png", [], "", "sounds/animalese (1).wav"],
       ["Not bad. We managed to complete our homework!! Do you always study in the library?", "pictures/xiaoming/xm_gg.png", [], XM, xm_hey],
       ["Mostly, yeah. It's a good atmosphere for me. How about you? Any specific study rituals or habits?", "pictures/xiaoming/girl_gg.png", [], name, girl_hmm],
       ["Not really. I just try to stay focused. Do you have any tips for staying organized?", "pictures/xiaoming/xm_gg.png", [], XM, xm_hmm],
       ["Oh, absolutely! I'm a fan of color-coded notes and setting small goals. Keeps things manageable. What's your approach?", "pictures/xiaoming/girl_gg.png", [], name, girl_hmm],
       ["I keep a checklist and try to cross things off as I go. It helps me see my progress.", "pictures/xiaoming/xm_gg.png", [], XM, xm_hmm],
       ["Nice! A checklist can be really satisfying, I should try doing that.", "pictures/xiaoming/girl_gg.png", [], name, girl_hmm],
       ["(You really enjoyed the study session.)", "pictures/xiaoming/gomgom.png", [], "", "sounds/animalese (1).wav"],
       ["(Craving to see him again soon, you muster up your courage.)", "pictures/xiaoming/gomgom.png", [], name, "sounds/animalese (1).wav"],
       ["I really enjoyed studying with you today!!", "pictures/xiaoming/girl_gg.png", [], name, awwcute],
       ["Let’s...... hang out again tomorrow!! How about dinner at Changi City Point?", "pictures/xiaoming/girl_gg.png", [], name, girl_hey],
       ["(He seems a little shocked by the sudden request.)", "pictures/xiaoming/xm_shocked_gg.png", [], "", surprise],
       ["(He shyly smiles.)", "pictures/xiaoming/xm_shy_smile_gg.png", [], "", "sounds/animalese (1).wav"],
       ["uhhh.....I should be free tomorrow...I....I think....", "pictures/xiaoming/xm_shy_smile_gg.png", [], XM, xm_hmm],
       ["(As you part ways with him, you gleefully smile all the way back to dorm, excited about tomorrow.)", "pictures/xiaoming/gomgom.png", [], "", awyeah],
       # DAY 4 ------------------- 
       ["DAY 4\n(It is approaching the dinner.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["(Feeling very excited, you put on your favourite outfit and perfume.)", "pictures/xiaoming/main_dorm.png", [], "", awyeah],
       ["(You set off the CCP to meet him)", "pictures/xiaoming/ccp.png", [], "", "sounds/animalese (1).wav"],
       ["hey, you look great today.", "pictures/xiaoming/xm_talk_ccp.png", [], XM, xm_hey],
       ["(Your heart flutters.)", "pictures/xiaoming/girl_ccp_sad.png", [], "", ohhhh],
       ["hahahaha thanks!! Uhhhh what do you wanna eat today?", "pictures/xiaoming/girl_ccp.png", [], name, girl_hey],
       ["Honestly, I am clueless about the restaurants here...what are your recommendations?", "pictures/xiaoming/xm_talk_ccp.png", [], XM, xm_hmm],
       ["", "pictures/xiaoming/ccp.png", [{"text": "ohhh, I am kinda craving for some Japanese food!! How about Suki-ya? It’s pretty value-for-money.", "nextSceneIndex": 109, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "hmmm, how about MacDonalds? I have cravings for some delicious McSpicy.", "nextSceneIndex": 107, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "hmmm, how about Shabu Sai, I am really craving some free-flow hotpot buffet right now!!", "nextSceneIndex": 104 , "affection": {"affectedNPC": XIAOMING, "change": DECREASE}} ]],
       ["Wow that’s gonna be quite the burden on my wallet. Can we keep it simple? After all it’s just a normal dinner", "pictures/xiaoming/xm_sad_ccp.png", [], XM, sorry],
       ["(Oof, that sounded sad)", "pictures/xiaoming/girl_ccp_sad.png", [], "", sad],
       ["Ahhh that’s fine, how about Suki-ya instead? It pretty budget compared to the others.", "pictures/xiaoming/girl_ccp.png", [109], name, girl_hey],
       ["ahhh sorry but I am trying to avoid fast food currently, I have got a competition coming up and am trying my best to stay healthy.", "pictures/xiaoming/xm_sad_ccp.png", [], XM, sorry],
       ["Oh that’s fair, how about Suki-ya then. There is a huge selection of food that is not fried and its quite budget friendly too!", "pictures/xiaoming/girl_ccp.png", [], name, girl_hey],
       ["That sounds nice... lets go for it.", "pictures/xiaoming/xm_talk_ccp.png", [], XM, xm_hey],
       ["(Both of you enter the restaurant and get seated.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["(After placing your orders, it’s time to learn even more about each other.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["", "pictures/xiaoming/girl_res.png", [{"text": "Hey, I know that you are passionate about sports. Do you happen to watch the NBA? I am a huge fan too!!", "nextSceneIndex": 117 , "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Uhh.... so what are your hobbies other than football?", "nextSceneIndex": 118 , "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "(Be silent and stare into his beautiful eyes awkwardly.... (you’re too nervous!!))", "nextSceneIndex": 113 , "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["(As expected of a super shy and introverted guy, XM stares back at you, equally awkward)", "pictures/xiaoming/xm_shy_res.png", [], "", "sounds/animalese (1).wav"],
       ["(You want to initiate a conversation, but you are so tense and nervous to think of a topic.)", "pictures/xiaoming/res.png", [], "", heartbeat],
       ["(Both of you eat the meal in silence.)", "pictures/xiaoming/res.png", [], "", "sound/silence.wav"],
       ["(The miserable night ends like this... shame on you LOL)", "pictures/xiaoming/res.png", [127], "", boo],
       ["(XM eyes lit up.)", "pictures/xiaoming/xm_eyes_res.png", [], "", "sounds/animalese (1).wav"],
       ["I love watching the NBA!! I always watch them.... even in class hehe.", "pictures/xiaoming/xm_talk_res.png", [], XM, awyeah],
       ["My favourite team is the Celtics!! I am a super huge fan of Jason Tatum, what about you?", "pictures/xiaoming/xm_talk_res.png", [], XM, xm_hey],
       ["DAMN I am SOO glad that you enjoy watching the NBA!! I am a hardcore fan and it’s nice that we have something in common 😊", "pictures/xiaoming/girl_res.png", [], name, animewow],
       ["I am a big fan of the Warriors!! Always been a joy to watch Steph Curry play the game, he really changed the entire NBA scene with his 3-pointers.", "pictures/xiaoming/girl_res.png", [], name, girl_hey],
       ["(Both of you seemed to have found a common interest.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["(Even when the food arrived, both of you continued to discuss about the sport, from the performance of each team and even predictions for the champion this season.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["(You both clown at some under-performing players and laugh at NBA memes together.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["(Suddenly it feels like both of you have gotten super close as the ‘friendship’ continues to deepen.)", "pictures/xiaoming/res.png", [], "", "sounds/animalese (1).wav"],
       ["(You wish for the conversation to continue forever, but of course all good things must come to an end.)", "pictures/xiaoming/res.png", [], "", awwcute],
       ["(After dinner, you both head to dorm together with all smiles, looking forward to the next meeting...)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       # DAy 5 ------------- end at [127]
       ["DAY 5\n(The previous night, both of you agreed to meet up again today.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["(This time, you meet Xiao Ming at the outdoor basketball court.)", "pictures/xiaoming/dorm.png", [], "", "sound/bball.wav"],
       ["(Turns out, after learning that both of you have a keen interest in NBA and basketball in general, you take the opportunity to ask him out to play basketball with you.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["(When you reach the court, he is already shooting around by himself.)", "pictures/xiaoming/bball.png", [], "", "sound/bball.wav"],
       ["Heyyy!! Let’s shoot the ball together.", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hey],
       ["(He passes you the ball and you throw up a few shots at the hoop.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["(…..you completely miss the target multiple times.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["(You look super embarrassed, getting ready to be clowned upon by XM.)", "pictures/xiaoming/girl_shy_bball.png", [], "", boo],
       ["(However, he kindly smiles and didn’t seem to be judgemental at all.)", "pictures/xiaoming/xm_smile_bball.png", [], "", awwcute],
       ["Hahaha it’s ok, let me teach you how to shoot the ball. There is certain techniques involved in shooting.", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hey],
       ["(He starts going through the shooting motion with you.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["First, you have to make sure only your shooting hand interferes with the shot... your guide hand should not alter the path of the shot at all", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hey],
       ["Also, be sure to flick your wrist. Imagine that you are dipping your fingers into the hoop as you shoot. Hold the follow through too!!", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hmm],
       ["(He passes you the ball again, signalling for you to give it a shot.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["(Unfortunately, you just seem to suck at the game.)", "pictures/xiaoming/bball.png", [], "", boo],
       ["(Rather than laughing at you, he walks towards you.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["(He holds your hand, places the ball on your palm.)", "pictures/xiaoming/xm_smile_bball.png", [], "", ohhhh],
       ["(He starts to personally adjust your shooting posture with his hands.)", "pictures/xiaoming/xm_smile_bball.png", [], "", awyeah],
       ["(You feel your heart beating fast.)", "pictures/xiaoming/bball.png", [], "", heartbeat],
       ["(You unconsciously look into his eyes.)", "pictures/xiaoming/bball.png", [], "", ohhhh],
       ["(His gentle eyes gazes back into your soul.)", "pictures/xiaoming/xm_smile_bball.png", [], "", ohhhh],
       ["(You maintain eye contact with him by accident, feeling adrenaline surging through your body)", "pictures/xiaoming/girl_shy_bball.png", [], "", ohhhh],
       ["", "pictures/xiaoming/girl_shy_bball.png", [{"text": "Continue holding that eye contact 😉", "nextSceneIndex": 151 , "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Step away from embarrassment.", "nextSceneIndex": 154 , "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}, {"text": "Look away shyly", "nextSceneIndex": 154, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}]],
       ["ahhh sorry!!", "pictures/xiaoming/xm_girl_bball.png", [], XM, sorry], #150
       ["(He shyly looks away, returning to his typical shy state.)", "pictures/xiaoming/xm_shy_bball.png", [], "", "sounds/animalese (1).wav"],
       ["uhh uhhh but ye...ahhh!! This is how the posture should be!!", "pictures/xiaoming/xm_shy_bball.png", [157], XM, xm_hey],
       ["(He looks apologetic.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["Hey, im so sorry, should have respected your personal space.", "pictures/xiaoming/xm_sad_bball.png", [], XM, sorry],
       ["I will be more mindful alright?", "pictures/xiaoming/xm_sad_bball.png", [], XM, xm_hmm],
       ["Anyways, there you have it. Practice shooting with this posture and you will be a sharpshooter in no time!!", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hey],
       ["(You take another shot, following the shooting posture given.)", "pictures/xiaoming/bball.png", [], "", "sounds/animalese (1).wav"],
       ["(You score.)", "pictures/xiaoming/bball.png", [], "", "sound/goal.wav"],
       ["LETS GO!! Damn your advice is amazing!!", "pictures/xiaoming/girl_bball_happy.png", [], name, awyeah],
       ["Yeah I know right!! I am sure you will be solid in no time!!", "pictures/xiaoming/xm_talk_bball.png", [], XM, xm_hmm],
       ["(After the session, y’all head back to dorm together)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["Hey, that was fun, thanks so much for all the guidance, really appreciate it!!", "pictures/xiaoming/girl_dorm.png", [], name, girl_hey],
       ["It’s not just me, you are a really fast-learner! It took me way longer to be able to shoot the ball decently", "pictures/xiaoming/xm_dorm.png", [], XM, xm_hey],
       ["(Y’all part ways, with the plans of catching a movie tomorrow since it is the weekends.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       # DAY 6 end at [164]
       ["DAY 6\n(It’s finally the weekends.)", "pictures/xiaoming/dorm.png", [], "", "sounds/animalese (1).wav"],
       ["(You happily make your way to Century Square, getting ready to meet Xiao Ming for a cute movie date.)", "pictures/xiaoming/cs.png", [], "", "sounds/animalese (1).wav"],
       ["(You reach the cinema and already spotted XM waiting at the corner. )", "pictures/xiaoming/cinema.png", [], "", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": SMALLER, "amount": 3, "altSceneIndex": 194}],
       ["(Being happy that he is very punctual, you walk up to him enthusiastically)", "pictures/xiaoming/cinema.png", [], "", awwcute],
       ["Hey, thank for being on time!!", "pictures/xiaoming/girl_talk_cinema.png", [], name, girl_hey],
       ["No problem. So, what movies do you want to watch?", "pictures/xiaoming/xm_happy_cinema.png", [], XM, xm_hey],
       ["", "pictures/xiaoming/girl_talk_cinema.png", [{"text": "I am thinking of watching a horror!! The Nun sounds thrilling to watch!!", "nextSceneIndex": 176 , "affection": {"affectedNPC": XIAOMING, "change": INCREASE }}, {"text": "How about some comedy? I really need a good laugh to end off this stressful week.", "nextSceneIndex": 175 , "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "How about a romance movie? I have been looking forward to watch “A Silent Voice” in the cinemas.", "nextSceneIndex": 173, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["ahhhh...... romance are not really my kinda thing. I have always been into something action-packed and thrilling. Love the adrenaline rush these movies give me. Let’s watch The Nun instead shall we? It should be exciting.", "pictures/xiaoming/xm_sad_cinema.png", [], XM, xm_hmm],
       ["Okok, let’s do it.", "pictures/xiaoming/girl_talk_cinema.png", [177], name, girl_hey],
       ["Comedy sounds nice, however I am lowkey craving for something thrilling. Let’s watch The Nun instead.", sorry, [177], XM, "sounds/animalese (1).wav"],
       ["”Damn you actually read my mind!! I am a huge fan of horror movies too. Let’s do it.”", "pictures/xiaoming/xm_happy_cinema.png", [], XM, animewow],
       ["(After buying tickets and some popcorns, you both head into the cinema and got seated.)", "pictures/xiaoming/theatre.png", [], "", "sounds/animalese (1).wav"],
       ["(As expected, the movie was gruesome and filled with jumpscares.)", "pictures/xiaoming/theatre.png", [], "", "sounds/animalese (1).wav"],
       ["(You hold on for your dear life.... maybe such movies are not meant for you.)", "pictures/xiaoming/girl_shocked_t.png", [], "", boo],
       ["(XM seems to notice your uneasiness.)", "pictures/xiaoming/theatre.png", [], "", "sounds/animalese (1).wav"],
       ["(At the climax of the movie, you felt him squeezing your hands.)", "pictures/xiaoming/girl_shocked_t.png", [], "", ohhhh],
       ["(Perhaps it’s to comfort you.)", "pictures/xiaoming/theatre.png", [], "", awwcute],
       ["", "pictures/xiaoming/theatre.png", [{"text": "Pretend nothing happen ;)", "nextSceneIndex": 184 , "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Move your hand away.", "nextSceneIndex": 187 , "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["(You sit through the remaining of the movie like this.)","pictures/xiaoming/theatre.png", [], "", awyeah],
       ["(Your heart beats fast... not because of the horror but rather from Xiao Ming’s actions.)", "pictures/xiaoming/theatre.png", [], "", ohhhh],
       ["(After what seems like forever, the movie ends.)", "pictures/xiaoming/theatre.png", [188], "", "sounds/animalese (1).wav"],
       ["(XM also quickly withdraws his hand, looking flustered.)", "pictures/xiaoming/xm_shocked_t.png", [], "", surprise],
       ["(Both of you watch the remaining of the movie awkwardly with no further interactions)", "pictures/xiaoming/theatre.png", [], "", heartbeat],
       ["Wow!! That sure was thrilling!! How did you find it? You seemed pretty horrified haha.", "pictures/xiaoming/xm_happy_cinema.png", [], XM, xm_hey],
       ["Yeah, that was really scary, maybe I overestimated myself.", "pictures/xiaoming/girl_talk_cinema.png", [], name, girl_hmm],
       ["Hahahaha its okay, you look pretty cute when scared anyways.", "pictures/xiaoming/xm_happy_cinema.png", [], XM, xm_hmm],
       ["(You blush.)", "pictures/xiaoming/girl_shocked_c.png", [], "", ohhhh],
       ["uhhhh anyways, I got to go now, see you tomorrow!!", "pictures/xiaoming/xm_happy_cinema.png", [212], XM, xm_hmm],
       # alt scene last line [192]
       ["(You arrive at the mall and started waiting for him.)", cs, [], "", "sounds/animalese (1).wav"],
       ["hmmm....he said to meet at 10am, he is 10 minutes late. Why isn’t he here yet", "pictures/xiaoming/girl_pissed_t.png", [], name, girl_hmm],
       ["Maybe I should give him a call", "pictures/xiaoming/girl_pissed_t.png", [], name, girl_hmm],
       ["(You call him.... but there was no response.)", theatre, [], "", boo],
       ["damn, lets just wait a while more.", "pictures/xiaoming/girl_pissed_t.png", [], name, girl_hmm],
       ["(As time goes by.... you become more and more infuriated.)", theatre, [], "", girl_hmm],
       ["(You look at the time, it’s 10.40am now.)", theatre, [], "", "sounds/animalese (1).wav"],
       ["(Finally, you receive a call from him)", theatre, [], "", "sounds/animalese (1).wav"],
       ["Hey!! Where are you? It’s already 10.40am!! We will probably have to catch the next movie timing!", "pictures/xiaoming/girl_pissed_t.png", [], name, girl_hmm],
       ["Yo, I am soooooo sorry, but something came up at home and I can’t join you today anymore", "pictures/xiaoming/xm_sad_cinema.png", [], XM, sorry],
       ["", "pictures/xiaoming/girl_talk_cinema.png", [{"text": "Hey, if it’s a family emergency or something, don’t sweat about it. I understand. I hope everything’s ok at home.", "nextSceneIndex": 205 , "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "It’s cool. It’s just that you should have told me in advance if you couldn’t make it.", "nextSceneIndex": 207, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "WTF, you can’t just make me wait for 40 damn minutes just for you to say that you can’t make it!!", "nextSceneIndex": 208, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["Hey, if it’s a family emergency or something, don’t sweat about it. I understand. I hope everything’s ok at home.", "pictures/xiaoming/girl_talk_cinema.png", [], name, "sounds/animalese (1).wav"],
       ["Thanks for understanding!! I am genuinely sorry and I will do my best to make it up to you!!", "pictures/xiaoming/xm_happy_cinema.png", [209], XM, awwcute],
       ["My bad. I will make sure it won’t ever happen again.", "pictures/xiaoming/xm_sad_cinema.png", [209], XM, sorry],
       ["Yoooo I am so sorry, it’s totally my bad. I hope you don’t get mad. I promise I will make it up to you. Calm down alright?", "pictures/xiaoming/xm_sad_cinema.png", [], XM, sorry],
       ["How about meeting again? Same time. I swear that I won’t make you wait for me anymore!!", "pictures/xiaoming/xm_sad_cinema.png", [], XM, xm_hey],
       ["(Disappointed, you head back home)", "pictures/xiaoming/dorm.png", [], "", sad],
       ["(It sucks, but at least he promises to make it up to you tomorrow, so your hopes are still alive.)", "pictures/xiaoming/dorm.png", [], "", sad],
       # LAST DAY FINALLY [210]\
       ["DAY 7\n(Before meeting Xiao Ming, you plan to get a gift for him for no particular reason.)", cs, [], "", "sounds/animalese (1).wav"],
       ["(Maybe love makes you do dumb things.)", cs, [], "", awwcute],
       ["(Hmmm, what should I get?)", "pictures/xiaoming/girl_cs.png", [], "", girl_hmm],
       ["(In the afternoon, you meet up with XM at the shopping mall.)", sm, [], "", "sounds/animalese (1).wav"],
       ["Hey!! I brought you a lil something, hope you like it!!", "pictures/xiaoming/girl_sm.png", [], name, awwcute],
       ["(You hand him the gift.)", sm, [], "", "sounds/animalese (1).wav"],
       ["What gift did you buy for him?", sm, [], "", "sounds/animalese (1).wav"],
       ["", sm, [{"text": "A shoebag", "nextSceneIndex": 220, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "A bunch of snacks.", "nextSceneIndex": 221, "affection": {"affectedNPC": XIAOMING, "change": NEUTRAL}}, {"text": "A cute phone cover", "nextSceneIndex": 222, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]],
       ["Wait.... how did you know I needed this, my old shoebag got holes in it and I was planning to replace it. This will do it for me!! Thanks so much!!", "pictures/xiaoming/shoebag.png", [223], XM, animewow],
       ["Oohhhh thanks!! This will push me through the late night studies!!", "pictures/xiaoming/snacks.png", [223], XM, awyeah],
       ["Ahh shit, my phone doesn’t fit into the cover 🙁 I appreciate it a lot though.", "pictures/xiaoming/phone cover.png", [], XM, xm_hmm],
       ["(You start walking around the shopping mall.)", sm, [231], "", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": BIGGER, "amount": 4, "altSceneIndex": 224}],
       ["(XM also takes out something from his bag.)", sm, [], "", "sounds/animalese (1).wav"],
       ["Hey, I brought something as well. I am not sure if you are a fan of cute key-chains, but I came across it and thought that it suits you well!", "pictures/xiaoming/xm_happy_sm.png", [], XM, awwcute],
       ["(He passes you a cute rabbit keychain.)", "pictures/xiaoming/keychain.png", [], "", "sounds/animalese (1).wav"],
       ["(You feel very heartened that he brought you a gift too.)", "pictures/xiaoming/girl_sm.png", [], "", awwcute],
       ["Soooo... where do you wanna shop at?", "pictures/xiaoming/xm_happy_sm.png", [], XM, "sounds/animalese (1).wav"],
       ["", "pictures/xiaoming/girl_sm.png", [{'text': "Sephora", "nextSceneIndex": 230, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}, {"text": "Victoria's Secret (are you fr?)", "nextSceneIndex": 230, "affection": {"affectedNPC": XIAOMING, "change":DECREASE}}, {"text": "Foot-Locker", "nextSceneIndex": 231, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}]],
       ["uhhhh... ngl I personally wouldn’t get anything from there anyways. How about Foot Locker instead? I wanna scout some new shoes to add to my collection!!", "pictures/xiaoming/xm_happy_sm.png", [], XM, sorry],
       ["Ohh sounds good. I don’t mind looking at some nice shoes too.", "pictures/xiaoming/girl_sm.png", [232], name, xm_hey],
       ["Yooo, I didn’t know that you are into shoes, I am a sneakerhead too!! If you’re looking to get a new shoe I am down to recommend you some a few models", "pictures/xiaoming/xm_happy_sm.png", [], XM, xm_hey],
       ["(Both of you visit Foot Locker, XM passionately goes through all the models of the shoes being displayed.)", "pictures/xiaoming/fl.png", [], "", "sounds/animalese (1).wav"],
       ["(He recommends a few pair that he personally thinks are value-for-money.)", "pictures/xiaoming/xm_fl.png", [], "", "sounds/animalese (1).wav"],
       ["Here, try these few pairs. It’s durable, comfortable and looks great aesthetically at the same time!!", "pictures/xiaoming/xm_fl.png", [], XM, xm_hey],
       ["(You try on the shoes.)", "pictures/xiaoming/fl.png", [], "", "sounds/animalese (1).wav"],
       ["“Hey, you look amazing with this!", "pictures/xiaoming/xm_fl.png", [], XM, xm_hey],
       ["(Embarassed but thrilled by the compliment, you decide to purchase the pair of shoes. After all, you actually like it too.)", "pictures/xiaoming/girl_shocked_fl.png", [], "", awyeah],
       ["(Seeing you buy the shoes he recommended, he smiles ear to ear, perhaps it was the satisfaction from successfully recommending a pair of shoes he likes too. )", "pictures/xiaoming/xm_smile_fl.png", [], "", awwcute],
       ["(After shopping, both of you decide to stop by the arcade)", arcade, [], "", "sounds/animalese (1).wav"],
       ["Let’s play the basketball machine!! It’s my favourite game in the arcade.", "pictures/xiaoming/xm_arcade.png", [], XM, xm_hey],
       ["(At the basketball machine, you pick up the ball.)", arcade, [], "", "sounds/animalese (1).wav"],
       ["(You adopt the shooting stance he taught you a few days back.)", arcade, [], "", "sounds/animalese (1).wav"],
       ["(He seems to notice it and smiles proudly.)", "pictures/xiaoming/xm_smile_arcade.png", [], "", awwcute],
       ["Wow, you seem to absorb everything I taught you!! You are such a fast learner!!", "pictures/xiaoming/xm_arcade.png", [], XM, xm_hey],
       ["(Both of you decide to have a friendly battle of points, with the loser treating dinner.)", arcade, [], "", "sounds/animalese (1).wav"],
       ["(Clearly, you lost the battle.)", arcade, [], "", boo],
       ["Aw man, I guess dinner is on me.", "pictures/xiaoming/girl_arcade.png", [], name, sad],
       ["All’s good, a drink will be fine. It was intense for sure. Close game, GGs!!", "pictures/xiaoming/xm_arcade.png", [], XM, xm_hey],
       ["(After treating him to bubble tea, both of you decide to take a stroll in the nearby park to end the day.)", "pictures/xiaoming/park.png", [], "", "sounds/animalese (1).wav"],
       ["(Making full use of this golden opportunity, you muster up your courage.)", "pictures/xiaoming/park.png", [], "", "sounds/animalese (1).wav"],
       ["Hey.... you know about prom at the end of the term right?", "pictures/xiaoming/girl park.png", [], name, heartbeat],
       ["Yeah... what about it", "pictures/xiaoming/xm_park.png", [], XM, xm_hmm],
       ["I....I was thinking if you can go to prom with me.", "pictures/xiaoming/girl park.png", [], name, girl_hmm],
       ["(XM stops in his tracks. He seemed visibly shocked)", "pictures/xiaoming/xm_shocked_park.png", [], "", surprise],
       ["(He seems to be processing what you said.)", "pictures/xiaoming/xm_shocked_park.png", [], "", "sounds/animalese (1).wav"],
       ["(After all, it was quite sudden.)", "pictures/xiaoming/park.png", [], "", "sounds/animalese (1).wav"],
       ["(You hold your breath, suddenly not feeling confident about this.)", "pictures/xiaoming/park.png", [], "", heartbeat, {"NPC": XIAOMING, "comparison": SMALLER, "amount": 4, "altSceneIndex": 267}], #[257]
       ["(Thankfully, his shocked face slowly turns into a heartwarming gentle smile.)", "pictures/xiaoming/xm_smile_park.png", [], "", awwcute],
       ["Hey.... how can I possibly say no to this beautiful girl here! Of course I want to.", "pictures/xiaoming/xm_park.png", [], XM, awwcute],
       ["It’s just that...I was taken aback. I was planning to ask you out for prom at some point too. I was just too shy to bring it up.", "pictures/xiaoming/xm_park.png", [], XM, xm_hey],
       ["Thank god you initiated it, now I don’t have to do it myself HAHA", "pictures/xiaoming/xm_park.png", [], XM, xm_hmm],
       ["(Congrats, it seems like the feelings was mutual.)", "pictures/xiaoming/park.png", [], "", awyeah],
       ["(On high spirits, both of you treasure the stroll back to the MRT station with all laughs and giggles.)", "pictures/xiaoming/park.png", [], "", awwcute],
       ["(Even on the way home, you smile uncontrollably.)", "pictures/xiaoming/girl_smile_park.png", [], "", awwcute],
       ["(You now have to motivation to push through the arduous studying, knowing that when exams are over you get to go prom with him.)", "pictures/xiaoming/girl_smile_park.png", [500], "", "sounds/animalese (1).wav"],
       ["(His face turned into a small frown. )", "pictures/xiaoming/xm_frown_park.png", [], "", "sounds/animalese (1).wav"],
       ["Hey, I am so sorry if I made you misunderstood.", "pictures/xiaoming/xm_frown_park2.png", [], XM, sorry],
       ["I have always just seen you as a nice friend right from the beginning.", "pictures/xiaoming/xm_frown_park2.png", [], XM, sad],
       ["I actually have someone else in mind.", "pictures/xiaoming/xm_frown_park2.png", [], XM, sad],
       ["(Your heart completely sank.)", "pictures/xiaoming/park.png", [], "", sad],
       ["I understand.... guess I was just overthinking things.", "pictures/xiaoming/girl park.png", [], name, girl_hmm],
       ["Sorry for misunderstanding your actions...", "pictures/xiaoming/girl park.png", [], name, girl_hmm],
       ["(Filled with embarrassment, you couldn’t wait to escape.)", "pictures/xiaoming/park.png", [], "", "sounds/animalese (1).wav"],
       ["I have something on.... I gotta go now.", "pictures/xiaoming/girl park.png", [], name, boo],
       ["(You turn around and sprinted all way to the MRT station without even saying goodbye.)", "pictures/xiaoming/park.png", [], "", sad],
       ["You start sobbing all the way home.)", "pictures/xiaoming/mrt.png", [], "", awwcute],
       ["(You got friendzoned.)", "pictures/xiaoming/bad.png", [], "", boo],
       ["Maybe it was just not meant to be.....", "pictures/xiaoming/bad.png", [], "", sad, None, True]
       ]
     
       return diag