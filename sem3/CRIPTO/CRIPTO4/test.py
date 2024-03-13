def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m

def square_root_modulo(c, p, q):
    # Compute square roots modulo p and q
    mp = pow(c, (p + 1) // 4, p)
    mq = pow(c, (q + 1) // 4, q)

    # Use extended Euclidean algorithm to find yp and yq
    yp = modinv(p, q)
    yq = modinv(q, p)

    # Use Chinese remainder theorem to find four square roots modulo n
    r1 = (yp * p * mq + yq * q * mp) % (p * q)
    r2 = (p * q) - r1
    r3 = (yp * p * mq - yq * q * mp) % (p * q)
    r4 = (p * q) - r3

    return r1, r2, r3, r4

# Example usage:
c = 729  # Replace with your actual value of c
p = 103   # Replace with your actual value of p
q = 107  # Replace with your actual value of q

roots = square_root_modulo(c, p, q)
print("Square Roots modulo n:", roots)
