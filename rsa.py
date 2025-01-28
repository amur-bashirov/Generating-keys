import random
import sys

# This may come in handy...
from fermat import miller_rabin, mod_exp

# If you use a recursive implementation of `mod_exp` or extended-euclid,
# you recurse once for every bit in the number.
# If your number is more than 1000 bits, you'll exceed python's recursion limit.
# Here we raise the limit so the tests can run without any issue.
# Can you implement `mod_exp` and extended-euclid without recursion?
sys.setrecursionlimit(4000)

# When trying to find a relatively prime e for (p-1) * (q-1)
# use this list of 25 primes
# If none of these work, throw an exception (and let the instructors know!)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


# Implement this function
def ext_euclid(a: int, b: int) -> tuple[int, int, int]:
    """
    The Extended Euclid algorithm
    Returns x, y , d such that:
    - d = GCD(a, b)
    - ax + by = d

    Note: a must be greater than b
    """
    if b==0:
        return (1,0,a)
    x,y,z = ext_euclid(b, a % b)
    return (y,x - (a // b) * y,z)


# Implement this function
def generate_large_prime(bits=512) -> int:
    """
    Generate a random prime number with the specified bit length.
    Use random.getrandbits(bits) to generate a random number of the
     specified bit length.
    """
    while True:
        num = random.getrandbits(bits)
        if miller_rabin(num, 100):
            return num
      # Guaranteed random prime number obtained through fair dice roll


def Euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def Finde(E, p, q):
    """
    Find an encryption exponent e from the list E that is
    relatively prime to (p-1)*(q-1) and greater than 2.
    """
    phi_n = (p - 1) * (q - 1)
    for e in E:
        gcd = Euclid(e, phi_n)
        print(f"Testing e={e}, phi(N)={phi_n}, GCD={gcd}")
        if gcd == 1 and e > 2:
            return e
    raise Exception("Provided primes for e did not work to find a valid relatively prime e")





# Implement this function
def generate_key_pairs(bits: int) -> tuple[int, int, int]:
    """
    Generate RSA public and private key pairs.
    Return N, e, d
    - N must be the product of two random prime numbers p and q
    - e and d must be multiplicative inverses mod (p-1)(q-1)
    """

    p = generate_large_prime(bits)
    q = 0
    while True:
        q = generate_large_prime(bits)
        if q != p:
            break
    N=p*q
    assert N.bit_length() >= bits, f"N is too small: {N.bit_length()} bits (expected >= {bits})"

    e = Finde(primes,p,q)

    x,y , gcd = ext_euclid(e,(p-1)*(q-1))
    if gcd != 1:
        raise Exception("e and phi(N) are not coprime, modular inverse cannot be computed")
    d = x % ((p-1)*(q-1))
    if d < 0:
        d += ((p-1)*(q-1))
    print(f"p={p}, q={q}, N={N}, e={e}, d={d}, gcd={gcd}")
    return N,e,d
