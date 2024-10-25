def fib_rec(num):
    if type(num) is not int:
        raise TypeError

    if num < 0:
        raise ValueError

    if num == 0:
        return 0

    if num <= 2:
        return 1

    return fib_rec(num-1) + fib_rec(num-2)
