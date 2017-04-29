from math import pow

def sum_square_diff():
    sum_squares = 0
    square_of_sum = 0
    for i in range(1,101):
        sum_squares += pow(i,2)
        square_of_sum +=i

    return int(pow(square_of_sum,2) - sum_squares)

if __name__=="__main__":
    print(sum_square_diff())