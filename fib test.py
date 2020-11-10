def positivefib(a):
    fib1, fib2 = 1, 1
    arr = [0]
    n = 50
    while n > 0:
        fib1, fib2 = fib2, fib1 + fib2 
        n -= 1
        if fib2 % 2 == 0:
            arr.append(fib2)

    return arr[0:a] #тут получился смешной костыль


