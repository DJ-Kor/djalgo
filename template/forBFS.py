import sys
readl = sys.stdin.readline
from collections import deque

N, M = map(int, readl().split())
m = [[int(x) for x in readl().rstrip()] for _ in range(N)]

#
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]

print(N, M)
print(*m, sep='\n')

print(*visited, sep='\n')

move = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상하좌우


def BFS():
    q = deque()
    q.append((0, 0, 0, 1))
    visited[0][0] = [1, 0]

    while q:
        r, c, br, rou = q.popleft()

        for mr, mc in move:
            nr = r + mr
            nc = c + mc

            if nr == (N - 1) and nc == (M - 1):  # return rou+1 # Arrived
                if br:
                    visited[nr][nc][1] = min(visited[nr][nc][1], rou + 1)