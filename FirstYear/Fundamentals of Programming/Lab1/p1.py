#
# Implement the program to solve the problem statement from the first set here
#
# Given natural number n, determine the prime numbers p1 and p2 such that n = p1 + p2 (check the Goldbach hypothesis).
def prim(value):
    if value==2:
        return 1
    if value%2==0:
        return 0
    for index in range(3,int(value/2),2):
        if value%index==0:
            return 0
    return 1

def solve_odd(number):
    if prim(number-2)==1:
        return number-2       
    else:
        return False

def solve_even_1(number):
    if(prim(int(number/2))==1):
        return number//2
    else:
        return False

def add(n):
    if (n//2)%2==1:
        return 1
    else:
        return 0

def solve_even_2(n,nr):
    sw=0
    while int(n/2)-nr>2:
        if prim(int(n/2)-nr)==1 & prim(int(n/2)+nr)==1:
            p1=int(n/2)-nr
            p2=int(n/2)+nr
            print("p1="+str(p1),"p2="+str(p2))
            sw=1
        nr=nr+2
    return sw

def main():
    n=int(input("n="))
    if n<=3:
        print("There are no such values for p1 and p2")
    else:
        if n%2==1:
            if solve_odd(n)==False:
                print("There are no such values for p1 and p2")
            else:
                print("p1=",solve_odd(n),"p2=2")
        else:
            if not solve_even_1:
                print("p1=p2="+str(solve_even_1(n)))
            nr=1+add(n)
            if solve_even_2(n,nr)==0:
                print("There are no such values for p1 and p2")

main()