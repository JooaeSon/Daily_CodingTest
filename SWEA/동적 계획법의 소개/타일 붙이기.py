

T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())
    memo = [0]*(N+1)
    memo[1], memo[2], memo[3] = 1, 3, 6

    for i in range(4, N+1):
        if memo[i] == 0:
            memo[i] = memo[i-1]+2*memo[i-2]+memo[i-3]

    print(f'#{test_case} {memo[N]}')
