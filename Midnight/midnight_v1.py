from random import randint
from time import sleep

class midnight:

	def __init__(self):
		self.one = "\n#######\n#     #\n#  *  #\n#     #\n#######\n"
		self.two = "\n#######\n#   * #\n#     #\n# *   #\n#######\n"
		self.three = "\n#######\n#   * #\n#  *  #\n# *   #\n#######\n"
		self.four = "\n#######\n# * * #\n#     #\n# * * #\n#######\n"
		self.five = "\n#######\n# * * #\n#  *  #\n# * * #\n#######\n"
		self.six = "\n#######\n# * * #\n# * * #\n# * * #\n#######\n"
		self.dieSet = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
		self.playerScore = 0
		self.AIScore = 0
		self.input = 10
		self.gameEnd = False
		self.keptDie = []
		self.pickedBefore = []
		self.dieCheck = 0
		self.dieKeptThisTurn = 0

	def rollDice(self):
		self.setDieSetKeys()
		for key in self.dieSet_keys:
			self.dieSet[key] = randint(1,6)

	def setDieSetKeys(self): 
		self.dieSet_keys = self.dieSet.keys()
			
	def keepDie(self):
		while self.input != 0:
			if self.dieCheck == 6:
				print("\nAll die have been kept. Calculating score.\n")
				break
			self.userInput()
			if self.input != 0:
				self.keptDie.append(self.dieSet[self.input])
				self.pickedBefore.append(self.input)
				self.dieCheck += 1
				self.dieKeptThisTurn +=1
				del self.dieSet[self.input]
		self.dieKeptThisTurn  = 0
		self.input = 10
		
	def userInput(self):
		try:
			self.input = int(input("Which die would you like to keep? Enter 1 - 6 (0 to roll again): "))
			self.InputValidation()
		except:
			print("\nThat is not an acceptable value.\n")
			self.userInput()
	
	def InputValidation(self):	
		if self.input in self.pickedBefore:
			print("\nThat Die has been picked before\n")
			self.userInput()
		elif self.input > 6 or self.input < 0:
			print("\nC'mon it's 0 - 6\n")
			self.userInput()
		elif self.input == 0 and self.dieKeptThisTurn == 0:
			print("\nYou need to pick at least one.\n")
			self.userInput()
		
	def AI(self):
		keyValues = []
		keeper = 0
		delKey = ' '
		lenCheck = 0
		trashCollector = []
		self.dieSet = {1 : 0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0}
		self.input = 10
		self.gameEnd = False
		self.keptDie = []
		print("-" + " "*33 + "AI's Turn!"+ " "*32 + "-\n")
		while self.gameEnd == False:
			self.rollDice()
			self.printDie()
			print("-"*77+"\n")
			keyValues = self.dieSet.keys()
			lenCheck = len(self.dieSet)
			for i in keyValues:
				if self.dieSet[i] == 6:
					self.keptDie.append(self.dieSet[i])
					trashCollector.append(i)
				elif self.dieSet[i] == 1 and 1 not in self.keptDie:
					self.keptDie.append(self.dieSet[i])
					trashCollector.append(i)
				elif self.dieSet[i] == 4 and 4 not in self.keptDie:
					self.keptDie.append(self.dieSet[i])
					trashCollector.append(i)
			else:
				for i in trashCollector:
					del self.dieSet[i]
				trashCollector = []
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
			sleep(4)
			self.printKept()
			self.ruleBook()
		self.aScore()

	def ruleBook(self):
		if len(self.keptDie) == 6: 
			self.gameEnd = True
		else:
			self.gameEnd = False
		
	def winner(self):
		if self.playerScore == -1 and self.AIScore == -1:
			print("Wash!\nPlayer Bust!\nAI Bust!\n")
		elif self.playerScore == -1 and self.AIScore != -1:
			print("AI Wins!\nPlayer Bust!\nAI Score: " + str(self.AIScore)+"\n")
		elif self.playerScore != -1 and self.AIScore == -1:
			print("Player Wins!\nPlayer Score: " + str(self.playerScore)+"\nAI Bust!\n")
		elif self.playerScore != -1 and self.AIScore != -1 and self.playerScore > self.AIScore:
			print("Player Wins!\nPlayer Score: " + str(self.playerScore)+"\nAI Score: " + str(self.AIScore)+"\n")
		elif self.playerScore != -1 and self.AIScore != -1 and self.playerScore < self.AIScore:
			print("AI Wins!\nPlayer Score: " + str(self.playerScore)+"\nAI Score: " + str(self.AIScore)+"\n")
		elif self.playerScore == self.AIScore:
			print("Tie!\nPlayer Score: " + str(self.playerScore)+"\nAI Score: " + str(self.AIScore)+"\n")

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
		
	def printDie(self):
		print("-"*77)
		print("-" + " "*33 + "Roll Cup" + " "*34 + "-")
		print("-"*77+"\n")
		self.setDieSetKeys()
		for key in self.dieSet_keys:
			if key == 1:
				print("\nDie 1")
				self.AsciiPrint(self.dieSet[key])
			elif key == 2:
				print("\nDie 2")
				self.AsciiPrint(self.dieSet[key])
			elif key == 3:
				print("\nDie 3")
				self.AsciiPrint(self.dieSet[key])
			elif key == 4:
				print("\nDie 4")
				self.AsciiPrint(self.dieSet[key])
			elif key == 5:
				print("\nDie 5")
				self.AsciiPrint(self.dieSet[key])
			elif key == 6:
				print("\nDie 6")
				self.AsciiPrint(self.dieSet[key])
		print("")
		print("-"*77+"\n")
		
	def printKept(self):
		print("-"*77)
		print("-" + " "*33 + "Kept Die" + " "*34 + "-")
		print("-"*77+"\n")
		for i in self.keptDie:
			self.AsciiPrint(i)
		print("")
		print("-"*77+"\n")
		print("-"*77+"\n")

	def AsciiPrint(self, value):
		if value == 1:
			print(self.one)
		elif value == 2:
			print(self.two)
		elif value == 3:
			print(self.three)
		elif value == 4:
			print(self.four)
		elif value == 5:
			print(self.five)
		elif value == 6:
			print(self.six)

	def welcome (self):
		print("-"*77)
		print("-" + " "*33 + "Midnight" + " "*34 + "-")
		print("-" + " "*75 + "-")
		print("-" + " "*5 + " The object of the game is to get a 1 and a 4 and 24. That's it. " + " "*5 + "-")
		print("-" + " "*75 + "-")
		print("-"*77+"\n")
		print("-" + " "*30 + "Players's Turn!"+ " "*30 + "-\n")


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