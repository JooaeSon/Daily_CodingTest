from sys import stdin

N = int(stdin.readline())
A = [map(int, stdin.readline().split())]
O = [map(int, stdin.readline().split())]
N_operator = sum(O) # 연산자 총 개수


def dfs(cnt):
    global res, Max, Min

    if not -1000000000<=res<=1000000000:
        return

    if cnt >= N_operator-1:
        if res > Max: # 최대값 찾기
            Max=res
        if res < Min: # 최소값 찾기
            Min=res
        return

    for i in range(len(A)):
        dfs(cnt+1)
    return


res = 0
Max = float('-inf')
Min = float('inf')

dfs(0)

print(Max)
print(Min)