#
# Implement the program to solve the problem statement from the third set here
#
# Generate the largest perfect number smaller than a given natural number n. If such a number does not exist, 
# a message should be displayed. A number is perfect if it is equal to the sum of its divisors, except itself. 
# (e.g. 6 is a perfect number, as 6=1+2+3).

def sumDiv (value):
    s=1
    for index in range(2,value//2+1,1):
        if value%index==0:
            s=s+index
    return s

def solve_perfect(n):
    if n<=6:
        return False
    else:
        for index in range(n-1,5,-1):
            if sumDiv(index)==index:
                return index

def main():
    n=int(input("n="))
    if solve_perfect(n)==False:
        print("There is no perfect number smaller than n="+str(n))
    else:
        print("The largest perfect number smaller than n="+str(n),"its m="+str(solve_perfect(n)))

main()