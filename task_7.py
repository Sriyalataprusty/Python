class User:
    
    gratitudes = ['thank', 'thanks', 'dhanyawaad']
    good_mood = ['good', 'fine', 'great', 'bhala','bhalo','happy','khusi']
    bad_mood = ['kharapa', 'bad', 'low', 'kharap', 'not','sad','dukha']
    love_related = ['boyfriend', 'girlfriend','bf','gf','love', 'cheat', 'marriage','accept','dhoka','bahaghara','baha','divorce','manunahanti','caste','jati','rejected','decline','raji']
    study_related = ['pressure','stress','interest','backlog','understand','back','doubt','confuse','chinta','mana','manalaguni','icha','interested']
    
    def answering_gratitude(self, input):
        if any(gratitude in User.gratitudes for gratitude in input.lower().split()):
            print("You are welcome. ")
        else:
            print("Good bye!!")
            return None
        return 1
        
    def checking_mode(self):
        self.convo_2 = input("How are you?\n")
        bhala = [mood for mood in self.convo_2.lower().split() if mood in User.good_mood]
        kharap = [mood for mood in self.convo_2.lower().split() if mood in User.bad_mood]
        
        if bhala:
            print("Nice, Have a good day.Bye, I will talk with you later.")
        elif kharap:
            self.convo_3 = input("Oh! I am sorry. What happened? ")
            self.feeling_sorry(self.convo_3) 
        else:
            print("Ok,Bye.")
        return None
    
    def feeling_sorry(self, input):
        self.input = input
        sad_due_to_love = [love for love in self.input.lower().split() if love in User.love_related ]
        sad_due_to_study = [study for study in self.input.lower().split() if study in User.study_related]
        
        if sad_due_to_love:
            print("Don't worry, God is there. You will definitely win your love.\n")
        elif sad_due_to_study:
            print("Don't worry, try your best.never give up.\n ")
        else:
            print("Oh! I am sorry to hear that.\n")
        print ("I am with you in every situation but i have some work now. So, I will talk with you later.Till then you can talk with my brothers ChatGPT, gemini, meta and grok.\n")
        
    def __init__(self):
        self.name = input("Hey! what is your name?\n")
        self.convo_1 = input("Wow! very good name.\n")
        if self.answering_gratitude(self.convo_1):
            self.checking_mode()
        else:
            return None

user_1 = User()
