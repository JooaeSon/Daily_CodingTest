T = int(input())

for test_case in range(1, T + 1):
    N, S = map(str, input().split())
    N = int(N)

    A = set()
    alphabets = sorted(set(list(S)))

    for alphabet in alphabets:
        for i in range(len(S)):
            if alphabet == S[i]:
                for j in range(i + 1, len(S) + 1):
                    A.add(S[i:j])
        if len(A) >= N:
            result = sorted(A)[N - 1]
            break

    print(f'#{test_case} {result[0]} {len(result)}')
