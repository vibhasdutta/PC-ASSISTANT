
# *===============  Keyword Dictionarys
#! PLEASE ADD KEYWORD IN SMALL CASE
exit_list = ["exit", "bye", "good bye"]
web_command_list = ["open web browser", "open chrome", "open browser"]
sleep_word_list = ["wait"]
wakeup_word_list = ["wake", "wake up", "are you there"]

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

def remove_word_before(input_string,word):
    words = input_string.split()
    try:
        index = words.index(word)
        words = words[index+1:]  # Start from the word after the specified word
    except ValueError:
        pass  # Word not found, or it's the first word
    return ' '.join(words)
