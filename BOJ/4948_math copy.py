import sys
readl = sys.stdin.readline


def num_of_prime(n: int):
    np = 0

    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            np += 1

    return np


def is_prime(n: int):
    # Timeout
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    return True


while True:
    n = int(readl())

    # 종료 조건
    if not n:
        break

    res = num_of_prime(n)
    print(res)