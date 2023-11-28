import warnings
import winsound
from tkinter import *
from classes import *
from jungcook import *
from main import txtImgOptNameSndAff, createNameFrame, cleanUp, createScenes

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

def AC(name):
             #Day 1 Start
    diag =  [txtImgOptNameSndAff("Day 1: Accidental Encounter at a Coffee Shop", "pictures/CoffeeBlur.png", [1]), 
            txtImgOptNameSndAff("[You enter your favorite local coffee shop. It's cozy and bustling with the familiar hum of espresso machines and quiet conversations. You spots Your childhood friend is sitting alone at a corner table, his brows furrowed in concentration over a pile of notes and textbooks.]", "pictures/CoffeeBlur.png", [2]),
            txtImgOptNameSndAff("Thought: That's Adam! I haven't seen him in days. He looks so stressed... I wonder what he's studying.", "pictures/CoffeeShop.png", [{"text": "Walk over to him and offer to help with his studies.", "nextSceneIndex": 3, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Give a friendly wave and smile, then go order coffee.", "nextSceneIndex": 10, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Tease him about always being buried in books.", "nextSceneIndex": 13, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            txtImgOptNameSndAff("Hey Adam, you look like you could use a study buddy. Mind if I join you?", "pictures/CoffeeShop.png", [4], name),
            txtImgOptNameSndAff(f"Oh, hey {name}! That would be amazing, come sit here!", "pictures/CoffeeShop.png", [5], "Adam Cmith"),
            txtImgOptNameSndAff("[The friend smiles warmly, appreciating her offer.]", "pictures/CoffeeShop.png", [6]),
            txtImgOptNameSndAff("What are you studying? Maybe two heads are better than one.", "pictures/CoffeeShop.png", [7], name),
            txtImgOptNameSndAff("It's for my HASS class. I'm really struggling with this chapter on The Theory of Moral Sentiments.", "pictures/CoffeeShop.png", [8], "Adam Cmith"),
            txtImgOptNameSndAff("Huh? Let's tackle it together. I'm pretty good with that stuff.", "pictures/CoffeeShop.png", [9], name),
            txtImgOptNameSndAff("[They spend the next hour studying together, laughing, and reconnecting over old times. The atmosphere is warm and comfortable.]", "pictures/CoffeeBlur.png", [16]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("(Waves at him) Hi Adamm, good luck with your studies!", "pictures/CoffeeShop.png", [11], name),
            txtImgOptNameSndAff(f"Thanks, {name}! Enjoy your coffee.", "pictures/CoffeeShop.png", [12], "Adam Cmith"),
            txtImgOptNameSndAff("[He gives a brief smile and nods, focusing back on his work.]", "pictures/CoffeeBlur.png", [16]),
            #Bad Option Choosen
            txtImgOptNameSndAff("Still the bookworm, I see. Ever thought of looking up from those books?", "pictures/CoffeeShop.png", [14], name),
            txtImgOptNameSndAff("Uh, yeah, I guess... Just a lot to cover.", "pictures/CoffeeShop.png", [15], "Adam Cmith"),
            txtImgOptNameSndAff("[He looks a bit hurt and self-conscious, turning back to his notes.]", "pictures/CoffeeBlur.png", [16]),
            #Day 1 End Complete Gramma check
            #Start Day 2
            txtImgOptNameSndAff("Day 2: Unexpected Study Group with a Twist ", "pictures/CoffeeBlur.png", [17]),
            txtImgOptNameSndAff("[You were invited to join a study group for an upcoming major exam. The study group is scheduled to meet at a quiet location on campus, known for its serene atmosphere and conducive study environment.]", "pictures/CoffeeBlur.png", [18]),
            txtImgOptNameSndAff("[You enter the room and notice Adam.]", "pictures/CoffeeShop.png", [19]),
            txtImgOptNameSndAff("Thought: Wow, Adam's here too? That's unexpected. It's nice to see a familiar face, though.", "pictures/CoffeeShop.png", [{"text": "Approach Adam with a smile and express happiness to see him.", "nextSceneIndex": 20, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Greet the entire group, including Adam, but focus on the study material.", "nextSceneIndex": 26, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Act surprised and question Adam's presence in the study group.", "nextSceneIndex": 29, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            txtImgOptNameSndAff("Adam, what a pleasant surprise to see you here!", "pictures/CoffeeShop.png", [21], name),
            txtImgOptNameSndAff(f"Hey, {name}! I didn't know you were in this study group. Great to have you with us!", "pictures/CoffeeShop.png", [22], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam seems genuinely happy to see her, creating a warm and friendly atmosphere for the study session.]", "pictures/CoffeeShop.png", [23]),
            txtImgOptNameSndAff("Hey Adam, is this seat next to you taken?", "pictures/CoffeeShop.png", [24], name),
            txtImgOptNameSndAff("No, it's free. Come sit here!", "pictures/CoffeeShop.png", [25], "Adam Cmith"),
            txtImgOptNameSndAff("[They sit together, and as the study session progresses, they find themselves laughing and enjoying the atmosphere, blending productive study time with enjoyable conversation. This shared experience fosters a warm and friendly bond between them.] ", "pictures/CoffeeBlur.png", [32]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("Hi everyone! Ready to crack these chapters?", "pictures/CoffeeShop.png", [27], name),
            txtImgOptNameSndAff("Definitely. Let's make the most of this session.", "pictures/CoffeeShop.png", [28], "Adam Cmith and friends"),
            txtImgOptNameSndAff("[The group, including Adam, acknowledges her, and they all settle into a productive study rhythm.]", "pictures/CoffeeBlur.png", [32]),
            #Bad Option Choosen
            txtImgOptNameSndAff("Adam? I didn't expect to see you here. Are you sure you're in the right group?", "pictures/CoffeeShop.png", [30], name),
            txtImgOptNameSndAff("Yeah, I've been part of this group for a while. Just focusing on my studies.", "pictures/CoffeeShop.png", [31], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam seems a bit taken aback by her reaction, creating a slightly awkward tension in the group.] ", "pictures/CoffeeBlur.png", [32]),
            #Day 2 End Complete Gramma Check
            #Start Day 3
            txtImgOptNameSndAff("Day 3: Campus Garden Discovery", "pictures/CoffeeBlur.png", [33]),
            txtImgOptNameSndAff("[You, seeking a quiet spot to relax and clear your mind, stumble upon a hidden garden on campus. This tranquil oasis is filled with colorful flowers, lush greenery, and the soothing sound of a small fountain.]", "pictures/CoffeeBlur.png", [34]),
            txtImgOptNameSndAff("[You wander around and see Adam holding a camera.]", "pictures/CoffeeShop.png", [35]),
            txtImgOptNameSndAff("Thought: That's Adam... I didn't know he had an interest in photography. He seems so peaceful here." , "pictures/CoffeeShop.png", [{"text": "Approach and express interest in his secret hobby", "nextSceneIndex": 36, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Watch Adam silently at a distance and not disturb him.", "nextSceneIndex": 43, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Walk up to Adam and joke about his hobby.", "nextSceneIndex": 45, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            txtImgOptNameSndAff("Hey, Adam, this is a beautiful spot. I had no idea you were into photography. Can I see what you've captured?", "pictures/CoffeeShop.png", [37], name),
            txtImgOptNameSndAff(f"Oh, hi {name}! Sure, take a look. I just started last week so don’t expect much.", "pictures/CoffeeShop.png", [38], "Adam Cmith"),
            txtImgOptNameSndAff("No way! These are so beautiful!", "pictures/CoffeeShop.png", [39], name),
            txtImgOptNameSndAff("[They share a moment, appreciating the garden and his work.]", "pictures/CoffeeShop.png", [40]),
            txtImgOptNameSndAff("Hey, can you take a picture of me? Make sure I look good, ok?", "pictures/CoffeeShop.png", [41], name),
            txtImgOptNameSndAff("Of course, move here; these flowers really complement your outfit.", "pictures/CoffeeShop.png", [42], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam took a dozen pictures as you posed. They enjoy this moment together in the beautiful garden.]", "pictures/CoffeeBlur.png", [48]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("Thought: I shouldn't interrupt his moment of creativity. It's nice to see him so absorbed in his passion.", "pictures/CoffeeShop.png", [44], name),
            txtImgOptNameSndAff("[You enjoy the garden on your own, respecting his space. Adam never noticed that you were there.]", "pictures/CoffeeBlur.png", [48]),
            #Bad Option Choosen
            txtImgOptNameSndAff("Since when are you into photography? The camera does not fit you at all, haha.", "pictures/CoffeeShop.png", [46], name),
            txtImgOptNameSndAff("Ha ha ha… [Dry laugh] ", "pictures/CoffeeShop.png", [47], "Adam Cmith"),
            txtImgOptNameSndAff("[You keep teasing Adam, making him feel insecure about his secret hobby.]", "pictures/CoffeeBlur.png", [48]),
            #Day 3 End Gramma Check Complete
            #Start Day 4
            txtImgOptNameSndAff("Day 4: Volunteering Together at a Dog Shelter", "pictures/CoffeeBlur.png", [49]),
            txtImgOptNameSndAff("[You receive an unexpected text from Adam inviting you to join him in volunteering at a local dog shelter. It’s been years since we volunteered at this shelter together.]", "pictures/CoffeeBlur.png", [50]),
            txtImgOptNameSndAff("Text: Hey, I'm volunteering at the dog shelter this weekend. It’s the one that we used to go to together years ago; do you want to join me?", "pictures/CoffeeShop.png", [51], "Adam Cmith"),
            txtImgOptNameSndAff("Thought: Volunteering at a dog shelter with Adam... It's really been a while since we went together." , "pictures/CoffeeShop.png", [{"text": "Enthusiastically accept the invitation.", "nextSceneIndex": 52, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Politely decline due to being busy.", "nextSceneIndex": 59, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Leave the invitation on read without responding.", "nextSceneIndex": 62, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            txtImgOptNameSndAff("Text: That sounds amazing, Adam! I'd love to join you. What time should we meet?","pictures/CoffeeShop.png", [53], name),
            txtImgOptNameSndAff("Text: Great! Let's meet at 10 AM. It'll be fun!", "pictures/CoffeeShop.png", [54], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam is pleased with her enthusiastic response, and they look forward to spending a fulfilling day at the shelter, bonding over their love for animals.]", "pictures/CoffeeShop.png", [55]),
            txtImgOptNameSndAff("[They meet at the dog shelter.]", "pictures/CoffeeShop.png", [56]),
            txtImgOptNameSndAff("You remember Buster, that little beagle we took care of last time? I heard he was adopted by a lovely family. It's bittersweet, isn't it? I'm happy to see him find a home, but I also miss him...", "pictures/CoffeeShop.png", [57], name),
            txtImgOptNameSndAff("Yeah, I'm glad he found a good home. It's these moments, isn't it? Seeing them happy and loved is what makes all of this so worthwhile.", "pictures/CoffeeShop.png", [58], "Adam Cmith"),
            txtImgOptNameSndAff("[They talk and laugh over memories of their past volunteer days. These memories reveal a deeper, long-standing bond between them.]", "pictures/CoffeeBlur.png", [65]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("Text: I'd really like to join you, Adam, but I'm swamped with work this weekend. Rain check?", "pictures/CoffeeShop.png", [60], name),
            txtImgOptNameSndAff("Text: No worries, I understand. Let's plan for another time!", "pictures/CoffeeShop.png", [61], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam respects her busy schedule, and they both express a willingness to plan something together in the future.]", "pictures/CoffeeBlur.png", [65]),
            #Bad Option Choosen
            txtImgOptNameSndAff("Thought: Well, I am not really free this weekend... Let me check my schedule again so I can confirm with him.", "pictures/CoffeeShop.png", [63], name),
            txtImgOptNameSndAff("[You completely forgot to text him back, leaving him on read.] ", "pictures/CoffeeShop.png", [64]),
            txtImgOptNameSndAff("[Adam feels ignored and is unsure about your interest in spending time with him, leading to potential awkwardness in future interactions.]", "pictures/CoffeeBlur.png", [65]),
            #Day 4 End Gramma Check Complete
            #Start Day 5
            txtImgOptNameSndAff("Day 5: Photography Exhibition ", "pictures/CoffeeBlur.png", [66]),
            txtImgOptNameSndAff("[The Photographic Circle Club is hosting a photography exhibition showcasing the work of students. You are interested in art and photography and decide to visit the exhibition. Upon your arrival, you are surprised to discover that Adam has his own photography work displayed.]", "pictures/CoffeeBlur.png", [67]),
            txtImgOptNameSndAff("Thought: I had no idea Adam was into photography to this extent. His pictures are really impressive." , "pictures/CoffeeShop.png", [{"text": "Express admiration for his work and ask him about his inspiration.", "nextSceneIndex": 68, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Compliment his work politely and browse other exhibits.", "nextSceneIndex": 74, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Make a light-hearted joke about his serious photographs.", "nextSceneIndex": 77, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], name),
            #Good Option Choosen
            txtImgOptNameSndAff("Adam, your photographs are amazing! What inspires you to capture these moments?","pictures/CoffeeShop.png", [69], name),
            txtImgOptNameSndAff("Thanks! I find inspiration in everyday life, the small moments that tell a story. It means a lot that you appreciate it.", "pictures/CoffeeShop.png", [70], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam is touched by her genuine interest and opens up about his passion for photography, leading to a deep and meaningful conversation.]", "pictures/CoffeeShop.png", [71]),
            txtImgOptNameSndAff("Hey, this is the picture you took for me in the garden!?", "pictures/CoffeeShop.png", [72], name),
            txtImgOptNameSndAff("Yeah, that is one of my favorites and best works; it’s so captivating...", "pictures/CoffeeShop.png", [73], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam and you walk into the exhibition together, enjoying each other’s company. Their relationship has deepened.] ", "pictures/CoffeeBlur.png", [80]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("Nice work on these photos, Adam. You've got a good eye.", "pictures/CoffeeShop.png", [75], name),
            txtImgOptNameSndAff("Thanks, Feel free to look around the rest.", "pictures/CoffeeShop.png", [76], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam appreciates your compliment, but their interaction remains on a surface level as you move on to view other artworks.]", "pictures/CoffeeBlur.png", [80]),
            #Bad Option Choosen
            txtImgOptNameSndAff("These photos aren’t bad. Did you really take these yourself?", "pictures/CoffeeShop.png", [78], name),
            txtImgOptNameSndAff("Yeah, well, I have been practicing a lot and thought people would like it more...", "pictures/CoffeeShop.png", [79], "Adam Cmith"),
            txtImgOptNameSndAff("[Adam feels slightly misunderstood and retreats into his shell, creating a subtle distance between them.]", "pictures/CoffeeBlur.png", [80]),
            #Day 5 End Gramma Check Complete
            #Start Day 6
            txtImgOptNameSndAff("Day 6: Romantic Beach Walk", "pictures/CoffeeBlur.png", [81], None, None, {"NPC": ADAMCMITH, "comparison": SMALLER, "amount": 3, "altSceneIndex": 116 }),
            txtImgOptNameSndAff("[You and Adam decide to take an evening walk along the beach. The sound of the waves, the gentle sea breeze, and the stunning sunset create a perfect romantic setting.]", "pictures/CoffeeBlur.png", [82]),
            txtImgOptNameSndAff("[As they walk side by side on the sandy shore, the fading sunlight casts a warm glow, creating a serene and intimate atmosphere.]" , "pictures/CoffeeShop.png", [{"text": "Open up about feelings.", "nextSceneIndex": 83, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Enjoy the walk in comfortable silence.", "nextSceneIndex": 89, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Make a casual remark about the setting and emphasize their friendship.", "nextSceneIndex": 91, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}]),
            #Good Option Choosen
            txtImgOptNameSndAff("Adam, I'm really glad we're here together. There's something special about this moment, don't you think?","pictures/CoffeeShop.png", [84], name),
            txtImgOptNameSndAff("I was thinking the same. It feels like everything's just right.", "pictures/CoffeeShop.png", [85], "Adam Cmith"),
            txtImgOptNameSndAff("[This honest exchange brings them closer, allowing their relationship to progress into something more than just friendship.]", "pictures/CoffeeShop.png", [86]),
            txtImgOptNameSndAff("You know, I've always found the ocean to be calming, but tonight, it feels even more special. Maybe it's the company.", "pictures/CoffeeShop.png", [87], "Adam Cmith"),
            txtImgOptNameSndAff("I've always loved the beach too. It's like all your worries just wash away with the tide.", "pictures/CoffeeShop.png", [88], name),
            txtImgOptNameSndAff("[They sit in silence for a moment, simply enjoying each other's presence. As the sun sets, their expressions soften in the twilight. A brief exchange of glances at each other—it's their little special moment.] ", "pictures/CoffeeBlur.png", [94]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("Thought: Sometimes, words aren't needed. This quiet companionship says it all.", "pictures/CoffeeShop.png", [90], name),
            txtImgOptNameSndAff("[They continue walking, appreciating the beauty around them and each other's company without the need for words.]", "pictures/CoffeeBlur.png", [94]),
            #Bad Option Choosen
            txtImgOptNameSndAff("Nice weather for a beach walk, isn't it? It’s good to have a best friend to do these things with.", "pictures/CoffeeShop.png", [92], name),
            txtImgOptNameSndAff("Yeah, it's pretty great...", "pictures/CoffeeShop.png", [93], "Adam Cmith"),
            txtImgOptNameSndAff("[The conversation stays on the surface; however, Adam is reminded of his position as just a good friend.]", "pictures/CoffeeBlur.png", [94]),
            #Day 6 End Gramma Check Complete
            #Start Day 7
            txtImgOptNameSndAff("Day 7: Memory Lane at the Café", "pictures/CoffeeBlur.png", [95], None, None,{"NPC": ADAMCMITH, "comparison": SMALLER, "amount": 3, "altSceneIndex": 116 }),
            txtImgOptNameSndAff("[You decide to visit the café, reflecting on the incredible week you had. As you walk in, you are surprised and delighted to find Adam there, sitting at the same table where they first reconnected.]", "pictures/CoffeeBlur.png", [96]),
            txtImgOptNameSndAff("Thought: This feels like déjà vu, but so much has changed since that first day.", "pictures/CoffeeShop.png", [97], name),
            txtImgOptNameSndAff("[She approaches Adam, who looks up and smiles warmly. As she sat down, Adam exclaimed in his jolly voice...]", "pictures/CoffeeBlur.png", [98]),
            txtImgOptNameSndAff("Look what I got here, he says, pulling out his camera. I took some pictures during our beach walk yesterday." , "pictures/CoffeeShop.png", [{"text": "Express love for the photos and appreciation for his thoughtfulness.", "nextSceneIndex": 99, "affection": {"affectedNPC": ADAMCMITH, "change": INCREASE}}, {"text": "Leave a quick comment on his photo and move on.", "nextSceneIndex": 108, "affection": {"affectedNPC": ADAMCMITH, "change": NEUTRAL}}, {"text": "Acknowledge the photos but express discomfort at being photographed so much.", "nextSceneIndex": 111, "affection": {"affectedNPC": ADAMCMITH, "change": DECREASE}}], "Adam Cmith"),
            #Good Option Choosen
            txtImgOptNameSndAff("These are beautiful, Adam! Although did you take photos of anything else, or was I your only subject?","pictures/CoffeeShop.png", [100], name),
            txtImgOptNameSndAff("Honestly, you were the most picturesque of all the surroundings. How could I focus on anything else?", "pictures/CoffeeShop.png", [101], "Adam Cmith"),
            txtImgOptNameSndAff("[You appreciated the comment and felt a warm feeling in your heart.]", "pictures/CoffeeShop.png", [102]),
            txtImgOptNameSndAff("Wow, I never thought you could say something like that; you have grown, don’t you?", "pictures/CoffeeShop.png", [103], name),
            txtImgOptNameSndAff("Well, I am tired of waiting, so how do you think of me?", "pictures/CoffeeShop.png", [104], "Adam Cmith"),
            txtImgOptNameSndAff("[The protagonist gives a slight pause, then, with a soft voice, she asks...] ", "pictures/CoffeeBlur.png", [105]),
            txtImgOptNameSndAff("Will you go to prom with me?", "pictures/CoffeeShop.png", [106], name),
            txtImgOptNameSndAff("Of course I will.", "pictures/CoffeeShop.png", [107], "Adam Cmith"),
            txtImgOptNameSndAff("[Amidst the bustling coffee shop, it seemed as though there were only the two of them. The burden that had rested on their chests had lifted, and they eagerly anticipated the arrival of tomorrow.] ", "pictures/CoffeeBlur.png", [114]),
            #Neutral Option Choosen
            txtImgOptNameSndAff("You really do have talent here, Adam. These are very nice. Let's talk more later. I have a meeting at 5. Bye.", "pictures/CoffeeShop.png", [109], name),
            txtImgOptNameSndAff("Thank, he you later.", "pictures/CoffeeShop.png", [110], "Adam Cmith"),
            txtImgOptNameSndAff("[Their conversation is brief and plain. No further development really happens in the interaction.]", "pictures/CoffeeBlur.png", [116]),
            #Bad Option Choosen
            txtImgOptNameSndAff("These are nice, but... it's a little weird that you took so many pictures of me, don't you think?", "pictures/CoffeeShop.png", [112], name),
            txtImgOptNameSndAff("Oh, I didn't mean to make you uncomfortable. I just thought you looked really happy and wanted to capture that...", "pictures/CoffeeShop.png", [113], "Adam Cmith"),
            txtImgOptNameSndAff("[The mood becomes awkward. Adam feels misunderstood, and the protagonist senses that she might have hurt his feelings.]", "pictures/CoffeeBlur.png", [116]),
            #Day 7 End
            #Good ending index link to 114
            txtImgOptNameSndAff("[You and Adam go to prom to gether]", "pictures/dog.png", [115]),
            txtImgOptNameSndAff("[Congratulations You Win]", "pictures/dog.png", [115]),
            #Bad ending index link 116
            txtImgOptNameSndAff("Adam felt distence from you", "pictures/dog.png", [117]),
            txtImgOptNameSndAff("You Lose", "pictures/dog.png", [117]),
            




            txtImgOptNameSndAff("Day end successful &_&", "pictures/dog.png", [4]),
            txtImgOptNameSndAff("(Bad)", "pictures/dog.png", [4]),
            txtImgOptNameSndAff("NOOO WE ARE GONNA BE LATE, LETS GO NOW!", "pictures/dog.png", [5], "Mia", "sounds/xm2.wav"),
            txtImgOptNameSndAff("", "pictures/dog.png", [{"text": "Scene 6", "nextSceneIndex": 6, "affection": {"affectedNPC": XIAOMING, "change": INCREASE}}, {"text": "Scene 7", "nextSceneIndex": 7, "affection": {"affectedNPC": XIAOMING, "change": DECREASE}}]),
            txtImgOptNameSndAff("SCENE 6!", "pictures/dog.png", [], "YAY", "sounds/animalese (1).wav", {"NPC": XIAOMING, "comparison": SMALLER, "amount": 5, "altSceneIndex": 2 }), 
            txtImgOptNameSndAff("SCENE 7!", "pictures/dog.png", [4], "YAY", "sounds/animalese (1).wav"),
            ]