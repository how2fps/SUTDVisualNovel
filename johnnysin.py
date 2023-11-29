# ... [Previous code] ...
from classes import NPC

# Define the new character Johnny Sin
JOHNNYSIN = NPC("Johnny Sin")

# Add the day 1 scenario for Johnny Sin
day1_johnny = [
    ["(If you choose to go SUTD library to study)", pic, []],
    ["You're buried in books at the SUTD library, preparing for your final exams.", pic, []],
    ["Hey there, sorry to disturb you. I'm Johnny, an exchange student. I'm looking for some resources on Singapore's architecture. Could you help?", pic, [], "Johnny Sin", "sounds/dialogue.wav"],
    ["", pic, [{"text": "Sure, the architecture section is over there.", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": "neutral"}},
               {"text": "I'm really busy, maybe ask the librarian?", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": "decrease"}},
               {"text": "I'd love to help! Maybe we could watch a documentary on it sometime.", "nextSceneIndex": 2, "affection": {"affectedNPC": JOHNNYSIN, "change": "increase"}}]],
    ["Yes, and I'm fascinated by the blend of modern and traditional designs here. What about you? What are you studying so intently?", pic, [], "Johnny Sin"],
    ["I'm prepping for my final exams. It's a bit overwhelming.", pic, []],
    ["Maybe after your exams, you could show me around the city's architectural highlights?", pic, [], "Johnny Sin"],
    ["", pic, [{"text": "That sounds like a plan. It would be a nice break from studying.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "increase"}},
               {"text": "I might be able to. Let's see how my schedule looks after exams.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "neutral"}},
               {"text": "I'm not sure, I'll be pretty busy even after exams.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "decrease"}}]],
    ["That sounds like a plan. It would be a nice break from all this studying.", pic, []],
    # ... [Continue with more dialogue and options] ...
]

# Add the day 1 scenario to your main dialogue list
diag.extend(day1_johnny)
# ... [Previous code and Day 1 scenarios] ...

# Add the day 2 scenario for Johnny Sin
day2_johnny = [
    ["(If you go SUTD track for a sunset run)", pic, []],
    ["The university track in the late afternoon.", pic, []],
    ["Hey, I noticed you yesterday at the library. I'm going for a run. Care to join me? It's a great way to de-stress.", pic, [], "Johnny Sin", "sounds/dialogue.wav"],
    ["", pic, [{"text": "Sure, why not? Running at sunset sounds perfect.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "increase"}},
               {"text": "Maybe another day. I'm not up for a run right now.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "neutral"}},
               {"text": "Running isn't really my thing. Maybe another time?", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "decrease"}}]],
    ["Trust me, the view at sunset is worth it. Plus, I could use the company.", pic, [], "Johnny Sin"],
    ["(During the run) Look at that sunset! It's like the sky's putting on a show just for us.", pic, [], "Johnny Sin"],
    ["", pic, [{"text": "It's beautiful. I never took the time to appreciate it like this.", "nextSceneIndex": 4, "affection": {"affectedNPC": JOHNNYSIN, "change": "increase"}},
               {"text": "It is nice. But let's not stop; we should keep our pace.", "nextSceneIndex": 4, "affection": {"affectedNPC": JOHNNYSIN, "change": "neutral"}},
               {"text": "I'm too tired to enjoy it. Maybe we should head back?", "nextSceneIndex": 4, "affection": {"affectedNPC": JOHNNYSIN, "change": "decrease"}}]],
    ["Back home, moments like these are rare. I'm glad I got to share it with you.", pic, [], "Johnny Sin"],
   
]

# Add the day 3 scenario for Johnny Sin
day3_johnny = [
    ["Portrait Session in Art Class", pic, []],
    ["Art class, with an assignment to draw a portrait.", pic, []],
    ["I've been thinking about the assignment, and I would like to draw your portrait. Would that be okay with you?", pic, [], "Johnny Sin", "sounds/dialogue.wav"],
    ["", pic, [{"text": "Sure, that sounds like fun! I've always wanted to be someone's muse.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "increase"}},
               {"text": "I guess that's fine. But I'm not sure I'm model material.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "neutral"}},
               {"text": "I'm not really comfortable being your subject, sorry.", "nextSceneIndex": 3, "affection": {"affectedNPC": JOHNNYSIN, "change": "decrease"}}]],
    ["You have a certain...expression, it's captivating. Like the Mona Lisa.", pic, [], "Johnny Sin"],
    
]

# Add the scenarios
diag.extend(day2_johnny)
diag.extend(day3_johnny)


