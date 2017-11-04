# Python Class 955
# Lesson 4 Problem 6
# Author: sohcahtoa08 (215098)

# calculate lcm (for fractions, least common denominator) of 2 numbers
def lcm(num1, num2):
    '''lcm(num1, num2) -> int
    returns the least common
    multiple of num1 and num2'''
    # greaterNum represents the least possible valuable that lcm can be
    if num1>num2:
        greaterNum = num1 
    else:
        greaterNum = num2
    # keep increasing greaterNum by 1 until num1 and num2 can both divide evenly into greaterNum
    while True:
        if greaterNum%num1==0 and greaterNum%num2==0:
            lcm = greaterNum
            break # break when we find lcm
        greaterNum+=1
    return lcm

class Fraction:
    '''represents fractions'''
    
    def __init__(self, num, denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        else:
            # define the fraction's attributes (numerator and denominator)
            self.num = num
            self.denom = denom

    def __str__(self):
        '''str(Fraction) -> str
        string representation of
        fraction in lowest terms'''
        gcd = 0
        # differentiate which is greater between numerator and denominator
        minNum = min([self.num, self.denom])
        maxNum = max([self.num, self.denom])
        # if the smaller number is negative, make it positive (so that we can loop through it later)
        if minNum<0:
            minNum*=-1
        # calculate the gcd that evenly divides into both the numerator and denominator of the fraction
        for i in range(1, minNum+1):
            if minNum%i==0 and maxNum%i==0 and i>gcd:
                gcd = i
        # update the numerator and denominator of the fraction accordingly
        self.num, self.denom = self.num // gcd, self.denom // gcd
        if self.denom < 0: # transfers the negative sign to the numerator if it is in the denominator
            self.num, self.denom = self.num * -1, self.denom * -1
        if self.num % self.denom == 0: # if we can return an integer from the fraction, we return it here
            return str(self.num // self.denom)
        else: # otherwise, we just return the simplified fraction
            return str(self.num) + '/' + str(self.denom)
    
    def __float__(self):
        '''float(Fraction) -> float
        float representation of fraction'''
        return float(self.num/self.denom) # fairly straightforward

    def __add__(self, other):
        '''self+other -> Fraction object
        returns sum of self and other as
        a Fraction object.'''
        denom = lcm(self.denom, other.denom) # find the least common denominator for both denominators
        # update both numerators accordingly
        selfNum = self.num*(denom // self.denom)
        otherNum = other.num*(denom // other.denom)
        return Fraction((selfNum+otherNum),denom) # return sum

    def __sub__(self, other):
        '''self-other -> Fraction object
        returns difference between self
        and other as a Fraction object'''
        if self==other:
            return str(0) + '/1' 
        else:
            denom = lcm(self.denom, other.denom) # find the least common denominator for both denominators
            # update both numerators accordingly
            selfNum=self.num*(denom // self.denom)
            otherNum=other.num*(denom // other.denom)
            return Fraction((selfNum-otherNum),denom) # return difference

    def __mul__(self, other):
        '''self*other -> Fraction object
        returns product of self and other
        as a Fraction object'''
        return Fraction((self.num*other.num),(self.denom*other.denom)) # multiply both numerators and denominators and return the resulting fraction

    def __truediv__(self, other):
        '''self/other -> Fraction object
        returns quotient of self and other
        as a Fraction object'''
        return Fraction((self.num*other.denom),(self.denom*other.num)) # return quotient

    def __eq__(self, other):
        '''self==other -> bool
        returns True if self==other;
        otherwise, returns False'''
        return (float(self)==float(other)) # fairly straightforward

# test cases

p = Fraction(1,2)
print(p)  # should print 1/2
q = Fraction(2,-6)
print(q)  # should print -1/3

print()
x = float(p)
print(x)  # should print 0.5

### if overloading using special methods
print()
print(p+q)  # should print 1/6
print(p-q)  # should print 5/6
print(p-p)  # should print 0/1
print(p*q)  # should print -1/6
print(p/q)  # should print -3/2
print()
print(p==p) # True
print(p==q) # False

# some extra test cases

# all possible cases of fractions
print()
print(Fraction(5,10)) # should print 1/2
print(Fraction(10,5)) # should print 2
print(Fraction(-5,10)) # should print -1/2
print(Fraction(5,-10)) # should print -1/2
print(Fraction(-10,5)) # should print -2
print(Fraction(10,-5)) # should print -2
print(Fraction(-5,-5)) # should print 1
print(Fraction(10,10)) # should print 1
print()
print(Fraction(9,6)) # should print 3/2
print(Fraction(-9,6)) # should print -3/2
print(Fraction(9,-6)) # should print -3/2
print(Fraction(-9,-6)) # should print 3/2
print()

# equality test
f1 = Fraction(1,2)
f2 = Fraction(9,18)
print(f1==f2) # True
