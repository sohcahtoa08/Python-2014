numAnswered = int(input("Enter the number of questions answered: "))
numCorrect = int(input("Enter the number of questions correct: "))
score = (6 * numCorrect) + (1.5 * (25 - numAnswered))
print("The student's score is: " + str(score) + " out of a possible 150 points.")
