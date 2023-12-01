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

AdamsSound = "sounds/WeirdAdam.wav"

def AC(name):
             #Day 1 Start
    diag =  [("Day 1: Accidental Encounter at a Coffee Shop", "pictures/AdamCmith_Pic/001.png", [1]), 
            ("[You enter your favorite local coffee shop. It's cozy and bustling with the familiar hum of espresso machines and quiet conversations. You spots Your childhood friend is sitting alone at a corner table, his brows furrowed in concentration over a pile of notes and textbooks.]", "pictures/AdamCmith_Pic/002.png", [118]),
            ("Thought: That's Adam! I haven't seen him in days. He looks so stressed... I wonder what he's studying.", "pictures/AdamCmith_Pic/003.png", [{"text": "Walk over to him and offer to help with his studies.", "nextSceneIndex": 3, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Give a friendly wave and smile, then go order coffee.", "nextSceneIndex": 10, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Tease him about always being buried in books.", "nextSceneIndex": 13, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            ("Hey Adam, you look like you could use a study buddy. Mind if I join you?", "pictures/AdamCmith_Pic/004.png", [4], name, "sounds/animalese (1).wav"),
            (f"Oh, hey {name}! That would be amazing, come sit here!", "pictures/AdamCmith_Pic/005.png", [5], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[The friend smiles warmly, appreciating her offer.]", "pictures/AdamCmith_Pic/005.png", [6]),
            ("What are you studying? Maybe two heads are better than one.", "pictures/AdamCmith_Pic/004.png", [7], name, "sounds/animalese (1).wav"),
            ("It's for my HASS class. I'm really struggling with this chapter on The Theory of Moral Sentiments.", "pictures/AdamCmith_Pic/006.png", [8], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("Huh? Let's tackle it together. I'm pretty good with that stuff.", "pictures/AdamCmith_Pic/004.png", [9], name, "sounds/animalese (1).wav"),
            ("[They spend the next hour studying together, laughing, and reconnecting over old times. The atmosphere is warm and comfortable.]", "pictures/AdamCmith_Pic/008.png", [16]),
            #Neutral Option Choosen
            ("(Waves at him) Hi Adamm, good luck with your studies!", "pictures/AdamCmith_Pic/007.png", [11], name, "sounds/animalese (1).wav"),
            (f"Thanks, {name}! Enjoy your coffee.", "pictures/AdamCmith_Pic/005.png", [12], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[He gives a brief smile and nods, focusing back on his work.]", "pictures/AdamCmith_Pic/001.png", [16]),
            #Bad Option Choosen
            ("Still the bookworm, I see. Ever thought of looking up from those books?", "pictures/AdamCmith_Pic/002.png", [14], name, "sounds/animalese (1).wav"),
            ("Uh, yeah, I guess... Just a lot to cover.", "pictures/AdamCmith_Pic/006.png", [15], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[He looks a bit hurt and self conscious, turning back to his notes.]", "pictures/AdamCmith_Pic/001.png", [16]),
            #Day 1 End Complete Gramma check
            #___________________________________________________________________________Sound_______________________________________________________________________________________________________
            #Start Day 2
            ("Day 2: Unexpected Study Group with a Twist ", "pictures/AdamCmith_Pic/101.png", [17]),
            ("[You were invited to join a study group for an upcoming major exam. The study group is scheduled to meet at a quiet location on campus, known for its serene atmosphere and conducive study environment.]", "pictures/AdamCmith_Pic/101.png", [18]),
            ("[You enter the room.]", "pictures/AdamCmith_Pic/102.png", [119]),
            ("Thought: Wow, Adam's here too? That's unexpected. It's nice to see a familiar face, though.", "pictures/AdamCmith_Pic/103.png", [{"text": "Approach Adam with a smile and express happiness to see him.", "nextSceneIndex": 20, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Greet the entire group, including Adam, but focus on the study material.", "nextSceneIndex": 26, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Act surprised and question Adam's presence in the study group.", "nextSceneIndex": 29, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            ("Adam, what a pleasant surprise to see you here!", "pictures/AdamCmith_Pic/104.png", [21], name, "sounds/animalese (1).wav"),
            (f"Hey, {name}! I didn't know you were in this study group. Great to have you with us!", "pictures/AdamCmith_Pic/105.png", [22], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam seems genuinely happy to see her, creating a warm and friendly atmosphere for the study session.]", "pictures/AdamCmith_Pic/105.png", [23]),
            ("Hey Adam, is this seat next to you taken?", "pictures/AdamCmith_Pic/106.png", [24], name, "sounds/animalese (1).wav"),
            ("No, it's free. Come sit here!", "pictures/AdamCmith_Pic/107.png", [25], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[They sit together, and as the study session progresses, they find themselves laughing and enjoying the atmosphere, blending productive study time with enjoyable conversation. This shared experience fosters a warm and friendly bond between them.] ", "pictures/AdamCmith_Pic/108.png", [32]),
            #Neutral Option Choosen
            ("Hi everyone! Ready to crack these chapters?", "pictures/AdamCmith_Pic/109.png", [27], name, "sounds/animalese (1).wav"),
            ("Definitely. Let's make the most of this session.", "pictures/AdamCmith_Pic/110.png", [28], "Adam Cmith and friends", "sounds/WeirdAdam.wav"),
            ("[The group, including Adam, acknowledges her, and they all settle into a productive study rhythm.]", "pictures/AdamCmith_Pic/101.png", [32]),
            #Bad Option Choosen
            ("Adam? I didn't expect to see you here. Are you sure you're in the right group?", "pictures/AdamCmith_Pic/111.png", [30], name, "sounds/animalese (1).wav"),
            ("Yeah, I've been part of this group for a while. Just focusing on my studies.", "pictures/AdamCmith_Pic/112.png", [31], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam seems a bit taken aback by her reaction, creating a slightly awkward tension in the group.] ", "pictures/AdamCmith_Pic/101.png", [32]),
            #Day 2 End Complete Gramma Check
            #______________________________________________________________________________Sound____________________________________________________________________________________________________
            #Start Day 3
            ("Day 3: Campus Garden Discovery", "pictures/AdamCmith_Pic/201.png", [33]),
            ("[You, seeking a quiet spot to relax and clear your mind, stumble upon a hidden garden on campus. This tranquil oasis is filled with colorful flowers, lush greenery, and the soothing sound of a small fountain.]", "pictures/AdamCmith_Pic/202.png", [34]),
            ("[You wander around and see Adam holding a camera.]", "pictures/AdamCmith_Pic/203.png", [120]),
            ("Thought: That's Adam... I didn't know he had an interest in photography. He seems so peaceful here." , "pictures/AdamCmith_Pic/204.png", [{"text": "Approach and express interest in his secret hobby. ", "nextSceneIndex": 36, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Watch Adam silently at a distance and not disturb him.", "nextSceneIndex": 43, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Walk up to Adam and joke about his hobby.", "nextSceneIndex": 45, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            ("Hey, Adam, this is a beautiful spot. I had no idea you were into photography. Can I see what you've captured?", "pictures/AdamCmith_Pic/205.png", [37], name, "sounds/animalese (1).wav"),
            (f"Oh, hi {name}! Sure, take a look. I just started last week so don’t expect much.", "pictures/AdamCmith_Pic/203.png", [38], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("No way! These are so beautiful!", "pictures/AdamCmith_Pic/204.png", [39], name, "sounds/animalese (1).wav"),
            ("[They share a moment, appreciating the garden and his work.]", "pictures/AdamCmith_Pic/206.png", [40]),
            ("Hey, can you take a picture of me? Make sure I look good, ok?", "pictures/AdamCmith_Pic/205.png", [41], name, "sounds/animalese (1).wav"),
            ("Of course, move here; these flowers really complement your outfit.", "pictures/AdamCmith_Pic/207.png", [42], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam took a dozen pictures as you posed. They enjoy this moment together in the beautiful garden.]", "pictures/AdamCmith_Pic/208.png", [48]),
            #Neutral Option Choosen
            ("Thought: I shouldn't interrupt his moment of creativity. It's nice to see him so absorbed in his passion.", "pictures/AdamCmith_Pic/209.png", [44], name),
            ("[You enjoy the garden on your own, respecting his space. Adam never noticed that you were there.]", "pictures/AdamCmith_Pic/201.png", [48]),
            #Bad Option Choosen
            ("Since when are you into photography? The camera does not fit you at all, haha.", "pictures/AdamCmith_Pic/210.png", [46], name, "sounds/animalese (1).wav"),
            ("Ha ha ha… [Dry laugh] ", "pictures/AdamCmith_Pic/211.png", [47], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[You keep teasing Adam, making him feel insecure about his secret hobby.]", "pictures/AdamCmith_Pic/201.png", [48]),
            #Day 3 End Gramma Check Complete
            #__________________________________________________________________________________Sound________________________________________________________________________________________________
            #Start Day 4
            ("Day 4: Volunteering Together at a Dog Shelter", "pictures/AdamCmith_Pic/301.png", [49]),
            ("[You receive an unexpected text from Adam inviting you to join him in volunteering at a local dog shelter. It’s been years since we volunteered at this shelter together.]", "pictures/AdamCmith_Pic/302.png", [50]),
            ("Text: Hey, I'm volunteering at the dog shelter this weekend. It’s the one that we used to go to together years ago; do you want to join me?", "pictures/AdamCmith_Pic/303.png", [121], "Adam Cmith"),
            ("Thought: Volunteering at a dog shelter with Adam... It's really been a while since we went together." , "pictures/AdamCmith_Pic/304.png", [{"text": "Enthusiastically accept the invitation.", "nextSceneIndex": 52, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Politely decline due to being busy.", "nextSceneIndex": 59, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Leave the invitation on read without responding.", "nextSceneIndex": 62, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            ("Text: That sounds amazing, Adam! I'd love to join you. What time should we meet?","pictures/AdamCmith_Pic/305.png", [53], name),
            ("Text: Great! Let's meet at 10 AM. It'll be fun!", "pictures/AdamCmith_Pic/306.png", [54], "Adam Cmith"),
            ("[Adam is pleased with her enthusiastic response, and they look forward to spending a fulfilling day at the shelter, bonding over their love for animals.]", "pictures/AdamCmith_Pic/307.png", [55]),
            ("[They meet at the dog shelter.]", "pictures/AdamCmith_Pic/301.png", [56]),
            ("You remember Buster, that little beagle we took care of last time? I heard he was adopted by a lovely family. It's bittersweet, isn't it? I'm happy to see him find a home, but I also miss him...", "pictures/AdamCmith_Pic/308.png", [57], name, "sounds/animalese (1).wav"),
            ("Yeah, I'm glad he found a good home. It's these moments, isn't it? Seeing them happy and loved is what makes all of this so worthwhile.", "pictures/AdamCmith_Pic/309.png", [58], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[They talk and laugh over memories of their past volunteer days. These memories reveal a deeper, long standing bond between them.]", "pictures/AdamCmith_Pic/310.png", [65]),
            #Neutral Option Choosen
            ("Text: I'd really like to join you, Adam, but I'm swamped with work this weekend. Rain check?", "pictures/AdamCmith_Pic/311.png", [60], name),
            ("Text: No worries, I understand. Let's plan for another time!", "pictures/AdamCmith_Pic/312.png", [61], "Adam Cmith"),
            ("[Adam respects her busy schedule, and they both express a willingness to plan something together in the future.]", "pictures/AdamCmith_Pic/307.png", [65]),
            #Bad Option Choosen
            ("Thought: Well, I am not really free this weekend... Let me check my schedule again so I can confirm with him.", "pictures/AdamCmith_Pic/313.png", [63], name),
            ("[You completely forgot to text him back, leaving him on read.] ", "pictures/AdamCmith_Pic/307.png", [64]),
            ("[Adam feels ignored and is unsure about your interest in spending time with him, leading to potential awkwardness in future interactions.]", "pictures/AdamCmith_Pic/314.png", [65]),
            #Day 4 End Gramma Check Complete
            #_______________________________________________________________________________________Sound___________________________________________________________________________________________
            #Start Day 5
            ("Day 5: Photography Exhibition ", "pictures/AdamCmith_Pic/401.png", [66]),
            ("[The Photographic Circle Club is hosting a photography exhibition showcasing the work of students. You are interested in art and photography and decide to visit the exhibition. Upon your arrival, you are surprised to discover that Adam has his own photography work displayed.]", "pictures/AdamCmith_Pic/402.png", [122]),
            ("Thought: I had no idea Adam was into photography to this extent. His pictures are really impressive." , "pictures/AdamCmith_Pic/403.png", [{"text": "Express admiration for his work and ask him about his inspiration.", "nextSceneIndex": 68, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Compliment his work politely and browse other exhibits.", "nextSceneIndex": 74, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Make a light_hearted joke about his serious photographs.", "nextSceneIndex": 77, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            ("Adam, your photographs are amazing! What inspires you to capture these moments?","pictures/AdamCmith_Pic/404.png", [69], name, "sounds/animalese (1).wav"),
            ("Thanks! I find inspiration in everyday life, the small moments that tell a story. It means a lot that you appreciate it.", "pictures/AdamCmith_Pic/405.png", [70], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam is touched by her genuine interest and opens up about his passion for photography, leading to a deep and meaningful conversation.]", "pictures/AdamCmith_Pic/405.png", [71]),
            ("Hey, this is the picture you took for me in the garden!?", "pictures/AdamCmith_Pic/406.png", [72], name, "sounds/animalese (1).wav"),
            ("Yeah, that is one of my favorites and best works; it’s so captivating...", "pictures/AdamCmith_Pic/407.png", [73], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam and you walk into the exhibition together, enjoying each other’s company. Their relationship has deepened.] ", "pictures/AdamCmith_Pic/408.png", [80]),
            #Neutral Option Choosen
            ("Nice work on these photos, Adam. You've got a good eye.", "pictures/AdamCmith_Pic/409.png", [75], name, "sounds/animalese (1).wav"),
            ("Thanks, Feel free to look around the rest.", "pictures/AdamCmith_Pic/410.png", [76], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam appreciates your compliment, but their interaction remains on a surface level as you move on to view other artworks.]", "pictures/AdamCmith_Pic/401.png", [80]),
            #Bad Option Choosen
            ("These photos aren’t bad. Did you really take these yourself?", "pictures/AdamCmith_Pic/411.png", [78], name, "sounds/animalese (1).wav"),
            ("Yeah, well, I have been practicing a lot and thought people would like it more...", "pictures/AdamCmith_Pic/412.png", [79], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Adam feels slightly misunderstood and retreats into his shell, creating a subtle distance between them.]", "pictures/AdamCmith_Pic/401.png", [80]),
            #Day 5 End Gramma Check Complete
            #_____________________________________________________________________________________Sound_____________________________________________________________________________________________
            #Start Day 6
            ("Day 6: Romantic Beach Walk", "pictures/AdamCmith_Pic/501.png", [81], None, None, {"NPC": ADAMCMITH, "comparison": SMALLER, "amount": 3, "altSceneIndex": 116 }),
            ("[You and Adam decide to take an evening walk along the beach. The sound of the waves, the gentle sea breeze, and the stunning sunset create a perfect romantic setting.]", "pictures/AdamCmith_Pic/502.png", [124]),
            ("[As they walk side by side on the sandy shore, the fading sunlight casts a warm glow, creating a serene and intimate atmosphere.]" , "pictures/AdamCmith_Pic/503.png", [{"text": "Open up about feelings.", "nextSceneIndex": 83, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Enjoy the walk in comfortable silence.", "nextSceneIndex": 89, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Make a casual remark about the setting and emphasize their friendship.", "nextSceneIndex": 91, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}]),
            #Good Option Choosen
            ("Adam, I'm really glad we're here together. There's something special about this moment, don't you think?","pictures/AdamCmith_Pic/504.png", [84], name, "sounds/animalese (1).wav"),
            ("I was thinking the same. It feels like everything's just right.", "pictures/AdamCmith_Pic/505.png", [85], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[This honest exchange brings them closer, allowing their relationship to progress into something more than just friendship.]", "pictures/AdamCmith_Pic/506.png", [86]),
            ("You know, I've always found the ocean to be calming, but tonight, it feels even more special. Maybe it's the company.", "pictures/AdamCmith_Pic/507.png", [87], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("I've always loved the beach too. It's like all your worries just wash away with the tide.", "pictures/AdamCmith_Pic/508.png", [88], name, "sounds/animalese (1).wav"),
            ("[They sit in silence for a moment, simply enjoying each other's presence. As the sun sets, their expressions soften in the twilight. A brief exchange of glances at each other—it's their little special moment.] ", "pictures/AdamCmith_Pic/509.png", [94]),
            #Neutral Option Choosen
            ("Thought: Sometimes, words aren't needed. This quiet companionship says it all.", "pictures/AdamCmith_Pic/510.png", [90], name),
            ("[They continue walking, appreciating the beauty around them and each other's company without the need for words.]", "pictures/AdamCmith_Pic/501.png", [94]),
            #Bad Option Choosen
            ("Nice weather for a beach walk, isn't it? It’s good to have a best friend to do these things with.", "pictures/AdamCmith_Pic/511.png", [92], name, "sounds/animalese (1).wav"),
            ("Yeah, it's pretty great...", "pictures/AdamCmith_Pic/512.png", [93], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[The conversation stays on the surface; however, Adam is reminded of his position as just a good friend.]", "pictures/AdamCmith_Pic/513.png", [123]),#Can make a secret ending the Friend zone
            #Day 6 End Gramma Check Complete
            #_______________________________________________________________________________________Sound___________________________________________________________________________________________
            #Start Day 7
            ("Day 7: Memory Lane at the Café", "pictures/AdamCmith_Pic/001.png", [95], None, None,{"NPC": ADAMCMITH, "comparison": SMALLER, "amount": 4, "altSceneIndex": 116 }),
            ("[You decide to visit the café, reflecting on the incredible week you had. As you walk in, you are surprised and delighted to find Adam there, sitting at the same table where they first reconnected.]", "pictures/AdamCmith_Pic/009.png", [96]),
            ("Thought: This feels like déjà vu, but so much has changed since that first day.", "pictures/AdamCmith_Pic/010.png", [97], name),
            ("[She approaches Adam, who looks up and smiles warmly. As she sat down, Adam exclaimed in his jolly voice...]", "pictures/AdamCmith_Pic/011.png", [125]),
            ("Look what I got here, he says, pulling out his camera. I took some pictures during our beach walk yesterday." , "pictures/AdamCmith_Pic/012.png", [{"text": "Express love for the photos and appreciation for his thoughtfulness.", "nextSceneIndex": 99, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Leave a quick comment on his photo and move on.", "nextSceneIndex": 108, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Acknowledge the photos but express discomfort at being photographed so much.", "nextSceneIndex": 111, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], "Adam Cmith"),
            #Good Option Choosen
            ("These are beautiful, Adam! Although did you take photos of anything else, or was I your only subject?","pictures/AdamCmith_Pic/013.png", [100], name, "sounds/animalese (1).wav"),
            ("Honestly, you were the most picturesque of all the surroundings. How could I focus on anything else?", "pictures/AdamCmith_Pic/014.png", [101], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[You appreciated the comment and felt a warm feeling in your heart.]", "pictures/AdamCmith_Pic/015.png", [102]),
            ("Wow, I never thought you could say something like that; you have grown, don’t you?", "pictures/AdamCmith_Pic/016.png", [103], name, "sounds/animalese (1).wav"),
            ("Well, I am tired of waiting, so how do you think of me?", "pictures/AdamCmith_Pic/017.png", [104], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[The protagonist gives a slight pause, then, with a soft voice, she asks...] ", "pictures/AdamCmith_Pic/018.png", [105]),
            ("Will you go to prom with me?", "pictures/AdamCmith_Pic/019.png", [106], name, "sounds/animalese (1).wav"),
            ("Of course I will.", "pictures/AdamCmith_Pic/020.png", [107], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Amidst the bustling coffee shop, it seemed as though there were only the two of them. The burden that had rested on their chests had lifted, and they eagerly anticipated the arrival of tomorrow.] ", "pictures/AdamCmith_Pic/021.png", [114]),
            #Neutral Option Choosen
            ("You really do have talent here, Adam. These are very nice. Let's talk more later. I have a meeting at 5. Bye.", "pictures/AdamCmith_Pic/022.png", [109], name, "sounds/animalese (1).wav"),
            ("Thank, he you later.", "pictures/AdamCmith_Pic/023.png", [110], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[Their conversation is brief and plain. No further development really happens in the interaction.]", "pictures/AdamCmith_Pic/001.png", [116]),
            #Bad Option Choosen
            ("These are nice, but... it's a little weird that you took so many pictures of me, don't you think?", "pictures/AdamCmith_Pic/024.png", [112], name, "sounds/animalese (1).wav"),
            ("Oh, I didn't mean to make you uncomfortable. I just thought you looked really happy and wanted to capture that...", "pictures/AdamCmith_Pic/025.png", [113], "Adam Cmith", "sounds/WeirdAdam.wav"),
            ("[The mood becomes awkward. Adam feels misunderstood, and the protagonist senses that she might have hurt his feelings.]", "pictures/AdamCmith_Pic/001.png", [116]),
            #Day 7 End
            #________________________________________________________________________________Sound__________________________________________________________________________________________________
            #Good ending index link to 114
<<<<<<< HEAD
            ("[You and Adam go to prom to gether]", "pictures/Prom Night.png", [115]),
            ("[Congratulations You Win]", "pictures/Prom Night.png", [], True),
            #Bad ending index link 116
            ("Adam felt distence from you", "pictures/No Prom.png", [117]),
            ("You Lose", "pictures/No prom.png", [117], True),
=======
            ("[You and Adam go to prom to gether]", "pictures/dog.png", [115]),
            ("[Congratulations You Win]", "pictures/dog.png", [115], '', '', None, True),
            #Bad ending index link 116
            ("Adam felt distence from you", "pictures/dog.png", [117]),
            ("You Lose", "pictures/dog.png", [117], '', '', None, True),
>>>>>>> 373657e45c1a3acd98955853f9d12d4c7c237112
            #Adjustment to Options Update
            ("Thought: That's Adam! I haven't seen him in days. He looks so stressed... I wonder what he's studying.", "pictures/AdamCmith_Pic/003.png", [2], name),#118
            ("Thought: Wow, Adam's here too? That's unexpected. It's nice to see a familiar face, though.", "pictures/AdamCmith_Pic/103.png", [19], name),#119
            ("Thought: That's Adam... I didn't know he had an interest in photography. He seems so peaceful here." , "pictures/AdamCmith_Pic/204.png", [35], name),#120
            ("Thought: Volunteering at a dog shelter with Adam... It's really been a while since we went together." , "pictures/AdamCmith_Pic/304.png", [51], name),#121
            ("Thought: I had no idea Adam was into photography to this extent. His pictures are really impressive." , "pictures/AdamCmith_Pic/403.png", [67], name),#122
            ("What do you expect? You just friend zoned him...." , "pictures/AdamCmith_Pic/513.png", [123], "GM", "sounds/fzending.wav", True),#123
            ("[As they walk side by side on the sandy shore, the fading sunlight casts a warm glow, creating a serene and intimate atmosphere.]" , "pictures/AdamCmith_Pic/503.png", [82]),#124
            ("Look what I got here, he says, pulling out his camera. I took some pictures during our beach walk yesterday." , "pictures/AdamCmith_Pic/012.png", [98], "Adam Cmith", "sounds/WeirdAdam.wav")#125

            
    ]
    return diag