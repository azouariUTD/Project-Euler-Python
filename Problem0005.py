from Problem0003 import is_prime

def smallest_multiple():
    prod = 1
    for i in range(1,21):
        if is_prime(i):
            prod = i * prod
        else:
            if i < 10 and i%2==0:
                prod = 2 * prod
            elif i < 10 and i%3==0:
                prod=3*prod
    return prod

if __name__=="__main__":
    prod = smallest_multiple()
    print(prod)
