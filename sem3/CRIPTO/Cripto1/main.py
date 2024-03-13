import time
#gcd using Euclid method
def gcd1(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

#gcd using the dividing method
def gcd2(a, b):
    if a > b:
        small = b
    else:
        small = a
    for i in range(1, small + 1):
        if ((a % i == 0) and (b % i == 0)):
            gcd = i

    return gcd

#gcd using the repeated substractions method
def gcd3(a, b):
    if a*b==0:
        return a+b
    while a != b:
        if a > b:
            a = a - b
        else: b = b - a
    return a

#print menu for the 3 methods
def menu():
    print("1 - Euclidean method\n"
          "2 - Dividing method\n"
          "3 - Repetead substractions method\n")

#the menu
def run_menu():
    a = int(input("The first number: "))
    b = int(input("The second number: "))
    while True:
        menu()
        opt = input("Chose one method: ")
        if(opt=="1"):
            tic = time.perf_counter()
            print(gcd1(a,b))
            toc = time.perf_counter()
            print(toc-tic)
        elif(opt=="2"):
            tic = time.perf_counter()
            print(gcd2(a,b))
            toc = time.perf_counter()
            print(toc - tic)
        elif(opt=="3"):
            tic = time.perf_counter()
            print(gcd3(a,b))
            toc = time.perf_counter()
            print(toc - tic)
        else: exit(0)


if __name__ == '__main__':

    # 10 test for each method, calculating the runtimes to see which one is the most efficient one
    tic = time.perf_counter()
    print('1. GCD between 2 and 4 is', gcd1(2,4))
    toc = time.perf_counter()
    print('Euclidean method: ', toc-tic)
    tic = time.perf_counter()
    gcd2(2, 4)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(2, 4)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('2. GCD between 9 and 27 is', gcd1(9, 27))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(9, 27)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(9, 27)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('3. GCD between 32 and 24 is', gcd1(32, 24))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(32, 24)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(32, 24)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('4. GCD between 35 and 25 is', gcd1(35, 25))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(35,25)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(35,25)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('5. GCD between 283 and 349 is', gcd1(283,349))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(283,349)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(283,349)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('6. GCD between 542 and 876 is', gcd1(542,876))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(542,876)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(542,876)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('7. GCD between 222 and 888 is', gcd1(222,888))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(222,888)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(222,888)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('8. GCD between 28 and 126 is', gcd1(28, 126))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(28, 126)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(28, 126)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('9. GCD between 45 and 789 is', gcd1(45,789))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(45,789)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(45, 789)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()

    tic = time.perf_counter()
    print('10. GCD between 1234 and 348 is', gcd1(1234,348))
    toc = time.perf_counter()
    print('Euclidean method: ', toc - tic)
    tic = time.perf_counter()
    gcd2(1234,348)
    toc = time.perf_counter()
    print('Dividing method', toc - tic)
    tic = time.perf_counter()
    gcd3(1234,348)
    toc = time.perf_counter()
    print('Repetead substractions method', toc - tic)
    print()



    run_menu()








