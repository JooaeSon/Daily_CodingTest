T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))

    w.sort() # N개의 화물 무게
    t.sort() # 트럭의 적재 용량

    for i in reversed(range(len(t))):
        while w:
            weight = w.pop()
            if t[i] >= weight:
                result += weight
                break

    print(f'#{test_case} {result}')
