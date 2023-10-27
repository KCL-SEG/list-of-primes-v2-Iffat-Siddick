"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    x = 2
    total = 0
    while (total<= number_of_primes):
        for i in range(2, x):
            if (x % i != 0):
                list.append(x)
                total += 1
        x += 1
    return list

numbers = primes(5)
print(numbers)
