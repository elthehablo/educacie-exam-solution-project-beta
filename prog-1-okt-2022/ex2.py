def drawHangman(gamestate):
    """
    displays the current situation of hangman. gamestate is an array that shows how far the gallow is
    """
    print("-----  ")
    print("|   |")
    
    print("|", end = "")
    if gamestate > 0:
        print("   O")
    else:
        print("")
    print("|", end = "")
    if gamestate > 1:
        if gamestate > 2:
            if gamestate > 3:
                print("  {D}")
            else:
                print("  {D")
        else:
            print("   D")
    else:
        print("")
    print("|", end = "")
    if gamestate > 4:
        if gamestate > 5:
            print("   ||")
        else:
            print("   |")
    else:
        print("")
    print("-------")

def checkGuess(guess, wordguess, word):
    sum = 0
    for i in range(len(word)):
        if word[i] == guess:
            wordguess[i] = guess
            sum += 1
    print(str(sum)+" instances of letter found!")
    return wordguess, sum

def printWordguess(wordguess):
    """
    shows a visual interface that displays how many letters are still needed to guess the word as well as the letters that are already filled in
    """
    for i in range(len(wordguess)):
        if wordguess[i] == "":
            print("_", end = "")
        else:
            print(wordguess[i], end = "")
    print("")

def comparewords(wordguess, hangmanword):
    """
    boolean function to determine whether the guessed word as it stands is exactly the same as the hangman word
    returns: True if the word is exactly the same, False otherwise
    """
    boolarr = len(hangmanword)*[False]
    for i in range(len(hangmanword)):
        if(wordguess[i] == hangmanword[i]):
            boolarr[i] = True
    for i in range(len(boolarr)):
        if boolarr[i] == False:
            return False
    return True

def gallows():
    """
    plays a game of hangman
    """
    hangmanword = input("Word to use: ")
    gamestate = 0
    wrongguesses = []
    wordguess = len(hangmanword)*[""]
    while gamestate < 6 and comparewords(wordguess, hangmanword) == False:
        drawHangman(gamestate)
        printWordguess(wordguess)
        print("wrongly guessed letters:", end = "")
        print(wrongguesses)
        guess = input("Guess a letter: ")
        wordguess, test = checkGuess(guess, wordguess, hangmanword)
        if test == 0:
            gamestate += 1
            wrongguesses.append(guess)
    drawHangman(gamestate)
    if gamestate > 5:
        print("you lost!")
    else:
        print("you won!")

gallows()