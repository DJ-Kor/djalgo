import sys
readl = sys.stdin.readline

# 4948. 베르트랑 공준
# 수학, 정수론, 소수 판정, 에라토스테네스의 체
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]


def num_of_prime(n: int):
    np = 0

    for i in range(n + 1, 2 * n + 1):
        if is_prime(i):
            # print(i)
            np += 1

    return np


def is_prime(n: int):
    ##### 1부터 시작이 아님!
    # if n == 2:
    #     return True
    # if not n % 2:  # 2의 배수
    #     return False

    # for p in primes:
    #     if not n % p:  # p의 배수
    #         return False

    # Timeout if range(2, n-1)
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return False

    # primes.append(n)
    return True


while True:
    n = int(readl())

    # 종료 조건
    if not n:
        break

    res = num_of_prime(n)
    print(res)
    # print(primes)

################################################################################
# Python3로도 170ms 나오는 에라토스테네스의 체 사용
check = [0] * 2 + [1] * 246912
for i in range(2, 246913):
    if check[i]:
        for j in range(i * 2, 246913, i):
            check[j] = 0

while True:
    x = int(input())
    if x == 0:
        break
    print(sum(check[x + 1:x * 2 + 1]))