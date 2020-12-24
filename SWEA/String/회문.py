T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 가로 리스트 생성
    garo_lst = [list(input()) for _ in range(N)]

    result = ''
    # 가로 판단
    for g in garo_lst:
        for j in range(len(garo_lst)-M+1):
            if g[j:j+M] == g[j:j+M][::-1]:
                result = ''.join(g[j:j+M])
                break

    # 세로 리스트 생성
    sero_lst = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            sero_lst[j][i] = garo_lst[i][j]

    # 세로 판단
    for s in sero_lst:
        for j in range(len(sero_lst)-M+1):
            if s[j:j+M] == s[j:j+M][::-1]:
                result = ''.join(s[j:j+M])
                break

    print(f'#{test_case} {result}')
