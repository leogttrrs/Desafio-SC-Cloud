def fib(num):
    if type(num) is not int:
        raise TypeError

    if num < 0:
        raise ValueError

    atual = 0
    auxiliar = 1

    for i in range(num):
        prox_auxiliar = atual + auxiliar
        atual = auxiliar
        auxiliar = prox_auxiliar

    return atual
