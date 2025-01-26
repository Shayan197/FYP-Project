import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load and preprocess data
f = open('data.txt', 'r', errors='ignore')
raw_doc = f.read()
f.close()

raw_doc = raw_doc.lower()
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

sentence_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()

# Helper functions
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

# Greetings
greet_inputs = ('hello', 'hi', 'whatsup', 'how are you?')
greet_responses = ('hi', 'Hey', 'Hey There!', 'There there!!')

def greet(sentences):
    for word in sentences.split():
        if word.lower() in greet_inputs:
            return random.choice(greet_responses)

# Response generation
def response(user_response):
    robo1_response = ''
    sentence_tokens.append(user_response)  # Add user response temporarily
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sentence_tokens)  # Transform all sentences
    vals = cosine_similarity(tfidf[-1], tfidf)  # Compare last sentence with others
    idx = vals.argsort()[0][-2]  # Find the most similar sentence index
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]  # Get second highest similarity score
    if req_tfidf == 0:
        robo1_response = "I am sorry, I am unable to understand you!"
    else:
        robo1_response = sentence_tokens[idx]
    sentence_tokens.pop()  # Remove user response after processing
    return robo1_response

# Chat loop
flag = True
print('Hello! I am the Learning Bot. Type your text after greeting to talk to me. Type "bye" to end the conversation.')

while flag:
    user_response = input().lower()
    if user_response != 'bye':
        if user_response in ('thankyou', 'thanks'):
            flag = False
            print('Bot: You are Welcome!')
        else:
            if greet(user_response) is not None:
                print(f'Bot: {greet(user_response)}')
            else:
                print('Bot: ', end='')
                print(response(user_response))
    else:
        flag = False
        print('Bot: Goodbye!')


# import numpy as np
# import nltk
# import string
# import random
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# f = open('data.txt','r',errors='ignore')
# raw_doc = f.read()

# raw_doc = raw_doc.lower()
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# sentance_tokens = nltk.sent_tokenize(raw_doc)
# word_tokens = nltk.word_tokenize(raw_doc)
# lemmer = nltk.stem.WordNetLemmatizer()

# def LemTokens(tokens):
#     return [lemmer.lemmatize(token) for token in tokens]
# remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

# def LemNormalize(text):
#     return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punc_dict)))

# greet_inputs = ('hello', 'hi', 'whatsup', 'how are you?')
# greet_responses = ('hi', 'Hey', 'Hey There!', 'There there!!')

# def greet(sentenses):
#     for word in sentenses.split():
#         if word.lower() in greet_inputs:
#             return random.choice(greet_responses)

# def response(user_response):
#     robo1_response = ''
#     TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
#     tfidf = TfidfVec.fit_transform(sentance_tokens)
#     vals = cosine_similarity(tfidf[-1], tfidf)
#     idx = vals.argsort()[0][-2]
#     flat = vals.flatten()
#     flat.sort()
#     req_tfidf = flat[-2]
#     if(req_tfidf == 0):
#         robo1_response = robo1_response + "I am sorry unable to understand you!"
#         return robo1_response
#     else:
#         robo1_response = robo1_response + sentance_tokens[idx]
#         return robo1_response
    
# flag = True
# print('Hello I am the learning Bot. Start type your text after greeting to talk to me. For Ending Conversation type bye!')
# while(flag == True):
#     user_response = input()
#     user_response = user_response.lower()
#     if(user_response != 'bye'):
#         if(user_response == 'thankyou' or user_response == 'thanks'):
#             flag = False
#             print('Bot : You are Welcome..')
#         else:
#             if(greet(user_response) != None):
#                 print('Bot : ' + greet(user_response))
#             else:
#                 sentance_tokens.append(user_response)
#                 word_tokens = word_tokens + nltk.word_tokenize(user_response)
#                 final_words = list(set(word_tokens))
#                 print('Bot : ', end = '')
#                 print(response(user_response))
#                 sentance_tokens.remove(user_response)
#     else:
#         flag = False
#         print('Bot : Goodbye!')