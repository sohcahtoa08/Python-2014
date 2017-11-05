def encipher_fence(plaintext, numRails):
    '''encipher_fence(plaintext,numRails) -> str
    encodes plaintext using the railfence cipher
    numRails is the number of rails'''
    rails = [] # initialize empty list named 'rails'
    for n in range(numRails): # for loop that repeats 'numRails' times
        rails.append(plaintext[n::numRails]) # start at the nth position in 'plaintext' and add every 'numRail'th letter to a rail in the 'rails' list
    rails.reverse() # reverse the order of the elements in 'rails'
    return ''.join(rails) # join the rails together to create the railfence cipher, and return the resulting string


def return_rails(text, numRails):
    '''return_rails(text, numRails) -> list
    returns list of *numRails* rails for inputted text'''
    rails = [] # initialize empty list named 'rails'
    for n in range(numRails): # for loop that repeats 'numRails' times
        rails.append(text[n::numRails]) # start at the nth position in 'plaintext' and add every 'numRail'th letter to an element in the 'rails' list
    rails.reverse() # reverse the order of the elements in 'rails'
    return rails # return the list of 'rails'


def decipher_fence(ciphertext,numRails):
    '''decipher_fence(ciphertext,numRails) -> str
    returns decoding of ciphertext using railfence cipher
    with numRails rails'''
    decipheredText = '' # initialize empty string named 'decipheredText'
    rails = return_rails(ciphertext, numRails) # assign the rails of ciphertext to a variable 'rails'
    newRails = [] # initialize empty list named 'newRails'
    x = 0 # initialize variable 'x' to 0
    y = 0 # initialize variable 'y' to 0
    for rail in rails: # for each rail in 'rails'...
        y += len(rail) # add the length of the rail to variable 'y'
        newRails.append(ciphertext[x:y]) # add characters x to y (slicing) to list 'newRails'
        x = y # x is assigned the value of y
    newRails.reverse() # reverse the order of the elements in 'newRails'
    for i in range(len(newRails[0])): # for i in range(length of the first rail in 'newRails)...
        for rail in newRails: # for each rail in 'newRails'...
            if len(rail) <= i: # if the length of the rail is less than or equal to loop variable i...
                continue # continue back to the top of the for loop
            else: # else...
                decipheredText += rail[i] # add the character in it 'i'th position of the rail to 'decipheredText'
    return decipheredText # return 'decipheredText'


def decode_text(ciphertext,wordfilename):
    '''decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words'''
    inputFile = open('wordlist.txt','r') # open the file
    wordList = inputFile.readlines() # read the lines of the file and assign the list to 'wordList'
    inputFile.close() # close the file
    decodedText = '' # initialize empty string named 'decipheredText'
    validWordCount = 0 # initialize variable 'validWordCount' to 0
    highestValidWordCount = 0 # initialize variable 'highestValidWordCount' to 0
    for i in range(2,(len(ciphertext)//4)): # for i in range(2 to (the length of ciphertext floor-divided by 4))...
        newText = decipher_fence(ciphertext,i) # newText is assigned the value of the 'ciphertext' deciphered with 'i' rails
        newTextList = newText.split() # split 'newText' and assign the resulting list to variable 'newTextList'
        for item in wordList: # for each item in 'wordList'...
            item = item.strip('\n') # strip off the newline character
            for word in newTextList: # for each word in 'newTextList'...
                if word == item: # if the word matches a word in 'wordList'...
                    validWordCount += 1 # add 1 to 'validWordCount'
        if validWordCount > highestValidWordCount: # if current 'validWordCount' is greater than 'highestValidWordCount'...
            highestValidWordCount = validWordCount # 'highestValidWordCount' is assigned the value of 'validWordCount'
            decodedText = newText # 'decodedText' is assigned the value of 'newText'
        validWordCount = 0 # reset 'validWordCount' to 0 for next iteration of for loop
    return decodedText # return 'decodedText'


# test cases

# enciphering
print(encipher_fence("abcdefghi", 3))
# should print: cfibehadg
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou

# deciphering
print(decipher_fence("hsi  etTi sats.",2))
# should print: This is a test.
print(decipher_fence("iiae.h  ttTss s",3))
# should print: This is a test.
print(decipher_fence("pidtopbh ya ty !Hyraou",4))
# should print: Happy birthday to you!

# decoding
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
print(decode_text("unt S.frynPs aPiosse  Aa'lgn lt noncIniha ", 'wordlist.txt'))
# should print... we'll let you find out!
