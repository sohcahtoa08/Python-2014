file = open("wordlist.txt", "r")
count = 0
for line in file:
    if len(line) == 11:
        count += 1
        print(line)
file.close()
print(count)
