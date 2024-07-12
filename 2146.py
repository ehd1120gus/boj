import sys
sys.stdin = open("input/2146.txt")

input = sys.stdin.readline
from collections import deque

def BFS(sy, sx, count):
    arr[sy][sx] = count
    queue = deque([(sy, sx)])
    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:
                arr[ny][nx] = count
                queue.append((ny, nx))
            elif 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 0:
                borders.add((y, x))

def TaxiDistance(y, x):
    val = arr[y][x]
    visited = set([(y, x)])
    queue = deque([(y, x, 0)])
    while queue:
        y, x, dist = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and (ny, nx) not in visited:
                if arr[ny][nx] and arr[ny][nx] != val:
                    return dist
                visited.add((ny, nx))
                queue.append((ny, nx, dist + 1))

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
borders = set()

MAX_DIST = 2 * N
count = 2 # use count for marking visited

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            BFS(i, j, count)
            count += 1

ans = MAX_DIST
for (i, j) in borders:
    ans = min(TaxiDistance(i, j), ans)

print(ans)