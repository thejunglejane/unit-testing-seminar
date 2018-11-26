def is_even(n):
    '''Return True if ``n`` is an even number, otherwise return False.'''
    if n % 2 == 0:
        return True
    return False


def is_odd(n):
    '''Return True if ``n`` is an odd number, otherwise return False.'''
    if n % 2 != 0:
        return True
    return False


def is_composite(n):
    '''Return True if ``n`` is a composite number, otherwise return
    False.
    '''
    for i in range(n):
        if n % i != 0:
            return False
    return True


def is_prime(n):
    '''Return True if ``n`` is a prime number, otherwise return False.'''
    for i in range(n):
        if n % i == 0:
            return False
    return True

