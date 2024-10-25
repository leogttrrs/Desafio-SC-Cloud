import math

'''
Para essa solução, criei uma função auxiliar "eh_primo" para determinar se um número é primo. A função principal é 
"primos_ate_rec", que retorna a lista desejada.
'''


def eh_primo(num):
    if num == 2:
        return True
    elif num == 1 or num % 2 == 0:
        return False
    else:
        raiz = int(math.sqrt(num))
        for i in range(3, raiz + 1, 2):
            if num % i == 0:
                return False
    return True


def primos_ate_rec(num, atual=3, primos=None):
    if primos is None:
        primos = [2]

    if type(num) is not int:
        raise TypeError
    if num <= 1:
        raise ValueError

    if atual > num:
        return primos

    if eh_primo(atual):
        primos.append(atual)

    return primos_ate_rec(num, atual + 2, primos)


# Se a solução deve ser feita com uma única função, eu faria assim:
def p_rec(num, atual=3, primos=[2], divisor=3):
    if type(num) is not int:
        raise TypeError
    if num <= 1:
        raise ValueError

    if atual > num:
        return primos

    if divisor > int(math.sqrt(atual)):
        primos.append(atual)
        return p_rec(num, atual + 2, primos, 3)
    elif atual % divisor == 0:
        return p_rec(num, atual + 2, primos, 3)
    else:
        return p_rec(num, atual, primos, divisor + 2)
