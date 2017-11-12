def fibo(n, memo):
    if n <= 2:
        f = 1
    elif n in memo:
        f = memo[n]
    else:
        f = fibo(n-1, memo) + fibo(n-2, memo)
    memo[n] = f
    return f

memo ={}
print(fibo(40, memo))

