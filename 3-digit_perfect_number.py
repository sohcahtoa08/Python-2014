def is_multiple(x,y):
    '''is_multiple(x,y) -> bool
    returns True is x is a multiple of y, False otherwise'''
    # check if y divides evenly into x
    (x % y == 0)
    return y # return y's value to be used in function sum_of_proper_divs

def sum_of_proper_divs(n):
    '''Return sum of the proper divisors of parameter n.'''
    total = 0 # initializes total
    x = n # initializes x
    y = 1 # initializes y
    while y != x: # while loop, "While y is not equal to x..."
        is_multiple(x, y) # calls function is_multiple
        if (x % y == 0): # if x is divisible by y, then add y to total and assign the sum to variable total
            total += y
        y += 1 # increase y by 1 each iteration
    return total

print(sum_of_proper_divs(6)) # should be 6
print(sum_of_proper_divs(28)) # should be 28
print(sum_of_proper_divs(10)) # should be 8

for i in range(100, 1000): # test all 3 digit number for i
    if sum_of_proper_divs(i) == i: # if the sum of proper divisors of i is equal to i, then print i
        print(i)
