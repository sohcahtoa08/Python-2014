import random
number = random.randrange(101) # number is any integer from 0 to 100

name = str(input("Hello! My name is Computer. Nice to meet you. What's your name?")) # asks the user his/her name
# the following line explains the instructions and asks if the user is ready to play
intro = str(input("Okay, " + name + """, let's play a game. You have 10 lives to correctly guess the number I am thinking of. The number can be anywhere from 0-100 (inclusive). If you do not guess the number I am thinking of correctly within 10 guesses, then you lose, and I win. Ha ha ha! Are you up for the challenge (just say yes)?"""))
livesUsed = 0 # initialize livesUsed to 0
if intro == "yes": # intro should always be yes
    guess = int(input("Great! Let's begin. I'm thinking of a number between 0 and 100. Can you guess what number I am thinking of?")) # assigns variable guess to user's first guess
    for i in range(9): # repeats body of for loop 9 times
        if guess != number: # if guess is not equal to number...
            if guess < number: # if guess is greater than number...
                guess = int(input("Your guess is too low! Guess again: ")) # guess is too low, asks user for next guess
                livesUsed += 1 # increase livesUsed by 1
            elif guess > number: # if guess is less than number...
                guess = int(input("Your guess is too high! Guess again: ")) # guess is too high, asks user for next guess
                livesUsed += 1 # increase livesUsed by 1
        else: # if guess is equal to number
            livesUsed += 1 # increase livesUsed by 1
            break # exit the for loop
        

if guess == number: # if user guessed number correctly within 10 lives, print a variety of responses telling how many guesses it took the user to correctly guess the number, as well as a custom comment based off of this information
    if livesUsed <=3:
        print("Amazing!! You guessed my number in only " + str(livesUsed) + " guess(es)! You should seriously consider mind-reading as your future profession!")
    elif livesUsed > 3 and livesUsed <= 7:
        print("Eh. You're average, because you guessed my number in " + str(livesUsed) + " guesses. Keep practicing!")
    elif livesUsed > 7 and livesUsed <= 10:
        print("You guessed my number in " + str(livesUsed) + " guesses. You know, this game isn't for everyone, but if you're really determined, practice makes perfect. A LOT of practice.")
else: # if user did not correctly guess number within 10 lives, reveal number
    print('Whoops, you exhausted your lives! The number I was thinking of was actually ' + str(number) + '. But, on the bright side, I won! Better luck next time!')
