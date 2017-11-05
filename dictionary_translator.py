def translate():
    '''translate() -> None
    Prompts user to enter dictionary files and input and output files
    Changes words in input file according to the dictionary file
    Write translation in output file'''
    dictFileName = input('Enter name of dictionary (ending with ".txt"): ')
    while '.txt' not in dictFileName:
        dictFileName = input('Please make sure you enter the filename, followed by ".txt".')
    textFileName = input('Enter name of text file to translate (ending with ".txt"): ')
    while '.txt' not in textFileName:
        textFileName = input('Please make sure you enter the filename, followed by ".txt".')
    outputFileName = input('Enter name of output file (ending with ".txt"): ')
    while '.txt' not in outputFileName:
        outputFileName = input('Please make sure you enter the filename, followed by ".txt".')
    inFile = open(textFileName, 'r')
    dictFile = open(dictFileName, 'r')
    outFile = open(outputFileName, 'w')
    dictLines = dictFile.readlines()
    dictFile.close()
    textLines = inFile.readlines()
    inFile.close()
    for line in textLines:
        textLine = line.lower()
    for line in dictLines:
        dictLine = line.replace('|', ' ')
        dictLine = dictLine.split()
        dictLine = dictLine[1]
        outFile.write(dictLine)
    outFile.close()
translate()
