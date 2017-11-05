def longest_word(string):
    '''longest_word(string) -> int
    returns the length of the longest word in string'''
    wordList = string.split()
    maxLength = 0  # initialize the max length
    for word in wordList:
        if len(word) > maxLength: # found a new longest word
            maxLength = len(word) # set maxLength to the new longest length
    return str(word) + ': ' + str(maxLength)

print(longest_word('Art of Problem Solving'))
