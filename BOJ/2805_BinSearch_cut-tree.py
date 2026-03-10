import sys
readl = sys.stdin.readline

# 이분 탐색
# 2805. 나무 자르기

N, M = map(int, readl().split())  # (1 ≤ N ≤ 1,000,000, 1 ≤ M ≤ 2,000,000,000)
h = [int(x) for x in readl().split()]

s = 0
e = 20e8

ans = 0  # -1 로 하면 답 0일 때 오류!

while s + 1 < e:  # s < e 하면 무한루프 가능!
    curr = (s + e) // 2

    # tree = [x - curr for x in h if x > curr]
    # tot = sum(tree)
    tot = sum(x - curr for x in h if x > curr)  # 이게 더 빠름!

    # print(s, e, curr)
    # print(ans, tot)
    # print()

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

# print(c)
print(int(ans))