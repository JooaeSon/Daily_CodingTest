# i번 세로선의 결과가 i번이 나오도록 사다리 게임을 조작하려면, 추가해야 하는 가로선 개수의 최솟값을 출력
def move():
    for i in range(N):
        num=i
        for j in range(H):
            if ladder[num][j]:
                num+=1
            elif ladder[num-1][j]:
                num-=1
        if i != num:
            return 0
    return 1

def dfs(cnt, idx, r):
    global answer

    if cnt == r:
        if move(): # i에서 시작해서 i로 나온다면 True
            answer=cnt
        return

    for i in range(idx, H):
        for j in range(N-1):
            if ladder[j][i]: # 사다리 가로선이 이미 존재하면 생략
                continue
            if j-1 >= 0 and ladder[j-1][i]: # 왼쪽에도 있다면 생략
                continue
            if j+1 < N and ladder[j+1][i]: # 오른쪽에도 있다면 생략
                continue
            # 자기 자신도 없고 양쪽에도 없다면 가로 사다리 놓기 가능
            ladder[j][i]=1
            dfs(cnt+1, i, r)
            ladder[j][i]=0


N, M, H = map(int, input().split())
# ladder 에 연결관계 저장. ladder[y-1][x-1]은 y-1번째 세로일 때 x-1 가로에서 x번째 가로로 이동 가능.
ladder = [[0]*H for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    ladder[b-1][a-1] = 1 # 사다리 가로선 채우기

answer = float('inf')

for r in range(4): # r은 정답인 추가할 수 있는 가로선 개수
    dfs(0, 0, r)
    if answer != float('inf'):
        print(answer)
        break
else:
    print(-1)

# 참고: https://chldkato.tistory.com/151