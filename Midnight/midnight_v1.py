from random import randint

class midnight:

	def __init__(self):
		self.dieSet = {'die1' : 0, 'die2' : 0, 'die3' : 0, 'die4' : 0, 'die5' : 0, 'die6' : 0}
		self.playerScore = 0
		self.AIScore = 0
		self.input = 10
		self.gameEnd = False
		self.keptDie = []
		self.pickedBefore = []
		
	def userInput(self):
		try:
			self.input = int(input("Which die would you like to keep? Enter 1 - 6 (0 to roll again): "))
		except:
			print("That is not an acceptable value.")
			self.userInput()
	
	def InputValidation(self):
		if self.input in self.pickedBefore:
			print("That Die has been picked before")
			self.userInput()
		elif self.input > 6 or self.input < 0:
			print("C'mon it's 0 - 6")
			self.userInput()

	def rollDice(self):
		self.setDieSetKeys()
		for key in self.dieSet_keys:
			self.dieSet[key] = randint(1,6)

	def setDieSetKeys(self): 
		self.dieSet_keys = self.dieSet.keys()
			
	def keepDie(self):
		dieCheck = 0
		while self.input != 0:
			totalDie = len(self.keptDie)
			if totalDie == 6:
				self.input = 0
				print("All die have been kept. Calculating score.")
			else:
				self.userInput()
				self.InputValidation()
				if self.input in self.pickedBefore:
					print("Pick another Die")
					print("")
				if dieCheck == 0 and self.input == 0:
					self.input = 10
					print("You must pick at least one die.")
					print("")
				elif self.input == 1:
					self.keptDie.append(self.dieSet['die1'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die1']
				elif self.input == 2:
					self.keptDie.append(self.dieSet['die2'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die2']
				elif self.input == 3:
					self.keptDie.append(self.dieSet['die3'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die3']
				elif self.input == 4:
					self.keptDie.append(self.dieSet['die4'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die4']
				elif self.input == 5:
					self.keptDie.append(self.dieSet['die5'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die5']
				elif self.input == 6:
					self.keptDie.append(self.dieSet['die6'])
					self.pickedBefore.append(self.input)
					dieCheck = len(self.keptDie) - totalDie
					del self.dieSet['die6']
		self.input = 10
		print("")	
				
	def ruleBook(self):
		if len(self.keptDie) == 6: 
			self.gameEnd = True
		else: 
			self.gameEnd = False
	
	def pScore(self):
		if 1 not in self.keptDie or 4 not in self.keptDie:
			self.playerScore = -1
		else:
			i = 0
			while i <= 5:
				self.playerScore = self.playerScore + self.keptDie[i]
				i += 1
			self.playerScore = self.playerScore - 5
			
	def aScore(self):
		if 1 not in self.keptDie or 4 not in self.keptDie:
			self.AIScore = -1
		else:
			i = 0
			while i <= 5:
				self.AIScore = self.AIScore + self.keptDie[i]
				i += 1
			self.AIScore = self.AIScore - 5
		
	def AI(self):
		keyValues = []
		keeper = 0
		delKey = ' '
		lenCheck = 0
		self.dieSet = {'die1' : 0, 'die2' : 0, 'die3' : 0, 'die4' : 0, 'die5' : 0, 'die6' : 0}
		self.input = 10
		self.gameEnd = False
		self.keptDie = []
		while self.gameEnd == False:
			self.rollDice()
			self.printDie()
			keyValues = self.dieSet.keys()
			lenCheck = len(self.dieSet)
			for i in keyValues:
				if self.dieSet[i] == 6:
					self.keptDie.append(self.dieSet[i])
				elif self.dieSet[i] == 1 and 1 not in self.keptDie:
					self.keptDie.append(self.dieSet[i])
				elif self.dieSet[i] == 4 and 4 not in self.keptDie:
					self.keptDie.append(self.dieSet[i])
			else:
				self.ruleBook()
				if self.gameEnd == False and lenCheck == len(self.dieSet):
					keyValues = self.dieSet.keys()
					for i in keyValues:
						if self.dieSet[i] > keeper:
							keeper = self.dieSet[i]
							delKey = i
					del self.dieSet[delKey]
					self.keptDie.append(keeper)
					delKey = ' '
					keeper = 0
			self.printKept()
			self.ruleBook()
		self.aScore()
		
	def winner(self):
		if self.playerScore == -1 and self.AIScore == -1:
			print("Wash!")
			print("Player Bust!")
			print("AI Bust!")
			print(" ")
		elif self.playerScore == -1 and self.AIScore != -1:
			print("AI Wins!")
			print("Player Bust!")
			print("AI Score: " + str(self.AIScore))
			print(" ")
		elif self.playerScore != -1 and self.AIScore == -1:
			print("Player Wins!")
			print("Player Score: " + str(self.playerScore))
			print("AI Bust!")
			print(" ")
		elif self.playerScore != -1 and self.AIScore != -1 and self.playerScore > self.AIScore:
			print("Player Wins!")
			print("Player Score: " + str(self.playerScore))
			print("AI Score: " + str(self.AIScore))
			print(" ")
		elif self.playerScore != -1 and self.AIScore != -1 and self.playerScore < self.AIScore:
			print("AI Wins!")
			print("Player Score: " + str(self.playerScore))
			print("AI Score: " + str(self.AIScore))
			print(" ")
		elif self.playerScore == self.AIScore:
			print("Tie!")
			print("Player Score: " + str(self.playerScore))
			print("AI Score: " + str(self.AIScore))
			print(" ")
		
	def printDie(self):
		print("-"*77)
		print("-" + " "*33 + "Roll Cup" + " "*34 + "-")
		print("-"*77)
		print("")
		print(self.dieSet)
		print("")
		print("-"*77)
		print("")
		
	def printKept(self):
		print("-"*77)
		print("-" + " "*33 + "Kept Die" + " "*34 + "-")
		print("-"*77)
		print("")
		print(self.keptDie)
		print("")
		print("-"*77)
		print("")
		
	def welcome (self):
		print("-"*77)
		print("-" + " "*33 + "Midnight" + " "*34 + "-")
		print("-" + " "*75 + "-")
		print("-" + " "*5 + " The object of the game is to get a 1 and a 4 and 24. That's it. " + " "*5 + "-")
		print("-" + " "*75 + "-")
		print("-"*77)
		print("")


if __name__ == '__main__':
	m1 = midnight()
	m1.welcome()
	while m1.gameEnd == False:
		m1.rollDice()
		m1.printDie()
		m1.keepDie()
		m1.printKept()
		m1.ruleBook()
	m1.pScore()
	m1.AI()
	m1.winner()
	
