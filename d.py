# import nltk
# from nltk.tokenize import word_tokenize

# # Sample sentence
# sentence = "play music"
# print(sentence.split())

# # Tokenize the sentence into words
# words = word_tokenize(sentence)

# # Perform part-of-speech tagging
# pos_tags = nltk.pos_tag(words)

# # Print the tagged words
# print(pos_tags)
# from prompt_toolkit import prompt

# def suggest_message(topic):
#     # Logic to suggest email body message based on the topic
#     suggested_message = f"Hello,\n\nI hope this email finds you well. I wanted to reach out to discuss the topic of {topic}. It's an important subject that I believe requires our attention.\n\nPlease let me know your thoughts on this matter and if you have any further insights to share.\n\nLooking forward to hearing from you.\n\nBest regards,\n[Your Name]"

#     return suggested_message

# # Get the suggested email message based on the topic
# topic = "topic"
# suggested_email_message = suggest_message(topic)

# # Prompt the user to edit the email message
# email_message = prompt('Enter the Email message or press Enter to use the suggested message:\n', default=suggested_email_message)

# # Now you can edit the email_message variable as needed
# print("Entered Email Message:\n", email_message)

# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk import pos_tag
# from nltk import ne_chunk, Tree
# words = word_tokenize("press a and ctrl")
        
# # Get the English stopwords from NLTK
# stop_words = set(stopwords.words('english'))

# # Filter out the stop words
# filtered_words = [word for word in words if word.lower() not in stop_words]

# # Join the remaining words back into a single string
# filtered_text = ' '.join(filtered_words)


# print(filtered_text)


