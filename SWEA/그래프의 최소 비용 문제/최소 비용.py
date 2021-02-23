from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    energy = [[float('inf')]*N for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    energy[0][0] = 0
    deq = deque([(0, 0)])
    while deq:
        i, j = deq.popleft()

        for k in range(4):
            N_i = i+dx[k]
            N_j = j+dy[k]
            if 0 <= N_i < N and 0 <= N_j < N:
                differ = 0
                if H[N_i][N_j] > H[i][j]:
                    differ = H[N_i][N_j] - H[i][j]

                if energy[N_i][N_j] > energy[i][j]+differ+1:
                    energy[N_i][N_j] = energy[i][j]+differ+1
                    deq.append((N_i, N_j))

    print(f'#{test_case} {energy[N-1][N-1]}')
