import random
timesPlayed = 0

def return_matches(guess, code):
    black,white = 0,0
    blackMatch = [False]*len(guess)
    whiteMatch = [False]*len(guess)
    for n in range(len(guess)):
        if guess[n] == code[n]:
            blackMatch[n] = True
            whiteMatch[n] = True
            black += 1
    for n in range(len(guess)):
        if not blackMatch[n]:
            for char in range(len(guess)):
                if not whiteMatch[char] and guess[n] == code[char]:
                    whiteMatch[char] = True
                    white += 1
                    break
    return (black,white)

codeLength = int(input("How long would you like the code to be made?"))
numGuesses = int(input("How many guesses would you like?"))
difficulty = str(input("Pick a difficulty level: 'easy' or 'hard'?"))

def play_mastermind(codeLength, numGuesses, difficulty):
    while timesPlayed > 0:
        codeLength = int(input("How long would you like the code to be made?"))
        numGuesses = int(input("How many guesses would you like?"))
        difficulty = str(input("Pick a difficulty level: 'easy' or 'hard'?"))
        break
    colors = 'rybgop'
    code = ''
    winner = False
    for i in range(codeLength):
        color = colors[random.randrange(len(colors))]
        while difficulty == 'easy' and color in code:
            color = colors[random.randrange(len(colors))]
        code += color
    print("I've got a code of length "+str(codeLength))
    print("It uses colors in "+colors)
    for turn in range(1,numGuesses+1):
        legalGuess = False
        while not legalGuess:
            guess = input("Guess #"+str(turn)+" -- enter your guess: ")
            legalGuess = True
            if len(guess) == codeLength:
                for index in range(codeLength):
                    if guess[index] not in colors:
                        legalGuess = False
            else:
                legalGuess = False
            if not legalGuess:
                print("Sorry, that's not a legal guess!")
        (black,white) = return_matches(guess, code)
        if black==codeLength:
            print("Congrats, you cracked the code in only " + str(turn) + " guess(es)! You really are a Mastermind.")
            winner = True
            break
        print(str(black)+" black "+str(white)+ " white")
    if not winner:
        print("Sorry, you ran out of guesses!")
        print("You were so close! The code was actually: "+str(code))
        playAgain = str(input("What would you like to do now ('play again' or 'quit')?"))
        if playAgain == 'play again':
            play_mastermind(codeLength, numGuesses, difficulty)
        elif playAgain == 'quit':
            quit()
        else:
            playAgain = str(input("Sorry, that's not a valid response. What would you like to do now ('play again' or 'quit')?"))


play_mastermind(codeLength, numGuesses, difficulty)

while True:
    playAgain = str(input("What would you like to do now ('play again' or 'quit')?"))
    if playAgain == 'play again':
        timesPlayed += 1
        play_mastermind(codeLength, numGuesses, difficulty)
    elif playAgain == 'quit':
        quit()
    else:
        playAgain = str(input("Sorry, that's not a valid response. What would you like to do now ('play again' or 'quit')?"))

