from Problem0003 import is_prime

def find_nth_prime(n):
    i = 0
    counter = 0
    while True:
        if is_prime(i):
            counter +=1
        i +=1
        if counter==n:
            break
    return i-1

if __name__=="__main__":
    print(find_nth_prime(10001))

