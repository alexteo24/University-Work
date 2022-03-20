#
# Implement the program to solve the problem statement from the second set here
#
# Determine the twin prime numbers p1 and p2 immediately larger than the given non-null natural number n. 
# Two prime numbers p and q are called twin if q - p = 2.

def prime(value):
    if value == 2:
        return 1
    if value % 2 == 0:
        return 0
    for index in range(3, value // 2, 2):
        if value % index == 0:
            return 0
    return 1


def find_q(n):
    q = n + 1 + n % 2
    sw = 0
    while sw == 0:
        if prime(q) == 1:
            if prime(q+2) == 1:
                return q
        q = q + 2


def main():
    n = int(input("n="))
    print("The two twin prime numbers immediately larger than n are q="+str(find_q(n)), "and p="+str(find_q(n)+2))


main()
