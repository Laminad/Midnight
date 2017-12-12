from random import randint

import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen



class MidnightGameScreenStart(Screen):
    pass



class MidnightGameScreenRoll(Screen):

    die_set = {'Die 1' : 0, 'Die 2' : 0, 'Die 3' : 0, 'Die 4' : 0, 'Die 5' : 0, 'Die 6' : 0}
    die_set_keys = []

    def setDieSetKeys(self): 
        self.die_set_keys = self.die_set.keys()

    def rollDice(self):
        self.setDieSetKeys()
        for key in self.die_set_keys:
            self.die_set[key] = randint(1,6)
        print(self.die_set)    



class MidnightGameScreenRollResults(Screen):  
    pass



class MidnightGameScreenKeptDie(Screen):
    pass



class MidnightEngine(Widget):

    def __init__(self):
        self.die_set = {'Die 1' : 0, 'Die 2' : 0, 'Die 3' : 0, 'Die 4' : 0, 'Die 5' : 0, 'Die 6' : 0}
        self.kept_die = {}
        self.die_set_keys = []
        self.kept_die_keys = []
        self.kept_die_count = 0
        self.die_set_count = 0
        self.total_die = 6
        self.game_end = False
        self.score = 0
        self.game_result = ""
        self.
        

    def setDieSetKeys(self): 
        self.die_set_keys = self.die_set.keys()


    def setKeptDieKeys(self):
        self.kept_die_keys = self.kept_die.keys()


    def setKeptDieCount(self):
        self.kept_die_count = len(self.kept_die)


    def setDieSetCount(self):
        self.die_set_count = len(self.die_set)


    # def putDieinKeptDie(self):
        # This will use the user input to pull out the correct keys from the dictionary and put them in the Kept Die dictionary.
        # Not sure of the user input requirements so can not complete at this time.
  

    def rollDice(self, *args):
        self.setDieSetKeys()
        for key in self.die_set_keys:
            self.die_set[key] = randint(1,6)


    def rulebook(self):
        if self.kept_die_count == self.total_die: 
            self.game_end = True
        else: 
            self.game_end = False

    
    def AI(self):
        while self.game_end == False:
            die = self.die_set[0]
            if self.die_set[die] == 6:
                self.kept_die[die] = self.die_set[die]
                del self.die_set[die]
            elif (self.die_set[die] == 4) and (4 not in self.kept_die):
                self.kept_die[die] = self.die_set[die]
                del self.die_set[die]
            elif (self.die_set[die] == 1) and (1 not in self.kept_die):
                self.kept_die[die] = self.die_set[die]
                del self.die_set[die]
            else:
                break
            self.rulebook()
        else:
            self.rulebook()
            if self.game_end == False:
                max_value = max(self.die_set.values())
                key = {k:v for k, v in self.die_set.items() if v == max_value}
                self.kept_die[key] = max_value
                del self.die_set[key]


    def scoreCounter(self, game_object):
        for die in self.kept_die:
            self.score += self.kept_die[die]
        self.score -= 5  
        # This is to account for the 1 and 4, as those don't count towards your score.
        return self.score

    



class MidnightPlayerandAIScores(MidnightEngine):
    
    player_score = 0
    ai_score = 0
    player_result = ""
    ai_results = ""
    bust_check_result = ""
    player_game = MidnightEngine()
    ai_game = MidnightEngine()


    def setPlayerScore(self): 
        self.player_score = MidnightEngine.scoreCounter(player_game)


    def setAIScore(self): 
        self.ai_score = MidnightEngine.scoreCounter(ai_game)


    def setPlayerResult(self):
        self.player_result = self.bustCheck()
        self.bust_check_result = ""


    def setAIResult(self):
        self.ai_result = self.bustCheck()
        self.bust_check_result = ""


    def gameResultCheck(self):
        if self.player_score == "Bust!" and  self.ai_result == "Bust!":
            self.game_result = "Wash!"
        elif (self.player_score == self.ai_score) and ((self.player_score != 0) or (self.ai_score !=0)):
            self.game_result = "Tie!"
        elif self.player_score > self.ai_score:
            self.game_result = "Player Wins!"
        elif self.player_score < self.ai_score:
            self.game_result = "AI Wins!"






class MidnightApp(App):


    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MidnightGameScreenStart(name="screen_start"))
        screen_manager.add_widget(MidnightGameScreenRoll(name="screen_roll"))
        screen_manager.add_widget(MidnightGameScreenRollResults(name="screen_roll_results"))
        screen_manager.add_widget(MidnightGameScreenKeptDie(name="screen_kept_die"))
        return screen_manager


if __name__ == '__main__':
    MidnightApp().run()