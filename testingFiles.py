File = open('wordlist.txt','r')
wordList = File.readlines()



text = 'the quick brown fox jumps over the lazy dog'

List = text.split()

for words in wordList:
    words = words.strip('\n')
    for word in List:
        if words == word:
            print(True)


File.close()
