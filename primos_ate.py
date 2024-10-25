import math

'''
Para essa solução, criei uma função auxiliar "eh_primo" para determinar se um número é primo. A função principal é 
"primos_ate", que retorna a lista desejada.
'''


def eh_primo(num):
    if num == 2:
        return True

    elif num == 1 or num % 2 == 0:
        return False

    else:
        raiz = int(math.sqrt(num))
        for i in range(3, raiz+1, 2):
            if num % i == 0:
                return False

    return True


def primos_ate(num):
    if type(num) is not int:
        raise TypeError

    if num <= 1:
        raise ValueError

    primos = [2]

    for i in range(3, num + 1, 2):
        if eh_primo(i):
            primos.append(i)

    return primos


# Se a solução deve ser feita com uma única função, eu faria assim:
def p(num):
    if type(num) is not int:
        raise TypeError

    if num <= 1:
        raise ValueError

    primos = [2]

    for i in range(3, num + 1, 2):
        primo = True

        raiz = int(math.sqrt(i))

        for j in range(3, raiz + 1, 2):
            if i % j == 0:
                primo = False
                break

        if primo:
            primos.append(i)

    return primos


