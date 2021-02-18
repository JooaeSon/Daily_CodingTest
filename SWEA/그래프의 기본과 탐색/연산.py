from collections import deque

def BFS(N):
    global result, number

    deq = deque([(N, 0)])
    number[N] = -1
    # +1, -1, *2, -10
    while deq:
        num, cnt = deq.popleft()
        if num == M:
            result = cnt
            break

        for i in range(4):
            if i == 0 and 1 <= num + 1 <= 1000000 and number[num + 1] != -1:
                deq.append((num + 1, cnt + 1))
                number[num + 1] = -1
            elif i == 1 and 1 <= num - 1 <= 1000000 and number[num - 1] != -1:
                deq.append((num - 1, cnt + 1))
                number[num - 1] = -1
            elif i == 2 and 1 <= num * 2 <= 1000000 and number[num * 2] != -1:
                deq.append((num * 2, cnt + 1))
                number[num * 2] = -1
            elif i == 3 and 1 <= num - 10 <= 1000000 and number[num - 10] != -1:
                deq.append((num - 10, cnt + 1))
                number[num - 10] = -1


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    N, M = map(int, input().split())  # N -> M 으로 바꾸기
    number = [0] * 1000001
    BFS(N)

    print(f'#{test_case} {result}')
