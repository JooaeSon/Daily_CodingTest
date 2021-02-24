T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())
    A = [input() for _ in range(N)]
    B = [input() for _ in range(M)]

    for a in A:
        if a in B:
            result += 1

    print(f'#{test_case} {result}')
