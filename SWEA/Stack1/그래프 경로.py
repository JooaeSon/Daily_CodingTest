from _collections import deque
T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    lst = []
    for _ in range(E):
        key, value = map(int, input().split())
        lst.append((key, value))
    d = deque(lst)
    S, G = map(int, input().split())

    result = 0

    while d:
        start = S
        end = G
        cnt = 0
        while True:
            key, value = d.popleft()
            if key == start:
                cnt = 0
                start = value
            else:
                d.append((key, value))
                cnt += 1
            #print(d)

            if start == end:
                result = 1
                break

            if cnt >= len(d):
                result = 0
                break
        if result == 1:
            break
        elif result == 0:
            lst = list(d)
            chk = 0
            for l in lst:
                if l[0] != S:
                    chk += 1
            if chk == len(lst):
                break

    print(f'#{test_case} {result}')