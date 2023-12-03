# ... [Your previous imports and NPC creations] ...
import warnings
import winsound
from tkinter import *

from classes import *
from jungcook import *

warnings.filterwarnings('ignore')
# Creation of Johnny Sin character
JOHNNYSIN = NPC("Johnny Sin")

# Constants for affection changes
DECREASE = "DECREASE"
INCREASE = "INCREASE"
NEUTRAL = "NEUTRAL"

# Affection score thresholds
TOO_LOW_AFFECTION = -10
NORMALLY_HIGH_AFFECTION = 10
SUPER_HIGH_AFFECTION = 20
ABNORMALLY_LOW_AFFECTION = -20

# Initialize Johnny Sin's affection score
affection_score = 0

# Function to update affection score
def update_affection(change):
    global affection_score
    if change == INCREASE:
        affection_score += 1
    elif change == DECREASE:
        affection_score -= 1

# Function to determine the game ending based on affection score
def determine_ending():
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

# Function to display the abnormally low ending
def show_abnormally_low_ending():
    # Replace with actual code for the ending
    print("Johnny reveals his true, sinister nature...")

# Function to display the too low ending
def show_too_low_ending():
    # Replace with actual code for the ending
    print("Johnny expresses disappointment...")

# Function to display the normal ending
def show_normal_ending():
    # Replace with actual code for the ending
    print("Johnny thanks you for the time spent together...")

# Function to display the high affection ending
def show_high_affection_ending():
    # Replace with actual code for the ending
    print("Johnny confesses his feelings for you...")

# Function to display the super high affection ending
def show_super_high_affection_ending():
    # Replace with actual code for the ending
    print("Johnny reveals an obsessive side...")

# Function to trigger the end game based on the affection score
def end_game():
    ending = determine_ending()
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

# Function to run Johnny Sin's story
def JS(name):
    diag = [
        ("Introduction to Johnny's story", "picture/path.png", [1]),
        ("Johnny approaches you...", "picture/path2.png", [{"text": "Respond positively.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}, {"text": "Respond neutrally.", "nextSceneIndex": 4, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}}, {"text": "Respond negatively.", "nextSceneIndex": 5, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}], name),
        ("(You're buried in books at the SUTD library, preparing for your final exams.)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav"),
        ("Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", "pictures/libraryjohnny2.png", [2], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/libraryjohnny2.png", [{"text": "Sure, the architecture section is that way. But beware, the librarian is a stealthy guardianSure, the architecture section is that way. But beware, the librarian is a stealthy guardian.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Can't you see I'm trying to decode the mysteries of the universe here? Ask Google, my friend", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Absolutely, fellow adventurer! Let's embark on this scholarly quest together. Post-exams, we can explore the real deal!", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}]),    
        ("Intriguing! Im digging this blend of modern and traditional vibes. Whats your major", "pictures/libraryjohnny2.png", [4],"Johnny Sin", "sounds/xm1.wav"),
        ("I'm prepping for my final exams. It's a bit overwhelming.", "pictures/libraryjohnny3.png", [5],"You", "xm2.wav"),
        ("Maybe after your exams, you could show me around the city's architectural highlights?", "pictures/libraryjohnny3.png", [6],"Johnny Sin", "sounds/xm1.wav"),          ("", "pictures/libraryjohnny2.png", [{"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "A quest for later. Now, I must return to my study dungeon.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("That sounds like a plan. It would be a nice break from all this studying.", "pictures/libraryjohnny3.png", [8], "You", "sounds/xm2.wav"),
        ("(The conversation flows smoothly, and you're both surprised at how comfortable you feel around each other. Johnny's charm and your shared interest in architecture make for a promising start.)", "pictures/libraryjohnny3.png", [10]),
        ("(The next morning in SUTD track in the late afternoon.)", "pictures/trackjohnny2.png", [11], "sounds/animalese.wav"),
        ("Hey, I noticed you yesterday at the library. I'm going for a run. Care to join me? It's a great way to unwind.", "pictures/trackjohnny1.png", [12], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/trackjohnny1.png", [{"text": "I'm not much of a runner, but why not? It might be fun. Running at sunset sounds perfect.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Running with the setting sun? Tempting, but my brain cells need me more.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "Chasing sunsets? Running isn't really my thing. I'm more of a moonlight wanderer. Go away boi", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
        ("Trust me, the view at sunset is worth it. Plus, I could use the company.", "pictures/trackjohnny1.png", [14],"Johnny Sin", "sounds/xm1.wav"),
        ("(During the run) Look at that sunset! It's like the sky's putting on a show just for us.", "pictures/sunsetjohnny2.png", [15],"Johnny Sin", "sounds/animalese.wav"),
        ("", "pictures/sunsetjohnny2.png", [{"text": "It's beautiful. I never took the time to appreciate it like this.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It is nice. But let's not stop; we should keep our pace.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Honestly, I'm just here so I don’t get fined for skipping leg day", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("Back home, moments like these are rare. I'm glad I got to share it with you.", "pictures/sunsetjohnny2.png", [17],"Johnny Sin", "sounds/xm1.wav"),
        ("Me too, Johnny. This was unexpectedly enjoyable.", "pictures/sunsetjohnny2.png", [17], "You", "sounds/xm2.wav"), 
        ("(The run turns into a fun and light-hearted experience. Your laughter echoes in the cool evening air, and the shared moment at sunset feels special.)", "pictures/eveningjohnny1.png", [18]),
        ("(Day3, today I have Art class, with an assignment to draw a portrait.)", "pictures/classroomjohnny1.png", [19], None, "sounds/animalese.wav"),
        ("I've been thinking about the assignment, and I would like to draw your portrait. Would that be okay with you?", "pictures/classroomjohnny2.png", [20], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/classroomjohnny2.png", [{"text": "Me? Well, that's quite the compliment. That sounds like fun! I've always wanted to be someone's muse.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I guess that's fine. But I'm no Venus de Milo. Just dont expect a masterpiece.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I'm not really comfortable being your subject, sorry.Me? Why not draw the cafeteria lady instead? She's got character", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
        ("You have a certain...expression, it's captivating. Like the Mona Lisa.", "pictures/monalisa.png", [22],"Johnny Sin", "sounds/xm1.wav"),
        ("That's quite the compliment. I guess I can't say no to being compared to a masterpiece.", "pictures/monalisa.png", [23], "You", "sounds/xm2.wav"),
        ("(While drawing) You know, this reminds me of a scene from Titanic. Minus the drama, of course.", "pictures/classroomjohnny2.png", [24],"Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/classroomjohnny2.png", [{"text": "Well, let's keep it that way. No icebergs in Singapore, thankfully.", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just make sure you get my good side!", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope you're better at drawing than making movie references. Keep the charm, Picasso. Lets not turn this into a meme", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("Just a sunny island with a sunny girl.", "pictures/classroomjohnny2.png", [26],"Johnny Sin", "sounds/xm1.wav"),
        ("(The session is filled with playful banter. Johnny's focus on capturing your essence is flattering, and the mood is reminiscent of a classic romantic movie.)", "pictures/classroomjohnny1.png", [27]),
        ("(Sports stadium, buzzing with excitement.)", "pictures/stadiumjohnny1.png", [28], None, "sounds/animalese.wav"),
        ("I'm really glad you came. Your support means a lot to me.", "pictures/stadiumjohnny2.png", [29], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/stadiumjohnny2.png", [{"text": "I wouldn't miss it. Seeing you run is inspiring. I brought a banner to cheer you on. Go Johnny!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I'm curious to see how fast you run. Good luck!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I just hope it doesn't drag on too long.", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
        ("Just knowing you're here in the crowd makes me want to run faster.", "pictures/stadiumjohnny2.png", [31],"Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/stadiumjohnny2.png", [{"text": "Well, then I expect nothing less than a win from you!", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just focus on your race. Don’t worry about the crowd.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope this doesnt take too long. Ive got a date with Netflix later.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("(The energy of the competition is electric. As Johnny races, you find yourself fully invested in his success. His win feels like a shared victory.)", "pictures/stadiumjohnny3.png", [33]),
        ("(Changi City Point mall, bustling with activity.)", "pictures/ccp1.png", [34], None, "sounds/animalese.wav"),
        ("This mall is huge! Where should we start?", "pictures/ccp2.png", [35], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/ccp2.png", [{"text": "How about some window shopping? There are some great clothing stores here.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Maybe grab a bite first? I'm a bit hungry.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Navigating through crowds? That's a hard pass. Got a teleporter handy?", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's explore together and find the best spot in CCP!", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
        ("Sounds good. Maybe you can help me pick out something that screams 'Singapore'!", "pictures/ccp2.png", [37],"Johnny Sin", "sounds/xm2.wav"),
        ("(In a café) This coffee is great, but not as sweet as your company.", "pictures/cafejohnny1.png", [38],"Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/cafejohnny1.png", [    {"text": "Smooth line, Johnny. Been practicing?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "You and your compliments! But thanks, the coffee is good.", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "BRUH are you always this cheesy?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("Maybe a little. But only the best for today.", "pictures/cafejohnny1.png", [40],"Johnny Sin", "sounds/xm2.wav"),
        ("(Before the movie) I'm glad we did this. Today was perfect.", "pictures/cafejohnny1.png", [41],"Johnny Sin", "sounds/xm1.wav"),
        ("Me too, Johnny. It's nice to just relax and enjoy the day.", "pictures/cafejohnny1.png", [42], "You", "sounds/xm2.wav"),
        ("(The day is a mix of casual shopping, sipping coffee, and watching a movie. It's comfortable and easy, with a hint of budding romance.)", "pictures/cafejohnny1.png", [43]),
        ("(University observatory, under a starlit sky.)", "pictures/star1.png", [44], None, "sounds/animalese.wav"),
        ("These stars... they're like nothing I've seen back home.", "pictures/star1.png", [45], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/star1.png", [{"text": "They have a way of making everything seem so possible, so magical.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Yeah, it's a clear night. Perfect for star-gazing.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "I'm more of a city lights person, but this is okay.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},    {"text": "It's like they're shining just for us tonight.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
        ("You know, I've been meaning to tell you something. These past few days with you have been the highlight of my trip.", "pictures/star1.png", [47],"Johnny Sin", "sounds/xm1.wav"),
        ("Really? I've enjoyed our time together too.", "pictures/star1.png", [48], "You", "sounds/xm2.wav"),
        ("I feel like there's something special between us. I know my time here is limited, but I had to let you know.", "pictures/star1.png", [49],"Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/star1.png", [{"text": "Johnny, I feel it too. Let's just enjoy this moment, under the stars.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "That's really sweet, Johnny. I'm glad we met.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Easy there, cowboy. We are just two astronauts on a space walk.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ("(The night is filled with heartfelt confessions and quiet understanding. The stars above seem to bless this new, uncertain yet hopeful chapter in your lives.)", "pictures/star1.png", [51]),
        ("(A quiet spot on campus, preparing to say goodbye.)", "pictures/star1.png", [52], None, "sounds/animalese.wav"),
        ("This week with you has been the best part of my exchange. I wish it didn't have to end.", "pictures/star1.png", [53], "Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/star1.png", [{"text": "I feel the same way, Johnny. This week was unforgettable.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It's been great, hasn't it? We made some good memories.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "All good things come to an end, rollercoasters are fun, but eventually, you have to get off", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's make a promise to see each other again, no matter what.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"), 
        ("I hope we can keep in touch. Maybe you could visit me in the States someday?", "pictures/star1.png", [55],"Johnny Sin", "sounds/xm1.wav"),
        ("", "pictures/star1.png", [{"text": "I'd like that. It's not goodbye, just see you later.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Sure, we can try to stay in touch. Who knows what the future holds?", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "It's hard to make such promises, Johnny. But let's enjoy today.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
        ( "It's been an amazing week, Johnny Sin. Thanks for sharing it with me.", "pictures/star1.png", [57], "You", "sounds/justforfun.wav"),
                            

                     
        # ...
    ]
    return diag

end_game()
# end_game()

# ... [Rest of your code] ...
'''[txtImgOptNameSndAff("(You're buried in books at the SUTD library, preparing for your final exams.)", "pictures/libraryjohnny0.png", [1], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", "pictures/libraryjohnny2.png", [2], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/libraryjohnny2.png", [{"text": "Sure, the architecture section is that way. But beware, the librarian is a stealthy guardianSure, the architecture section is that way. But beware, the librarian is a stealthy guardian.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Can't you see I'm trying to decode the mysteries of the universe here? Ask Google, my friend", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Absolutely, fellow adventurer! Let's embark on this scholarly quest together. Post-exams, we can explore the real deal!", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}]),    
                     txtImgOptNameSndAff("Intriguing! Im digging this blend of modern and traditional vibes. Whats your major", "pictures/libraryjohnny2.png", [4],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("I'm prepping for my final exams. It's a bit overwhelming.", "pictures/libraryjohnny3.png", [5],"You", "xm2.wav"),
                     txtImgOptNameSndAff("Maybe after your exams, you could show me around the city's architectural highlights?", "pictures/libraryjohnny3.png", [6],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/libraryjohnny2.png", [{"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "A quest for later. Now, I must return to my study dungeon.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("That sounds like a plan. It would be a nice break from all this studying.", "pictures/libraryjohnny3.png", [8], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(The conversation flows smoothly, and you're both surprised at how comfortable you feel around each other. Johnny's charm and your shared interest in architecture make for a promising start.)", "pictures/libraryjohnny3.png", [10]),
                     txtImgOptNameSndAff("(The next morning in SUTD track in the late afternoon.)", "pictures/trackjohnny2.png", [11], "sounds/animalese.wav"),
                     txtImgOptNameSndAff("Hey, I noticed you yesterday at the library. I'm going for a run. Care to join me? It's a great way to unwind.", "pictures/trackjohnny1.png", [12], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/trackjohnny1.png", [{"text": "I'm not much of a runner, but why not? It might be fun. Running at sunset sounds perfect.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Running with the setting sun? Tempting, but my brain cells need me more.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "Chasing sunsets? Running isn't really my thing. I'm more of a moonlight wanderer. Go away boi", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("Trust me, the view at sunset is worth it. Plus, I could use the company.", "pictures/trackjohnny1.png", [14],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("(During the run) Look at that sunset! It's like the sky's putting on a show just for us.", "pictures/sunsetjohnny2.png", [15],"Johnny Sin", "sounds/animalese.wav"),
                     txtImgOptNameSndAff("", "pictures/sunsetjohnny2.png", [{"text": "It's beautiful. I never took the time to appreciate it like this.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It is nice. But let's not stop; we should keep our pace.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Honestly, I'm just here so I don’t get fined for skipping leg day", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Back home, moments like these are rare. I'm glad I got to share it with you.", "pictures/sunsetjohnny2.png", [17],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Me too, Johnny. This was unexpectedly enjoyable.", "pictures/sunsetjohnny2.png", [17], "You", "sounds/xm2.wav"), 
                     txtImgOptNameSndAff("(The run turns into a fun and light-hearted experience. Your laughter echoes in the cool evening air, and the shared moment at sunset feels special.)", "pictures/eveningjohnny1.png", [18]),
                     txtImgOptNameSndAff("(Day3, today I have Art class, with an assignment to draw a portrait.)", "pictures/classroomjohnny1.png", [19], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("I've been thinking about the assignment, and I would like to draw your portrait. Would that be okay with you?", "pictures/classroomjohnny2.png", [20], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/classroomjohnny2.png", [{"text": "Me? Well, that's quite the compliment. That sounds like fun! I've always wanted to be someone's muse.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I guess that's fine. But I'm no Venus de Milo. Just dont expect a masterpiece.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I'm not really comfortable being your subject, sorry.Me? Why not draw the cafeteria lady instead? She's got character", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("You have a certain...expression, it's captivating. Like the Mona Lisa.", "pictures/monalisa.png", [22],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("That's quite the compliment. I guess I can't say no to being compared to a masterpiece.", "pictures/monalisa.png", [23], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(While drawing) You know, this reminds me of a scene from Titanic. Minus the drama, of course.", "pictures/classroomjohnny2.png", [24],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/classroomjohnny2.png", [{"text": "Well, let's keep it that way. No icebergs in Singapore, thankfully.", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just make sure you get my good side!", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope you're better at drawing than making movie references. Keep the charm, Picasso. Lets not turn this into a meme", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Just a sunny island with a sunny girl.", "pictures/classroomjohnny2.png", [26],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("(The session is filled with playful banter. Johnny's focus on capturing your essence is flattering, and the mood is reminiscent of a classic romantic movie.)", "pictures/classroomjohnny1.png", [27]),
                     txtImgOptNameSndAff("(Sports stadium, buzzing with excitement.)", "pictures/stadiumjohnny1.png", [28], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("I'm really glad you came. Your support means a lot to me.", "pictures/stadiumjohnny2.png", [29], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/stadiumjohnny2.png", [{"text": "I wouldn't miss it. Seeing you run is inspiring. I brought a banner to cheer you on. Go Johnny!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "I'm curious to see how fast you run. Good luck!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I just hope it doesn't drag on too long.", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]),
                     txtImgOptNameSndAff("Just knowing you're here in the crowd makes me want to run faster.", "pictures/stadiumjohnny2.png", [31],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/stadiumjohnny2.png", [{"text": "Well, then I expect nothing less than a win from you!", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Just focus on your race. Don’t worry about the crowd.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "I hope this doesnt take too long. Ive got a date with Netflix later.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("(The energy of the competition is electric. As Johnny races, you find yourself fully invested in his success. His win feels like a shared victory.)", "pictures/stadiumjohnny3.png", [33]),
                     txtImgOptNameSndAff("(Changi City Point mall, bustling with activity.)", "pictures/ccp1.png", [34], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("This mall is huge! Where should we start?", "pictures/ccp2.png", [35], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/ccp2.png", [{"text": "How about some window shopping? There are some great clothing stores here.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Maybe grab a bite first? I'm a bit hungry.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Navigating through crowds? That's a hard pass. Got a teleporter handy?", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's explore together and find the best spot in CCP!", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
                     txtImgOptNameSndAff("Sounds good. Maybe you can help me pick out something that screams 'Singapore'!", "pictures/ccp2.png", [37],"Johnny Sin", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(In a café) This coffee is great, but not as sweet as your company.", "pictures/cafejohnny1.png", [38],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/cafejohnny1.png", [    {"text": "Smooth line, Johnny. Been practicing?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "You and your compliments! But thanks, the coffee is good.", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "BRUH are you always this cheesy?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("Maybe a little. But only the best for today.", "pictures/cafejohnny1.png", [40],"Johnny Sin", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(Before the movie) I'm glad we did this. Today was perfect.", "pictures/cafejohnny1.png", [41],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Me too, Johnny. It's nice to just relax and enjoy the day.", "pictures/cafejohnny1.png", [42], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("(The day is a mix of casual shopping, sipping coffee, and watching a movie. It's comfortable and easy, with a hint of budding romance.)", "pictures/cafejohnny1.png", [43]),
                     txtImgOptNameSndAff("(University observatory, under a starlit sky.)", "pictures/star1.png", [44], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("These stars... they're like nothing I've seen back home.", "pictures/star1.png", [45], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "They have a way of making everything seem so possible, so magical.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},    {"text": "Yeah, it's a clear night. Perfect for star-gazing.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},    {"text": "I'm more of a city lights person, but this is okay.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},    {"text": "It's like they're shining just for us tonight.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"),
                     txtImgOptNameSndAff("You know, I've been meaning to tell you something. These past few days with you have been the highlight of my trip.", "pictures/star1.png", [47],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("Really? I've enjoyed our time together too.", "pictures/star1.png", [48], "You", "sounds/xm2.wav"),
                     txtImgOptNameSndAff("I feel like there's something special between us. I know my time here is limited, but I had to let you know.", "pictures/star1.png", [49],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "Johnny, I feel it too. Let's just enjoy this moment, under the stars.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "That's really sweet, Johnny. I'm glad we met.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "Easy there, cowboy. We are just two astronauts on a space walk.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff("(The night is filled with heartfelt confessions and quiet understanding. The stars above seem to bless this new, uncertain yet hopeful chapter in your lives.)", "pictures/star1.png", [51]),
                     txtImgOptNameSndAff("(A quiet spot on campus, preparing to say goodbye.)", "pictures/star1.png", [52], None, "sounds/animalese.wav"),
                     txtImgOptNameSndAff("This week with you has been the best part of my exchange. I wish it didn't have to end.", "pictures/star1.png", [53], "Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "I feel the same way, Johnny. This week was unforgettable.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "It's been great, hasn't it? We made some good memories.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "All good things come to an end, rollercoasters are fun, but eventually, you have to get off", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},{"text": "Let's make a promise to see each other again, no matter what.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],"You"), 
                     txtImgOptNameSndAff("I hope we can keep in touch. Maybe you could visit me in the States someday?", "pictures/star1.png", [55],"Johnny Sin", "sounds/xm1.wav"),
                     txtImgOptNameSndAff("", "pictures/star1.png", [{"text": "I'd like that. It's not goodbye, just see you later.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},{"text": "Sure, we can try to stay in touch. Who knows what the future holds?", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},{"text": "It's hard to make such promises, Johnny. But let's enjoy today.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],"You"),
                     txtImgOptNameSndAff( "It's been an amazing week, Johnny Sin. Thanks for sharing it with me.", "pictures/star1.png", [57], "You", "sounds/justforfun.wav"),
                     txtImgOptNameSndAff( end_game(affection_score), "pictures/star1.png", [57], "You", "sounds/justforfun.wav"),
                     end_game(affection_score)]))'''