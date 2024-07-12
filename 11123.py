import sys
sys.stdin = open("input/11123.txt")

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    board = [list(1 if cell == '#' else 0 for cell in input()) for _ in range(H)]

    count = 0
    visited = [[0] * W for _ in range(H)]
    
    def BFS(sx, sy):
        queue = [(sy, sx)]
        visited[sy][sx] = 1
        while queue:
            y, x = queue.pop(0)
            for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < H and 0 <= nx < W and board[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

    for i in range(H):
        for j in range(W):
            if board[i][j] and not visited[i][j]:
                count += 1
                BFS(j, i)

    print(count)