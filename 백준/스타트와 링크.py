from sys import stdin

N = int(stdin.readline())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]

def dfs(cnt, idx):
    global answer

    if cnt==N//2:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if selected[i] and selected[j]: # 둘다 선택 했다면
                    start += S[i][j]
                elif not selected[i] and not selected[j]: # 둘다 선택 안된 애라면
                    link += S[i][j]
        answer=min(answer, abs(start-link))
        return

    for i in range(idx, N):
        if selected[i]: # 숫자가 이미 선택되었다면
            continue
        selected[i] = 1
        dfs(cnt+1, i+1)
        selected[i] = 0

selected = [0]*N
answer = float('inf')

dfs(0, 0)
print(answer)

# 백준 PyPy3로 돌려야 돌아감.
