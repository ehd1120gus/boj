n = int(input())
arr = list(map(int, input().split()))

mem = [[0, 0] for _ in range(n)] # value, delete used value

def calculate(r: int):
    if r == 0:
        mem[0][0] = arr[0]
        mem[0][1] = 0
        return mem[0][0], mem[0][1]

    acc = mem[r - 1][0]
    acc_del = mem[r - 1][1]

    mem[r][0] = max(acc + arr[r], arr[r])
    mem[r][1] = max(acc, acc_del + arr[r])
    return mem[r][0], mem[r][1]

res = -1001
for i in range(n):
    acc, acc_del = calculate(i)
    res = max(res, acc, acc_del)

if res <= 0:
    res = max(arr)

print(res)