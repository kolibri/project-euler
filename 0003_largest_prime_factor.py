our_number = 600851475143


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        print(i)
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


max_prime = max(prime_factors(our_number))

print(max_prime)
