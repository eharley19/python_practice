primes = set()
num = 2

while True:

    for prime in primes:
        if num % prime == 0:
            break
        print(num)
        primes.add(num)

    num += 1
