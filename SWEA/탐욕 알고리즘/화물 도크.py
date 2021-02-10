T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N = int(input())

    timeline = []
    for _ in range(N):
        s, e = map(int, input().split())
        timeline.append([s, e])

    timeline.sort(key=lambda x: -x[1])  # 끝나는 시간 기준으로 내림 차순 정렬

    past_end = 0

    while timeline:
        start, end = timeline.pop()
        if past_end <= start:
            result += 1
            past_end = end

    print(f'#{test_case} {result}')
