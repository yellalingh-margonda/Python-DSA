def fib2(n):
    if n<=1:
        return n
    last= fib2(n-1)
    second_last=fib2(n-2)
    return last+second_last


def fib(n):
    if n<=1:
        return 1
    return fib(n-1)+fib(n-2)
