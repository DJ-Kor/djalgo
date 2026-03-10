import sys
readl = sys.stdin.readline
from collections import deque

n, m = map(int, readl().split())
mm = [[int(x) for x in readl().split()] for _ in range(n)]

ans = [[0 for _ in range(m)] for _ in range(n)]
# visited = [[0 for _ in range(m)] for _ in range(n)]
move = ((-1, 0), (1, 0), (0, -1), (0, 1))
q = deque()

dest_x = -1
dest_y = -1
#
for i in range(n):
    for j in range(m):
        if mm[i][j] == 2:
            dest_x = i
            dest_y = j
            q.append((i, j, 0))

while q:
    x, y, c = q.popleft()

    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if not (0 <= nx < n and 0 <= ny < m):  # out of range
            continue
        elif not mm[nx][ny]:  # not land
            continue
        elif nx == dest_x and ny == dest_y:  # starting point
            continue
        elif ans[nx][ny]:  # visited
            continue

        ans[nx][ny] = c + 1
        q.append((nx, ny, c + 1))

# cant go = -1
for i in range(n):
    for j in range(m):
        if not ans[i][j]:
            ans[i][j] = -1
# not land and starting point = 0
for i in range(n):
    for j in range(m):
        if mm[i][j] == 0 or mm[i][j] == 2:
            ans[i][j] = 0

for i in range(n):
    print(*ans[i])