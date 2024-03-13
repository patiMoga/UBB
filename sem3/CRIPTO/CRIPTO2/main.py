def gcd(a, b):
    """
    :return: the greatest commonn divisor between n and all the modules of n
    """
    while b != 0:
        a, b = b, a % b
    return a
def find_generators(n):
    """
    :return: all the generators for n
    """
    generators = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            generators.append(i)
    return generators


if __name__ == '__main__':
    print(find_generators(12))
    print(find_generators(8))
    print(find_generators(13))
    print(find_generators(7))