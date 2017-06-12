from Problem0003 import is_prime

def summazation_primes():
    sum=0
    for i in range(0,2000000):
        if is_prime(i):
            sum+=i
    return sum

if __name__=="__main__":
    print(summazation_primes())

