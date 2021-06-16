def createGuessingWord():
	return input("Player 1 - Enter a word for Player 2 to guess: ").upper()

def displayGuessingWord(word, cSet, lSet):
	for i in word:
		if i in cSet:
			print(i, end="")
		elif i != " ":
			print("_", end="")
		else:
			print(" ", end="")
	print()

	print("Guessed Letters: ", end="")
	for i in lSet:
		print(i, end="")
	print()

def hasLetterBeenUsed(cSet, lSet, letter):
	
	isLetterUsed = False

	if letter in cSet:
		isLetterUsed = True 
	elif letter in lSet:
		isLetterUsed = True 

	return isLetterUsed

def checkGuessingLetter(wordToGuess, letter):
	letterFound = False
	for i in wordToGuess:
		if letter == i:
			letterFound = True
			break
	return letterFound 

def hasPlayerWon(wordToGuess, cSet):
	
	wonGame = True
	for i in wordToGuess:
		if not i in cSet:
			wonGame = False
			break

	return wonGame

def hasPlayerLost(noOfErrors):

	if noOfErrors > 7:
		displayHangman(noOfErrors)

	return noOfErrors > 7

def displayWinner(wordToGuess):
	print("Player 2 has guessed the word " + wordToGuess + " and won the game!")

def displayLoser():
	print("Player 2 has ran out of guesses and lost the game.")

def displayHangman(noOfErrors):

	if noOfErrors > 0:
		print("__")
		print(" |")
	if noOfErrors > 7:
		print(" 0 -DEAD!")
	if noOfErrors > 1:	
		print(" O ")
	if noOfErrors > 4:
		print("-|-")
	elif noOfErrors > 3:
		print("-|")
	elif noOfErrors > 2:
		print(" |")
	if noOfErrors > 6:
		print("/ \\")
	elif noOfErrors > 5:
		print("/")

def gameLoop():
	
	wordToGuess = createGuessingWord()
	print(chr(27) + "[2J") #Clears Screen
	letterSet = {" "} #Stores guessed letters
	correctSet = {" "}#Stores Correct Letrers
	noOfErrors = 0
	isWon = False
	isLoss = False

	while(isWon == False and isLoss == False):
		displayGuessingWord(wordToGuess, correctSet, letterSet)
		displayHangman(noOfErrors)
		print()
		guessingLetter = input("Player 2: Guess a Letter: ").upper()
		if hasLetterBeenUsed(correctSet, letterSet, guessingLetter):
			print("You have already gussed this Letter. Try another")
		else:
			if checkGuessingLetter(wordToGuess, guessingLetter):
				correctSet.add(guessingLetter)
			else:
				letterSet.add(guessingLetter)
				noOfErrors += 1

		isWon = hasPlayerWon(wordToGuess,correctSet)
		isLoss = hasPlayerLost(noOfErrors)

	if isWon:
		displayWinner(wordToGuess)
	elif isLoss:
		displayLoser()

gameLoop()

