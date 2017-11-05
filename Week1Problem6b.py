values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}

wordFile = open("wordlist.txt", "r")
wordFile = wordFile.readlines()

highestWord = ''
highestScore = 0

for word in wordFile:
    if len(word) == 8 and 'z' not in word:
        score = 0
        for letter in word:
            for key in values.keys():
                if letter == key.lower():
                    score += values[key]
        if score > highestScore:
            # to get both answers,
            # try 'if score > highestScore:' to get only the one that comes first in the file
            # 'if score >= highestScore:' to get only the one that comes later on in the file
            highestScore = score
            highestWord = word
print(highestWord + str(highestScore))
