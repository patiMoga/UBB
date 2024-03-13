import sympy

alphabet = ' abcdefghijklmnopqrstuvwxyz'

letter_to_index = dict(zip(alphabet, range(len(alphabet)))) # maps the letters of alphabet to indexes
index_to_letter = dict(zip(range(len(alphabet)), alphabet)) # maps the indexes to letter of alphabet

k,l=2,3

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


def decode_number_to_text(number):
    # Function to convert a number to a two-letter block
    def number_to_block(num):
        first_letter_index = (num // 27)
        second_letter_index = num % 27
        return index_to_letter[first_letter_index] + index_to_letter[second_letter_index]

    # Convert the number to a list of two-letter blocks
    blocks = []
    while number > 0:
        block = number % (27 * 27)
        blocks.append(number_to_block(block))
        number //= (27 * 27)

    # Reverse the order of blocks and join them to get the final text
    text = ''.join(blocks[::-1])

    return text

def generate_prime_numbers(start, end):
    primes = []
    for num in range(start, end + 1):
        if sympy.isprime(num) and num % 4 == 3:
            primes.append(num)
    return primes


def generate_primes_and_product(min_product, max_product):
    while True:
        # Generate two prime numbers
        primes = generate_prime_numbers(100, 1000)
        if len(primes) < 2:
            continue

        p, q = primes[:2]

        # Calculate the product
        product = p * q

        # Check if the product is within the desired range
        if min_product <= product <= max_product:
            return p, q

def encrypt(message, n):
    # Ensure the message has an even length
    if len(message) % 2 != 0:
        message += ' '

    # Function to convert a two-letter block to a numerical value
    def block_to_number(block):
        return (letter_to_index[block[0]]) * 27 + letter_to_index[block[1]]

    # Split the message into two-letter blocks and convert each block to a number
    values = [block_to_number(message[i:i+2]) for i in range(0, len(message), 2)]
    encrypted=[]
    for c in values:
        c=pow(c,2,n)
        encrypted.append(c)

    text=[]
    for num in encrypted:
        text.append(decode_number_to_text(num))
    for i in range(len(text)):
        text[i]=text[i][1:]

    return text

def decrypt(text,p,q):
    numbers=[]
    message=[]
    for i in range(len(text)):
        value=letter_to_index[text[i][0]]*729
        value+=letter_to_index[text[i][1]]*27
        value+=letter_to_index[text[i][2]]
        numbers.append(value)
    for num in numbers:
        # Compute square roots modulo p and q
        mp = pow(num, (p + 1) // 4, p)
        mq = pow(num, (q + 1) // 4, q)

        # Use extended Euclidean algorithm to find yp and yq
        yp = modinv(p, q)
        yq = modinv(q, p)
        r=[]
        # Use Chinese remainder theorem to find four square roots modulo n
        r1 = (yp * p * mq + yq * q * mp) % (p * q)
        r2 = (p * q) - r1
        r3 = (yp * p * mq - yq * q * mp) % (p * q)
        r4 = (p * q) - r3
        r.append(r1)
        r.append(r2)
        r.append(r3)
        r.append(r4)
        ra=min(r)
        message.append(decode_number_to_text(ra))
    return "".join(message)



def printmeniu():
    print("1 Criptare mesaj: ")
    print("2 Decriptare mesaj ")
    print("x Iesire ")

def main():
    p, q = generate_primes_and_product(729, 19683)
    n = p * q
    ciphertext=""
    while True:
        printmeniu()
        op=input()
        if op=="1":
            print("Introduceti mesaj")
            mes=input()
            for i in range(len(mes)):
                if mes[i] not in alphabet:
                    print("Mesaj gresit")
                    return
            ciphertext=encrypt(mes,n)
            print("".join(ciphertext))
        if op=="2":
            message=decrypt(ciphertext,p,q)
            print(message)
        if op=="x":
            break
main()