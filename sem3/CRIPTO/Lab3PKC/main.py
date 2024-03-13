
def pollards_rho(n, f, x0):
    def gcd(a, b): #computes the gcd
        if (b == 0):
            return a
        else:
            return gcd(b, a % b)
    x = x0
    y = x0
    d = 1

    while d == 1: #while the program doesnt find a gcd different than one it keeps going
        x = f(x) % n
        y = f(f(y)) % n
        d = gcd(abs(x - y), n)

    if d == n:
        return None #returns none if the number is prime

    return d

n = 127
f=lambda x: x*x+1; #the function
x0=2; #first value of x0
f1 = pollards_rho(n,f,x0)
if f1 is None:
    print(f"Pollard's method failed")
    print()
else:
    f2 = n // f1
    if (f1 > f2):
        aux = f1
        f1 = f2
        f2 = aux
    print(f"1. The factors of {n} are {f1} and {f2}.")
    print()


n = 8051
f1 = pollards_rho(n,f,x0)
if f1 is None:
    print(f"Pollard's method failed")
    print()
else:
    f2 = n // f1
    if(f1>f2):
        aux=f1
        f1=f2
        f2=aux
    print(f"2. The factors of {n} are {f1} and {f2}.")
    print()

n = 8159
f1 = pollards_rho(n,f,x0)
if f1 is None:
    print(f"Pollard's method failed")
    print()
else:
    f2 = n // f1
    if(f1>f2):
        aux=f1
        f1=f2
        f2=aux
    print(f"3. The factors of {n} are {f1} and {f2}.")
    print()

n = 6193
f1 = pollards_rho(n,f,x0)
if f1 is None:
    print(f"Pollard's method failed")
    print()
else:
    f2 = n // f1
    if(f1>f2):
        aux=f1
        f1=f2
        f2=aux
    print(f"4. The factors of {n} are {f1} and {f2}.")
    print()