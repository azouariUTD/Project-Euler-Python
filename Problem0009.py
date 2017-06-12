def special_pythagorean_triplet():
    for i in range(1,1000):
        for j in range(1,1000):
            for k in range(1,1000):
                if i*i + j*j==k*k and i+j+k==1000:
                    return i*j*k

if __name__=="__main__":
    print(special_pythagorean_triplet())