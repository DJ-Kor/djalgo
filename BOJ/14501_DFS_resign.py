import sys
readl = sys.stdin.readline

# 14501. 퇴사
# 다이나믹 프로그래밍, 브루트포스 알고리즘, DFS

N = int(readl())
T = []
P = []

for _ in range(N):
    t, p = map(int, readl().split())
    T.append(t)
    P.append(p)

# print(N, T, P)


def dfs(n, sm):
    global ans
    # 종료조건
    if n >= N:
        ans = max(ans, sm)
        return

    # 하부호출
    # 상담 o
    if n + T[n] <= N:
        dfs(n + T[n], sm + P[n])

    # 상담 x
    dfs(n + 1, sm)


ans = 0
dfs(0, 0)

print(ans)