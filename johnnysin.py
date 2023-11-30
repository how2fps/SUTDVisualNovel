chatButton4 = Button(selectFrame, text=NPC.getName(),  image = image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20))
                     chatButton4.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)
                     # Add a label for the character description
                     description4 = Label(selectFrame, text="An exchange student from the USA with\na heart as warm as his home state.\n\nHis charm lies in his adventurous spirit\nand his willingness to immerse\nhimself in new experiences.\n\n-Johnny's enthusiasm is infectious\n\n-He brings a touch of foreign intrigue\nand a lot of friendly warmth.\n\nJoin him on his journey of cultural exchange.", bg="#ed8c8c",font=("Comic Sans MS", 15))
                     description4.grid(row=row, column=column+2, sticky=W+E)
                     johnny_dialogues = []
                     chatButton1 = Button(selectFrame, text=NPC.getName(), image= image, compound=TOP,  borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda i=i :createScenes(window, selectFrame,
                            [ txtImgOptNameSndAff(
            "(You're buried in books at the SUTD library, preparing for your final exams.)", 
            "pictures/dog.png", 
            [1], 
            None, 
            "sounds/animalese.wav"
        ),
        txtImgOptNameSndAff(
            "Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", 
            "pictures/dog.png", 
            [2], 
            "Johnny Sin", 
            "sounds/animalese.wav"
        ),
        txtImgOptNameSndAff(
            "", 
            "pictures/dog.png", 
            [
                {"text": "You might find what you need in the architecture section. It's over there.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                {"text": "I'm really busy with my own studies. Maybe ask the librarian?", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},
                {"text": "I'd love to help! There's also a great documentary on this. We could watch it together sometime. Are you an architecture major?", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}
            ]
        ),
        
     txtImgOptNameSndAff(
        "Yes, and I'm fascinated by the blend of modern and traditional designs here. What about you? What are you studying so intently?", 
        "pictures/dog.png", 
        [4],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "I'm prepping for my final exams. It's a bit overwhelming.", 
        "pictures/dog.png", 
        [5],
        "You", 
        "sounds/yourvoice.wav"
    ),
    txtImgOptNameSndAff(
        "Maybe after your exams, you could show me around the city's architectural highlights?", 
        "pictures/dog.png", 
        [6],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
 txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I'm not sure, I'll be pretty busy even after exams.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "That sounds like a plan. It would be a nice break from all this studying.", 
        "pictures/dog.png", 
        [8], 
        "You", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(The conversation flows smoothly, and you're both surprised at how comfortable you feel around each other. Johnny's charm and your shared interest in architecture make for a promising start.)", 
        "pictures/dog.png", 
        [10]
    ),
    txtImgOptNameSndAff(
        "(The next morning in SUTD track in the late afternoon.)", 
        "pictures/dog.png", 
        [11], 
        
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "Hey, I noticed you yesterday at the library. I'm going for a run. Care to join me? It's a great way to de-stress.", 
        "pictures/dog.png", 
        [12], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "I'm not much of a runner, but why not? It might be fun. Running at sunset sounds perfect.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Maybe another day. I'm not really up for a run right now.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "Running isn't really my thing. Maybe another time?", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ]
    ),
    txtImgOptNameSndAff(
        "Trust me, the view at sunset is worth it. Plus, I could use the company.", 
        "pictures/dog.png", 
        [14],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(During the run) Look at that sunset! It's like the sky's putting on a show just for us.", 
        "pictures/dog.png", 
        [15],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "It's beautiful. I never took the time to appreciate it like this.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "It is nice. But let's not stop; we should keep our pace.", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I'm too tired to enjoy it. Maybe we should head back?", "nextSceneIndex": 16, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "Back home, moments like these are rare. I'm glad I got to share it with you.", 
        "pictures/dog.png", 
        [17],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "Me too, Johnny. This was unexpectedly enjoyable.", 
        "pictures/dog.png", 
        [17], 
        "You", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(The run turns into a fun and light-hearted experience. Your laughter echoes in the cool evening air, and the shared moment at sunset feels special.)", 
        "pictures/dog.png", 
        [18]
    ),
    txtImgOptNameSndAff(
        "(Art class, with an assignment to draw a portrait.)", 
        "pictures/dog.png", 
        [19], 
        None, 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "I've been thinking about the assignment, and I would like to draw your portrait. Would that be okay with you?", 
        "pictures/dog.png", 
        [20], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "Me? Well, that's quite the compliment. That sounds like fun! I've always wanted to be someone's muse.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "I guess that's fine. But I'm not sure I'm model material.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I'm not really comfortable being your subject, sorry.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ]
    ),
    txtImgOptNameSndAff(
        "You have a certain...expression, it's captivating. Like the Mona Lisa.", 
        "pictures/dog.png", 
        [22],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "That's quite the compliment. I guess I can't say no to being compared to a masterpiece.", 
        "pictures/dog.png", 
        [23], 
        "You", 
        "sounds/yourvoice.wav"
    ),
    txtImgOptNameSndAff(
        "(While drawing) You know, this reminds me of a scene from Titanic. Minus the drama, of course.", 
        "pictures/dog.png", 
        [24],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "Well, let's keep it that way. No icebergs in Singapore, thankfully.", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Just make sure you get my good side!", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I hope you're better at drawing than making movie references.", "nextSceneIndex": 25, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "Just a sunny island with a sunny girl.", 
        "pictures/dog.png", 
        [26],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(The session is filled with playful banter. Johnny's focus on capturing your essence is flattering, and the mood is reminiscent of a classic romantic movie.)", 
        "pictures/dog.png", 
        [27]
    ),
     txtImgOptNameSndAff(
        "(Sports stadium, buzzing with excitement.)", 
        "pictures/dog.png", 
        [28], 
        None, 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "I'm really glad you came. Your support means a lot to me.", 
        "pictures/dog.png", 
        [29], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "I wouldn't miss it. Seeing you run is inspiring. I brought a banner to cheer you on. Go Johnny!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "I'm curious to see how fast you run. Good luck!", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I just hope it doesn't drag on too long.", "nextSceneIndex": 30, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ]
    ),
    txtImgOptNameSndAff(
        "Just knowing you're here in the crowd makes me want to run faster.", 
        "pictures/dog.png", 
        [31],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "Well, then I expect nothing less than a win from you!", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Just focus on your race. Don’t worry about the crowd.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "Don't get too distracted by looking for me.", "nextSceneIndex": 32, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "(The energy of the competition is electric. As Johnny races, you find yourself fully invested in his success. His win feels like a shared victory.)", 
        "pictures/dog.png", 
        [33]
    ),
     txtImgOptNameSndAff(
        "(Changi City Point mall, bustling with activity.)", 
        "pictures/dog.png", 
        [34], 
        None, 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "This mall is huge! Where should we start?", 
        "pictures/dog.png", 
        [35], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "How about some window shopping? There are some great clothing stores here.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Maybe grab a bite first? I'm a bit hungry.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I don’t really like malls. They're too crowded.", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},
            {"text": "Let's explore together and find the best spot in CCP!", "nextSceneIndex": 36, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "Sounds good. Maybe you can help me pick out something that screams 'Singapore'!", 
        "pictures/dog.png", 
        [37],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(In a café) This coffee is great, but not as sweet as your company.", 
        "pictures/dog.png", 
        [38],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "Smooth line, Johnny. Been practicing?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "You and your compliments! But thanks, the coffee is good.", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "Are you always this cheesy?", "nextSceneIndex": 39, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "Maybe a little. But only the best for today.", 
        "pictures/dog.png", 
        [40],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "(Before the movie) I'm glad we did this. Today was perfect.", 
        "pictures/dog.png", 
        [41],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "Me too, Johnny. It's nice to just relax and enjoy the day.", 
        "pictures/dog.png", 
        [42], 
        "You", 
        "sounds/yourvoice.wav"
    ),
    txtImgOptNameSndAff(
        "(The day is a mix of casual shopping, sipping coffee, and watching a movie. It's comfortable and easy, with a hint of budding romance.)", 
        "pictures/dog.png", 
        [43]
    ),
    txtImgOptNameSndAff(
        "(University observatory, under a starlit sky.)", 
        "pictures/dog.png", 
        [44], 
        None, 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "These stars... they're like nothing I've seen back home.", 
        "pictures/dog.png", 
        [45], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "They have a way of making everything seem so possible, so magical.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Yeah, it's a clear night. Perfect for star-gazing.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "I'm more of a city lights person, but this is okay.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},
            {"text": "It's like they're shining just for us tonight.", "nextSceneIndex": 46, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "You know, I've been meaning to tell you something. These past few days with you have been the highlight of my trip.", 
        "pictures/dog.png", 
        [47],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "Really? I've enjoyed our time together too.", 
        "pictures/dog.png", 
        [48], 
        "You", 
        "sounds/yourvoice.wav"
    ),
    txtImgOptNameSndAff(
        "I feel like there's something special between us. I know my time here is limited, but I had to let you know.", 
        "pictures/dog.png", 
        [49],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "Johnny, I feel it too. Let's just enjoy this moment, under the stars.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "That's really sweet, Johnny. I'm glad we met.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "It's been fun, but let's not get ahead of ourselves.", "nextSceneIndex": 50, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "(The night is filled with heartfelt confessions and quiet understanding. The stars above seem to bless this new, uncertain yet hopeful chapter in your lives.)", 
        "pictures/dog.png", 
        [51]
    ),
     txtImgOptNameSndAff(
        "(A quiet spot on campus, preparing to say goodbye.)", 
        "pictures/dog.png", 
        [52], 
        None, 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "This week with you has been the best part of my exchange. I wish it didn't have to end.", 
        "pictures/dog.png", 
        [53], 
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "I feel the same way, Johnny. This week was unforgettable.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "It's been great, hasn't it? We made some good memories.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "All good things come to an end, right? That's life.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},
            {"text": "Let's make a promise to see each other again, no matter what.", "nextSceneIndex": 54, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "I hope we can keep in touch. Maybe you could visit me in the States someday?", 
        "pictures/dog.png", 
        [55],
        "Johnny Sin", 
        "sounds/animalese.wav"
    ),
    txtImgOptNameSndAff(
        "", 
        "pictures/dog.png", 
        [
            {"text": "I'd like that. It's not goodbye, just see you later.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
            {"text": "Sure, we can try to stay in touch. Who knows what the future holds?", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
            {"text": "It's hard to make such promises, Johnny. But let's enjoy today.", "nextSceneIndex": 56, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}
        ],
        "You"
    ),
    txtImgOptNameSndAff(
        "It's been an amazing week, Johnny Sin. Thanks for sharing it with me.", 
        "pictures/dog.png", 
        [57], 
        "You", 
        "sounds/animalese.wav"
    )
   


                        
                          
                            ]), padx=2, pady=2)
                     chatButton1.grid(row=row, column=column+2, sticky=N+E+W+S, padx=10, pady=10)
                     




































































# ... [Import statements and initial setup from your original code] ...

from classes import *
from tkinter import *

# Character Definitions
XIAOMING = NPC("Xiao Ming")
JUNGCOOK = NPC("JungCook")
ADAMCMITH = NPC("Adam Cmith")
JOHNNYSIN = NPC("Johnny Sin")


DECREASE = "decrease"
INCREASE = "increase"
NEUTRAL = "neutral"
BIGGER = "bigger"
SMALLER = "smaller"


picmain = "pictures/dog.png"
picofJS = "pictures/dog.png"
sound = "sounds/animalese (1).wav"
elif NPC == JOHNNYSIN:
    # Description for Johnny Sin
    description4 = Label(selectFrame, text="An exchange student from the USA with\na heart as warm as his home state.\n\nHis charm lies in his adventurous spirit\nand his willingness to immerse\nhimself in new experiences.\n\n-Johnny's enthusiasm is infectious\n\n-He brings a touch of foreign intrigue\nand a lot of friendly warmth.\n\nJoin him on his journey of cultural exchange.", bg="#ed8c8c", font=("Comic Sans MS", 15))
    description4.grid(row=row, column=column+2, sticky=W+E)

    # Dialogue list for Johnny Sin's story
    johnny_dialogues = [
        txtImgOptNameSndAff("You're buried in books at the SUTD library, preparing for your final exams.", "pictures/dog.png", [1], None, "sounds/animalese.wav"),
        txtImgOptNameSndAff("Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", "pictures/dog.png", 
                            [{"text": "You might find what you need in the architecture section. It's over there.", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                             {"text": "I'm really busy with my own studies. Maybe ask the librarian?", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}},
                             {"text": "I'd love to help! There's also a great documentary on this. We could watch it together sometime. Are you an architecture major?", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}}],
                            "Johnny Sin", "sounds/animalese.wav"),
        txtImgOptNameSndAff("Yes, and I'm fascinated by the blend of modern and traditional designs here. What about you? What are you studying so intently?", "pictures/dog.png", 
                            [{"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
                             {"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                             {"text": "I'm not sure, I'll be pretty busy even after exams.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}],
                            "You", "sounds/animalese.wav"),
        txtImgOptNameSndAff("That sounds like a plan. It would be a nice break from all this studying.", "pictures/dog.png", [4], "You", "sounds/animalese.wav"),
        txtImgOptNameSndAff("(The conversation flows smoothly, and you're both surprised at how comfortable you feel around each other. Johnny's charm and your shared interest in architecture make for a promising start.)", "pictures/dog.png", [])
    ]

    # Button to start Johnny Sin's story
    chatButton4 = Button(selectFrame, text=NPC.getName(), image=image, compound=TOP, borderwidth=2, background="#d1aa73", foreground="black", font=("roboto", 20), command=lambda: createScenes(window, selectFrame, johnny_dialogues))
    chatButton4.grid(row=row, column=column, sticky=N+E+W+S, padx=10, pady=10)

# ... [rest of the code]















# Dialogue function for Johnny Sin
def JohnnySin(name):
    diag = [
        # Day 1
        ["(Your day at university begins with an unexpected encounter.)", picmain, [1]],
        ["While walking through the campus, you bump into a new face.", picmain, [2]],
        ["Hey, I'm Johnny. I'm new here. Could you show me around?", picofJS, [3], "Johnny Sin", sound],
        ["(How do you respond to Johnny's request?)", picmain, [4]],
        ["", picmain, [{"text": "Sure, let's take a tour around the campus.", "nextSceneIndex": 5, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
                       {"text": "Sorry, I'm a bit busy right now.", "nextSceneIndex": 6, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                       {"text": "I'm not the best person for this, try asking someone else.", "nextSceneIndex": 7, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]],

        # ... [More dialogue and scenarios for Day 1] ...

        # Day 2
        ["(The next day, you encounter Johnny again in a different setting.)", picmain, [8]],
        ["You find Johnny in the library, looking lost among the bookshelves.", picmain, [9]],
        ["Hey, it's you again! Can you help me find a book on local history?", picofJS, [10], "Johnny Sin", sound],
        ["(Johnny seems to need help. How do you react?)", picmain, [11]],
        ["", picmain, [{"text": "I'd be happy to help you out.", "nextSceneIndex": 12, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
                       {"text": "I'm not sure, but the librarian could assist you.", "nextSceneIndex": 13, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                       {"text": "I really can't help right now, sorry.", "nextSceneIndex": 14, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]],

        # ... [More dialogue and scenarios for Day 2] ...

        # Day 3
        ["(On the third day, your paths cross once more.)", picmain, [15]],
        ["Johnny approaches you at the university cafe.", picmain, [16]],
        ["I've noticed you around. Do you want to grab a coffee together?", picofJS, [17], "Johnny Sin", sound],
        ["(Johnny invites you for coffee. Your response?)", picmain, [18]],
        ["", picmain, [{"text": "Coffee sounds great, let's go.", "nextSceneIndex": 19, "affection": {"affectedNPC": JOHNNYSIN, "change": INCREASE}},
                       {"text": "Maybe another time, I'm a bit busy now.", "nextSceneIndex": 20, "affection": {"affectedNPC": JOHNNYSIN, "change": NEUTRAL}},
                       {"text": "I'm not really interested, thanks though.", "nextSceneIndex": 21, "affection": {"affectedNPC": JOHNNYSIN, "change": DECREASE}}]],

        # ... [More dialogue and scenarios for Day 3] ...

        
    ]
    return diag

