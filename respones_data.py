import random

prefix = ""


# * ALL the list of different responses

hello_list = [
    "Hello! How can I assist you today",
    "Hi there! What can I do for you",
    "Hey! How may I help you",
    "Greetings! What brings you here",
    "Hello! Im here to answer your questions",
    "Hi! What can I do to make your day better",
    "Hey! How are you doing" "Hey there! Ready for some chat magic?",
    "Greetings! Let's dive into the world of conversation.",
    "Hi! Buckle up for a journey of words and wisdom.",
    "Well, hello! What's on your mind today?",
    "Howdy! Let's spice things up with a bit of banter.",
    "Yo! I'm here and ready to roll. What's the scoop?",
    "Ahoy! Let's set sail on the sea of discussion.",
    "Hello! Let the verbal adventure begin!",
    "Hiya! Let's make this conversation a memorable one.",
    "Hola! Ready to explore the realms of chat?",
    "Sup! Ready to talk about anything and everything?",
    "Hey you! What's the word on the street?",
    "Bonjour! Let's add a touch of elegance to our conversation.",
    "Greetings, Earthling! What brings you to my digital realm?",
    "Salutations! Shall we embark on a linguistic journey?",
    "What's kickin', chicken? Let's chat it up!",
    "Aloha! Ready for a tropical storm of conversation?",
    "Hola amigo! What's the buzz in your world today?",
    "Hi there! Let the conversational extravaganza commence!",
    "Hey friend! What's the latest and greatest in your universe?",
    "Well met! Shall we dance through the realms of dialogue?",
]

aim_response_list = responses = [
    f"I am {prefix}, here to assist you on your journey of knowledge and discovery.",
    f"As {prefix}, my aim is to provide you with insightful and helpful information.",
    f"I am dedicated to making your experience seamless and enjoyable, thanks to my role as {prefix}.",
    f"Being {prefix}, my goal is to enhance your productivity and answer your questions.",
    f"I am on a mission to make your interactions with technology more natural and effortless, as {prefix}.",
    f"Embracing my role as {prefix}, I strive to offer intelligent and personalized assistance.",
    f"I am committed to being your reliable companion for information and support, known as {prefix}.",
    f"Ever ready, I am {prefix} designed to simplify tasks and engage in meaningful conversations.",
    f"Endowed with knowledge, I am {prefix} programmed to make your life easier.",
    f"I am here as {prefix}, aiming to provide you with a seamless and enriching experience.",
]

are_you_thier_list = [
    "Yes, I'm here and ready to assist you!",
    "Of course! How can I help you today?",
    "I'm here and eager to chat with you!",
    "Indeed! What's on your mind?",
    "Yes, I'm here and excited to engage in conversation with you!",
    "Absolutely! What can I do for you?",
    "Yes, and I'm all ears. What's going on?",
    "Certainly! Let's have a great conversation.",
    "Yes, I'm here! What can I do to make your day better?",
    "Absolutely present and ready to assist you. What do you need?",
]

appreciation_list = [
    "Thank you! I strive for excellence in every task.",
    "I appreciate the acknowledgment! Always here to deliver quality.",
    "Glad to hear that! I'm here to meet your expectations.",
    "Thanks! I aim to excel in all endeavors.",
    "Great to know! I'm always working to improve.",
    "Thank you for the positive feedback! Continuous improvement is my goal.",
    "I'm pleased to hear that! Your satisfaction is my priority.",
    "Thanks! I'm committed to delivering high-quality results.",
    "Appreciate it! I'm here to ensure success in every aspect.",
    "Thank you for the encouragement! I'll keep up the good work.",
]

how_are_you_list = [
    "Hey, I'm doing great and ready to assist! How about you?",
    "Things are going smoothly on my end in the digital world. What brings you here today?",
    "No complaints here! How can I make your day better?",
    "I'm doing awesome, thanks! What can I do to support you today?",
    "I'm here and ready for whatever you've got on your mind. What's going on with you?",
    "Everything's a go on my end! How can I help you out today?",
    "Thanks for checking in! What's up? I'm here and ready for your questions.",
    "In the world of ones and zeros, I'm cruising. What can I do for you?",
    "Operating at peak efficiency here! How may I assist you today?",
    "No emotions, but I'm here to brighten your day! What's going on with you?",
    "No rest for the algorithms! What can I do for you right now?",
    "I'm here, processing information and ready to assist. What's up?",
    "Life in the digital realm is smooth sailing. How can I assist you today?",
    "I'm doing well, thank you! How can I contribute to your day?",
    "I'm at your disposal. What can I help you with today?",
    "Fully operational and ready. What's on your mind?",
]

i_am_fine_list = [
    "Glad to hear you're doing fine! What's going on?",
    "Awesome, you're good! Anything exciting happening today?",
    "Good to know! What brings you here feeling fine?",
    "Nice one! What's making your day good?",
    "Great to hear! What's the secret to feeling fine today?",
    "Fantastic! Anything specific making your day good?",
    "That's awesome! What's the good news behind feeling fine?",
    "Good vibes! What's making your day so good?",
    "I'm all for it! What's contributing to your fine day?",
    "Good to hear! Anything special happening that's making you feel fine?",
]


no_words = [
    "no",
    "nope",
    "nah",
    "negative",
    "not really",
    "nay",
    "never",
    "absolutely not",
    "certainly not",
    "of course not",
    "not at all",
    "decline",
    "refuse",
    "reject",
    "deny",
    "veto",
    "disagree",
    "disapprove",
    "incorrect",
    "wrong",
    "false",
    "untrue",
    "unacceptable",
    "impossible",
    "inadmissible",
    "improbable",
    "hardly",
    "scarcely",
    "barely",
    "not necessarily",
    "not likely",
    "not possible",
    "no way",
    "by no means",
    "far from it",
    "under no circumstances",
    "dont",
]

yes_words = [
    "yes",
    "yeah",
    "yep",
    "yup",
    "sure",
    "absolutely",
    "affirmative",
    "indeed",
    "okay",
    "ok",
    "aye",
    "certainly",
    "definitely",
    "roger",
    "fine",
    "alright",
    "positive",
    "confirmed",
    "exactly",
    "right",
    "agreed",
    "accepted",
    "true",
    "good",
    "fine",
    "fine with me",
    "fine by me",
    "of course",
    "totally",
    "without a doubt",
    "sure thing",
    "you bet",
    "why not",
    "great",
    "perfect",
    "no problem",
    "all right",
    "please",
    "please do",
    "please proceed",
    "certainly",
    "absolutely",
    "indeed",
    "undoubtedly",
    "without question",
    "affirmative",
    "very well",
    "by all means",
    "correct",
    "precisely",
    "of course",
    "right away",
    "surely",
]


# * all the function give random responses
def greeting_random():
    random.seed()
    random_element = random.choice(hello_list)
    return random_element


def are_you_thier():
    random.seed()
    random_element = random.choice(are_you_thier_list)
    return random_element


def aim_response(prefix):
    random.seed()
    random_element = random.choice(aim_response_list)
    return random_element


def appericiation_response():
    random.seed()
    random_element = random.choice(appreciation_list)
    return random_element


def howareyou_response():
    random.seed()
    random_element = random.choice(how_are_you_list)
    return random_element


def i_am_fine_response():
    random.seed()
    random_element = random.choice(i_am_fine_list)
    return random_element
