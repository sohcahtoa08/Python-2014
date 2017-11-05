def anagramsList(inputString):
    '''anagramsList(inputString) -> list
    returns list of all permutations (with
    each character a subelement of a list)
    of inputString'''
    inputList = list(inputString)
    # base case
    if len(inputList) == 1:
        return [inputList[:]]
    # recursive step
    outputList = []
    for index in range(len(inputList)):
        # construct all permutations that start with the item
        #   at location given by index
        # remove item and permute the rest
        restOfList = inputList[:index]+inputList[index+1:]
        perms = anagramsList(restOfList)
        # add all permutations starting with inputList[index]
        #   and ending with each permuatation just generated
        for tail in perms:
            outputList.append([inputList[index]]+tail)
    return outputList

def anagrams(inputString):
    '''anagrams(inputList) -> list
    returns the inputList with each
    element of each nested list within
    inputList joined together'''
    inputList = anagramsList(inputString) # inputList = list of all permutations (with each character a subelement of a nested list) of the inputted text
    joinedList = [] # initialize empty list named 'joinedList'
    for item in inputList: # for each nested list in 'inputList'...
        joinedList.append(''.join(item)) # join the items of the list together, and add the result to 'joinedList'
    return joinedList # return 'joinedList'

def jumble_solve(inputString):
    '''jumble_solve(inputString) -> list
    returns list of all valid words that
    are anagrams of inputString'''
    validWords = [] # initialize 'validWords' as empty list
    inputFile = open('wordlist.txt','r') # open 'wordlist.txt' file
    wordList = inputFile.readlines() # read the lines of the file and assign the list to 'wordList'
    inputFile.close() # close the file
    inputString = inputString.lower() # make all letters in the inputted string lowercase
    for word in wordList: # for each word in 'wordList'...
        word = word.strip('\n') # strip off the newline character
        for item in anagrams(inputString): # for each anagram of the inputted string...
            if item == word: # check to see if the item is equal to the word in 'wordList'
                if item not in validWords: # if it is and is also not already in 'validWords' (avoids repetition), then add it to 'validWords'
                    validWords.append(item)
    return validWords # return 'validWords'


# test cases
print(jumble_solve('CHWAT'))
print(jumble_solve('RAROM'))
print(jumble_solve('CEPLIN'))
print(jumble_solve('YAFILM'))
