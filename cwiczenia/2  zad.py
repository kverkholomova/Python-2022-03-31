def is_prime(n: int):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def is_b(a: int, b: int):
    return abs(a - b) == 2 and is_prime(a) and is_prime(b)


for i in range(2, 1000):

        if is_prime(i) and (not ((is_prime(i+2)) or is_prime(i-2))):
            print(i)


