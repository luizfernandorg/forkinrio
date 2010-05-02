#coding: utf-8


def primegen(start=1):
    """
    Setup
    >>> from itertools import islice
    >>> pp = lambda g, c: list(islice(g,c))

    Start test
    >>> pp(primegen(), 1)
    [2]
    >>> pp(primegen(), 2)
    [2, 3]
    >>> pp(primegen(), 19)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
    """
    number = start
    while True:
        if is_prime(number):
            yield number
        number += 1

# trial_division do exercício anterior
def is_prime(n):
    """
    >>> primes = [2, 3, 5, 7, 11]
    >>> all(map(is_prime, primes))
    True
    >>> non_primes = [1, 4, 6, 8, 10, 12]
    >>> any(map(is_prime, non_primes))
    False
    """
    from math import sqrt

    # Primes starts on 2
    if n <= 1: return False
    # Caso especial da porra
    if n == 2: return True
    # Numeros pares > 2 nao sao primos
    if n % 2 == 0: return False

    square_root = int(sqrt(n))
    for m in xrange(3, square_root + 1, 2): # lista de nums impares ate sqrt
        if n % m == 0:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()
