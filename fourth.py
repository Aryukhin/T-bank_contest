import math

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_divisors_count(n):

    total_divisors = 0
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(1, sqrt_n):
        if n % i == 0:
            total_divisors += 1
            if i != n // i:
                total_divisors += 1
    return total_divisors

def count_special_numbers(l, r):
    count = 0
    for number in range(l, r + 1):
        if number > 1 and not is_prime(number):
            divisors = prime_divisors_count(number)
            if is_prime(divisors):
                count += 1
    return count

if __name__ == "__main__":
    l, r = map(int, input().split())
    print(count_special_numbers(l, r))
