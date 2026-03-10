import sys
readl = sys.stdin.readline

N, M = map(int, readl().split())
h = [int(x) for x in readl().split()]

s = 0
e = 20e8  # max

ans = 0  # min

while s + 1 < e:
    curr = (s + e) // 2

    tot = sum(x - curr for x in h if x > curr)  # 이게 더 빠름!

    if tot == M:
        ans = curr
        break

    elif tot > M:
        ans = curr
        s = curr
        continue

    elif tot < M:
        e = curr
        continue

print(int(ans))