import sys
readl = sys.stdin.readline

N = int(readl())
counsel = [tuple(map(int, readl().split())) for _ in range(N)]

dp = [0] * (N + 1)
ans = 0

for i in range(N - 1, -1, -1):
    if counsel[i][0] + i > N:  # 날 종료
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], counsel[i][1] + dp[i + counsel[i][0]])

# print(dp)
print(dp[0])