def even_fib():
    fib_list = [1,2]
    i = 1
    sum = 2
    while True:
        fib_list.append(fib_list[i-1] + fib_list[i])
        if fib_list[i+1] > 4000000:
            break
        if fib_list[i+1]%2 == 0:
            sum += fib_list[i+1]
        i +=1
    return fib_list, sum

if __name__=="__main__":
    fib_list,  sum = even_fib()
    print(fib_list)
    print(sum)
