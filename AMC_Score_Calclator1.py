numCorrect = int(input("Enter the number of questions correct: "))
numBlank = int(input("Enter the number of questions left blank: "))
score = (6 * numCorrect) + (1.5 * numBlank)
print("The student's score is: " + str(score) + " out of a possible 150 points.")
