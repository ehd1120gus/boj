import sys
sys.stdin = open("input/13398.txt")

N, M = map(int, input().split())
prev = [list(map(int,input().split())) for _ in range(N)]
after = [list(map(int,input().split())) for _ in range(N)]

# find first 1 in arr
sy, sx = -1, -1
for i in range(N):
    for j in range(M):
        if prev[i][j] != after[i][j]:
            sy, sx = i, j
            break

# BFS
start_val, target_val = prev[sy][sx], after[sy][sx]
visited = [[0] * M for _ in range(N)]
queue = [(sy, sx)]

visited[sy][sx] = 1
prev[sy][sx] = target_val

while queue:
    y, x = queue.pop(0)
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < N and 0 <= nx < M and prev[ny][nx] == start_val and not visited[ny][nx]:
            prev[ny][nx] = target_val
            visited[ny][nx] = 1
            queue.append((ny, nx))

for i in range(N):
    for j in range(M):
        if prev[i][j] != after[i][j]:
            print("NO")
            exit()
print("YES")