from sys import stdin
N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())
cnt = 0


def calculate():
    global cnt
    # 주 감독 계산
    for i in range(N):
        A[i] -= B
        cnt += 1

    # 부 감독 계산
    for i in range(N):
        if A[i] > 0:
            if A[i] % C > 0:
                cnt+=1
            cnt+=A[i]//C

    return


calculate()
print(cnt)