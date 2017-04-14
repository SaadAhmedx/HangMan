import os
import random

def clear():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def runGain():
	userInput = input("Want To Run Again ? Y/n: ").lower()
	if userInput == 'y':
		clear()
		letterGame()
		runGain()
	else:
		clear()
		exit("Good Bye\n")

def letterGame():
	wordList = ["hacking", "bounty", "security", "hunting", "descriptor", "vulnerability"]
	
	while True:

		secWord = random.choice(wordList)
		goodGuess = []
		badGuess = []

		while len(goodGuess) != len(secWord):
			attempt = " ".join(badGuess)

			for secLetter in secWord:
				if secLetter in goodGuess :
					print(secLetter, end="")
				else:
					print("_", end="")

				clear()	 			

			print("\n\n=> {}\n\nStrikes {}/5\n".format(attempt, len(badGuess)))		
			userGuess = input("\nEnter Letter To Guess: ").lower()

			if len(userGuess) != 1 :
				continue

			elif userGuess in badGuess or userGuess in goodGuess :
				continue

			elif not userGuess.isalpha() :
				continue
			
			if userGuess in list(secWord):

				x = -1
				for sec in list(secWord):
					if userGuess in sec:
						z = int(secWord.index(userGuess, x+1))
						goodGuess.insert(z, userGuess)
						x = z

			else:
				badGuess.append(userGuess)
				if len(badGuess) > 5:

					print("\nYou Loss The Sec Word Was {} \n".format(secWord))
					runGain()

		else:
			print("\nYou Win The Secert Word Was {} \n".format(secWord))
			runGain()	


letterGame()	


