from sys import stdin
N, L = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
answer = 0

# 행 계산
for i in range(N):
    pre=board[i][0]
    cnt = 1
    for j in range(1, N):
        if board[i][j]==pre:
            cnt+=1
        elif board[i][j] == pre+1 and cnt >= 0:
            if cnt>=L:
                cnt=1
                pre=board[i][j]
            else:
                break
        elif board[i][j] == pre-1 and cnt>=0:
            cnt = -L+1
            pre = board[i][j]
        else:
            break
    else:
        if cnt>=0:
            answer+=1

# 열 계산
for j in range(N):
    pre=board[0][j]
    cnt = 1
    for i in range(1, N):
        if board[i][j]==pre:
            cnt+=1
        elif board[i][j] == pre+1 and cnt >= 0:
            if cnt>=L:
                cnt=1
                pre=board[i][j]
            else:
                break
        elif board[i][j] == pre-1 and cnt>=0:
            cnt = -L+1
            pre = board[i][j]
        else:
            break
    else:
        if cnt>=0:
            answer+=1


print(answer)
# 참고 : https://conak-diary.tistory.com/77