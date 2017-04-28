from math import sqrt

def is_prime(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif n%2==0 or n%3==0:
        return False

    i = 5
    while i*i <= n:
        if n%i==0 or n%(i+2)==0:
            return False
        i +=6

    return True

def largest_prime_factor(n):
    largest_prime = 0
    for i in range(1,int(sqrt(n))-1):
        if is_prime(i) and n%i==0:
            largest_prime = i
    return largest_prime

if __name__=="__main__":
    print(largest_prime_factor(600851475143))