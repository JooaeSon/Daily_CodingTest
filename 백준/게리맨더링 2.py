

def divide(x, y, d1, d2, answer):
    while True:
        while True:
            lx, ly, rx, ry = x+d1, y-d1, x+d2, y+d2
            if rx == N-1 or ry == N:
                break
            bx, by = x+d1+d2, y-d1+d2
            if bx >= N or by >= N or by < 0:
                break
            answer = min(answer, find_min(x, y, lx, ly, rx, ry, by))
            d2+=1
        d1 += 1
        if x +d1 == N-1 or y-d1 ==-1:
            break
        d2 =1

    return answer

def find_min(x, y, lx, ly, rx, ry, by):

    return

N = int(input())

a, nsum = [], 0
for _ in range(N):
    row = list(map(int, input().split()))
    nsum += sum(row)
    a.append(row)

answer=float('inf')
for i in range(N-2):
    for j in range(1, N-1):
        d1, d2 = 1, 1
        answer = divide(i, j, d1, d2, answer)

print(answer)

