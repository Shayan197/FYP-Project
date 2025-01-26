import re
import random

class RuleBot:
    negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
    exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")

    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "What do you consume for sustenance?",
        "Is there intelligent life on this planet?",
        "Does Earth have a leader?",
        "What planets have you visited?",
        "What technology do you have on this planet?"
    )
    
    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\byour planet\b.*',
            'answer_why_intent': r'why\s+are.*',
            'about_intellipat': r'.*\bintellipaat\b.*'
        }

    def greet(self):
        """Greets the user and starts the chat."""
        self.name = input("What is your name?\n")
        will_help = input(f"Hi {self.name}, I am Rule-Bot. Will you help me learn about your planet?\n").lower()
        if will_help in self.negative_responses:
            print("Okay, have a nice Earth day!")
            return
        self.chat()

    def make_exit(self, reply):
        """Checks if the user wants to exit the chat."""
        if reply in self.exit_commands:
            print("Okay, have a nice Earth day!")
            return True
        return False

    def chat(self):
        """Main chat loop."""
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        """Matches user input to an intent."""
        for intent, regex_pattern in self.alienbabble.items():
            if re.match(regex_pattern, reply):
                if intent == 'describe_planet_intent':
                    return self.describe_planet_intent()
                elif intent == 'answer_why_intent':
                    return self.answer_why_intent()
                elif intent == 'about_intellipat':
                    return self.about_intellipat()
        return self.no_match_intent()

    def describe_planet_intent(self):
        """Response for describing the planet."""
        responses = [
            "My planet is a utopia of diverse organisms and species.",
            "I am from Opidipus, the capital of the Wayward Galaxies."
        ]
        return random.choice(responses)

    def answer_why_intent(self):
        """Response for 'why are you here?'."""
        responses = [
            "I come in peace.",
            "I am here to collect data on your planet and its inhabitants.",
            "I heard the coffee is good!"
        ]
        return random.choice(responses)

    def about_intellipat(self):
        """Response about Intellipaat."""
        responses = [
            "Intellipaat is a world-class professional training company.",
            "Intellipaat helps you learn concepts in an effective way.",
            "At Intellipaat, your career and skills grow together."
        ]
        return random.choice(responses)

    def no_match_intent(self):
        """Fallback response for unmatched inputs."""
        responses = [
            "Please tell me more.",
            "Why do you say that?",
            "I see. Can you elaborate?",
            "Interesting, can you tell me more?",
            "How do you think about that?",
            "Why?"
        ]
        return random.choice(responses)

AlienBot = RuleBot()
AlienBot.greet()

# import re
# import random

# class RuleBot:
#     negative_responses = ("no","nope","nah","naw","not a chance","sorry")
#     exit_commands = ("quit","pause","exit","goodbye","bye","later")
#     random_questions = (
#         "Why are you here?",
#         "Are there many humans like you?",
#         "What dou you consume for sustenanes?",
#         "Is there intelligent life on this plannet?",
#         "Does Earth have a leader?",
#         "What planets have you visited?",
#         "What technology do you have on this planet?"
#     )
#     def __init__(self):
#         self.alienbabble = {'describe_planet_intent': r'.*\s*your planet.*',
#                             'answer_why_intent': r'why\sare.*',
#                             'about_intellipat': r'.*\s*intellipaat'
#                             }
        
#     def greet(self):
#         self.name = input("What is your name?\n")
#         will_help = input(f"Hi {self.name}, i am Rule-Bot. Will you help me about your planet?\n")
#         if will_help in self.negative_responses:
#             print("Okay, have a nice earth day!")
#             return
#         self.chat()

#     def make_exit(self, reply):
#         for command in self.exit_commands:
#             if reply == command:
#                 print("Okay, have a nice Earth day!")
#                 return True
            
#     def chat(self):
#         reply = input(random.choice(self.random_questions)).lower()
#         while not self.make_exit(reply):
#             reply = input(self.match_reply(reply))

#     def match_reply(self,reply):
#         for key,value in self.alienbabble.items():
#             intent = key
#             regex_pattern = value
#             found_match = re.match(regex_pattern,reply)
#             if found_match and intent == 'describe_planet_intent':
#                 return self.describe_planet_intent()            
#             elif found_match and intent == 'answer_why_intent':
#                 return self.answer_why_intent()            
#             if found_match and intent == 'about_intellipat':
#                 return self.about_intellipat()
#         if not found_match:
#             return self.no_match_intent()

#     def describe_planet_intent(self):
#         responses = ("My planet is a utopia of diverse organism and species\n",
#                     "I am from Opidipus, the capital of the Wayward Galaxies")
#         return random.choice(responses)
    
#     def answer_why_intent(self):
#         responses = ("I come in peace\n","i am here to collect data on your planet and its inhabitants\n",
#                     "I heared the coffee is good\n")
#         return random.choice(responses)
    
#     def about_intellipat(self):
#         responses = ("Intekkipaat is World's large professional Company\n","Intellipaat will make you learn concepts in the way \n",
#                     "Intellipaat is where your carrier and your skills grows\n")
#         return random.choice(responses)
    
#     def no_match_intent(self):
#         responses = ("Please tell me more.\n","Tell me more!\n","Why do you say that?\n","I see. Can you Coaborate?\n",
#                     "Intresting, Can you tell me more?\n","I see. How do you Think?\n","Why?\n",
#                     "How do you think I feel how you say That?\n")
#         return random.choice(responses)


# AlienBot = RuleBot()
# AlienBot.greet()