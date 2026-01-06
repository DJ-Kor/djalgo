import sys
readl = sys.stdin.readline

# 1145 : 적어도 대부분의 배수

N = [int(x) for x in readl().split()]
N.sort()
print(N)


def is_ans(cand):
    c = 0

    for n in N:
        if not cand % n:
            c += 1

    return True if c == 3 else False


for n in N:
    print(1170 % n)