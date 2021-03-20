from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
a, b, c, d = map(int, stdin.readline().split())


def cal(num, idx, plus, subtract, multiply, division):
    global N, Max, Min

    if idx==N:
        Max=max(num, Max)
        Min=min(num, Min)
        return
    else:
        if plus:
            cal(num+A[idx], idx+1, plus-1, subtract, multiply, division)
        if subtract:
            cal(num - A[idx], idx + 1, plus, subtract-1, multiply, division)
        if multiply:
            cal(num*A[idx], idx+1, plus, subtract, multiply-1, division)
        if division:
            cal(int(num / A[idx]), idx + 1, plus, subtract, multiply, division-1)


Max = float('-inf')
Min = float('inf')

cal(A[0], 1, a, b, c, d)

print(Max)
print(Min)