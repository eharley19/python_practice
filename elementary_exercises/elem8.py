primes = set()
num = 2

while num < 50:
    for prime in primes:
        if num % prime == 0:
            break
    else:
        print(num)
        primes.add(num)
    num += 1
