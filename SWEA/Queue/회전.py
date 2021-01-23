from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))

    for _ in range(M):
        value = q.popleft()
        q.append(value)

    print(f'#{test_case} {q[0]}')
