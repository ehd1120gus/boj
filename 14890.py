import sys
sys.stdin = open("input/14890.txt")

input = sys.stdin.readline

def canPass(road):
    ramp = [False] * N
    for i in range(N - 1):
        if road[i] == road[i + 1]:
            continue
        elif road[i] == road[i + 1] + 1:
            if i + L > N - 1:
                return False
            for j in range(i + 1, i + L + 1):
                if road[i + 1] != road[j] or ramp[j]:
                    return False
                ramp[j] = True
        elif road[i] == road[i + 1] - 1:
            if i - L + 1 < 0:
                return False
            for j in range(i - L + 1, i + 1):
                if road[i] != road[j] or ramp[j]:
                    return False
                ramp[j] = True
        else:
            return False
    return True

# def canPass(road):
#     ramp = [False] * N
    
#     for i in range(N - 1):
#         diff = road[i + 1] - road[i]
#         if diff == 0:
#             continue
#         if abs(diff) != 1:
#             return False
        
#         start, end = (i - L + 1, i + 1) if diff == 1 else (i + 1, i + L + 1)
#         if not 0 <= start < end <= N:
#             return False
        
#         if any(road[j] != road[i + (diff == -1)] or ramp[j] for j in range(start, end)):
#             return False
        
#         ramp[start:end] = [True] * L
    
#     return True


N, L = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

# convert arr to row and columns
roads = arr + list(zip(*arr))

print(sum(canPass(road) for road in roads))