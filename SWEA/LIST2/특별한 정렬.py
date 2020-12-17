from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()

    d = deque()
    for l in lst:
        d.append(l)

    result = []
    while len(d) != 0:
        result.append(d.pop())
        result.append(d.popleft())

    answer = ''
    for i in result[:10]:
        answer = answer+str(i) + " "

    print(f'#{test_case} {answer}')