import argparse
import random


# This is a convenience function for main(). You don't need to touch it.
def prime_test(N: int, k: int) -> tuple[str, str]:
    return fermat(N, k), miller_rabin(N, k)


# You will need to implement this function and change the return value.
def mod_exp(x: int, y: int, N: int) -> int:
    if y == 0:
        return 1
    z = mod_exp(x, y // 2, N)
    if y % 2 ==0:
        return (z * z) % N
    else:
        return (z * z * x) % N


# You will need to implement this function and change the return value.
def fprobability(k: int) -> float:
    return 1/4**k


# You will need to implement this function and change the return value.
def mprobability(k: int) -> float:
    return 1/4**k


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.


def fermat(N: int, k: int) -> str:
    i=0
    while i<k:
        i+=1
        a = random.randint(2,N-1)
        if mod_exp(a,N-1,N)!= 1:
            return "composite"
    return "prime"


# You will need to implement this function and change the return value, which should be
# either 'prime' or 'composite'.
#
# To generate random values for a, you will most likely want to use
# random.randint(low, hi) which gives a random integer between low and
# hi, inclusive.
def miller_rabin(N: int, k: int) -> str:
    if fermat(N,k) == "composite":
        return "composite"
    z = 1  # Start with the identity for multiplication
    y = N - 1  # Start with the initial power
    a = random.randint(2, N - 1)  # Pick a random base a
    while mod_exp(a,y,N)==1 and y > 0:
        z = mod_exp(a,y,N)
        if y % 2 == 1:  # If y is odd
            y = y - 1 
            a= a*a
        y = y//2
    if z == N-1:
        return "prime"
    else:
        return "composite"


def main(number: int, k: int):
    fermat_call, miller_rabin_call = prime_test(number, k)
    fermat_prob = fprobability(k)
    mr_prob = mprobability(k)

    print(f'Is {number} prime?')
    print(f'Fermat: {fermat_call} (prob={fermat_prob})')
    print(f'Miller-Rabin: {miller_rabin_call} (prob={mr_prob})')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('number', type=int)
    parser.add_argument('k', type=int)
    args = parser.parse_args()
    main(args.number, args.k)
