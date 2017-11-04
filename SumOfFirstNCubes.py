n = int(input("Enter a positive integer: ")) # obtain user input

sumOfCubes = 0 # initialize variable 'sumOfCubes'

for i in range(1, n+1): # loop through each integer 1-n (including n)
    sumOfCubes += (i)**3 # calculate sumOfCubes, according to loop variable
    iTriangularNum = (((i)*(i+1))/2) # calculate the 'i'th triangular number
    print("\nthe sum of the first " + str(i) + " cube(s) is equal to " + str(sumOfCubes) + ", the square of " + str(iTriangularNum)) # print results 
